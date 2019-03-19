import os
import datetime as dt
import sys

import plotly.graph_objs as go
import plotly.io as pio
import plotly.plotly as py
import database_connection as db


def create_plot(data, sub_filter):
    try:
        fig = go.Figure()
        fig.add_scatter(x=data['time_saved'],
                        y=data['score'],
                        mode='lines')
        save_image(fig, data['id'][0], data['subreddit'][0], sub_filter)
    except IndexError:
        print("Error while visualising\t" + os.getcwd() + '\tIndex out of range\t' + str(len(data['id'])))


def visualize_multiple_posts(data):
    fig = []
    for dataset in data:
        fig.append(
            go.Scatter(
                x=dataset['time_saved'],
                y=dataset['score'],
                name=str(dataset['id'])
            )
        )
    # save_image(fig, data['id'][0], data['subreddit'][0], '')
    url = py.plot(fig, filename='test')
    print(url)


def save_image(fig, id, sub, sub_filter):
    date = dt.datetime.now().date()
    if not os.getcwd().split(os.sep)[-1] == str(id):
        change_directory(sub=sub, id=str(id), date=str(date.month) + "." + str(date.day), filter=sub_filter)
    try:
        pio.write_image(fig, str(id) + ".png")
    except PermissionError:
        print('unable to write to file')


def convert_to_binarydata(filename):
    with open(filename, 'rb') as file:
        binary_data = file.read()
    print(sys.getsizeof(binary_data))
    return binary_data


def save_to_db(id):
    print('trying to write image to db')
    try:
        # db.write_graph(id, convert_to_binarydata(id + '.png'))
        print('done writing image to db')
    except Exception:
        print(Exception.with_traceback())


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
