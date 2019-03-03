import os
import datetime as dt
import traceback

import plotly.graph_objs as go
import plotly.io as pio


def create_plot(data):
    for i in range(len(data['time_saved'])):
        print('score:\n' + str(data['score'][i]) + "\ndate saved:\n" + str(data['time_saved'][i]))
        try:
            fig = go.Figure()
            fig.add_scatter(x=data['time_saved'][i],
                            y=data['score'][i],
                            mode='lines')
            save_image(fig, data['id'][i], data['subreddit'])
        except ValueError:
            print("Error while visualising\t" + os.getcwd())


def save_image(fig, id, sub):
    date = dt.datetime.now().date()
    if not os.getcwd().split(os.sep)[-1] == str(id):
        change_directory(sub=sub, id=str(id), date=str(date.month) + "." + str(date.day), filter="Hot")
    try:
        pio.write_image(fig, str(id) + ".png")
    except PermissionError:
        print('unable to write to fail')


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
