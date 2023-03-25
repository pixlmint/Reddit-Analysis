import os
import datetime as dt

import plotly.graph_objs as go
import plotly.io as pio


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
    save_image(fig, data['id'][0], data['subreddit'][0], '')
    # url = py.plot(fig, filename='test')


def save_image(fig, id, sub, sub_filter):
    date = dt.datetime.now().date()
    target_path = generate_path(subreddit=sub, id_post=id, date=str(date.month) + "." + str(date.day))
    try:
        pio.write_image(fig, os.path.join(target_path, "some_data.png"))
    except PermissionError:
        print('unable to write to file')


# Reddit-Analysis/Data/dankmemes/2022-01-01/id_post
def generate_path(subreddit, id_post, date):
    path_str = os.path.join(os.getcwd(), "Data", subreddit, str(date), str(id_post))

    if not os.path.isdir(path_str):
        os.makedirs(path_str, exist_ok=True)

    return path_str
