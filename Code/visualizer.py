import os
import datetime as dt

import plotly.graph_objs as go
import plotly.io as pio


def create_plot(data, sub_filter):
    for i in range(len(data['id'])):
        try:
            fig = go.Figure()
            fig.add_scatter(x=data['time_saved'][i],
                            y=data['score'][i],
                            mode='lines')
            save_image(fig, data['id'][i], data['subreddit'], sub_filter)
        except IndexError:
            print("Error while visualising\t" + os.getcwd() + '\tIndex out of range\t' + str(len(data['id'])))


def save_image(fig, id, sub, sub_filter):
    date = dt.datetime.now().date()
    if not os.getcwd().split(os.sep)[-1] == str(id):
        change_directory(sub=sub, id=str(id), date=str(date.month) + "." + str(date.day), filter=sub_filter)
    try:
        pio.write_image(fig, str(id) + ".png")
    except PermissionError:
        print('unable to write to file')


def change_directory(sub=None, id=None, date=None, filter=None):
    id = str(id)
    dirs = os.getcwd().split(os.sep)
    if sub is not None:
        if dirs[-1] == "Code" or dirs[-1] == "Data":
            os.chdir("../Data")
            try:
                os.mkdir(str(date))
                os.chdir(str(date))
            except FileExistsError:
                os.chdir(str(date))
            change_directory(sub=sub, id=id, date=date, filter=filter)
        elif dirs[-1] == str(date):
            try:
                os.mkdir(filter)
                os.chdir(filter)
            except FileExistsError:
                os.chdir(filter)
            change_directory(sub=sub, id=id, date=date, filter=filter)
        elif dirs[-1] == filter:
            try:
                os.mkdir(sub)
                os.chdir(sub)
            except FileExistsError:
                os.chdir(sub)
            change_directory(sub=sub, id=id, date=date, filter=filter)
        elif dirs[-1] == sub:
            try:
                os.mkdir(id)
                os.chdir(id)
            except FileExistsError:
                os.chdir(id)
            return
        elif dirs[-1] == id:
            return
        else:
            os.chdir(".." + os.sep)
            change_directory(sub=sub, id=id, date=date, filter=filter)
