import os
from threading import Thread, Event

import praw

import database_connection
import get_posts as ps
import visualizer
from datetime import datetime
import ftp_writer


global keys

subreddits = ['dankmemes', 'askreddit']


def get_keys():
    file = open('keys.txt', 'r')
    keys_dict = {file.readline(): file.readline().split()[0][:14],
                 file.readline(): file.readline().split()[0][:27],
                 file.readline(): file.readline().split()[0][:16],
                 file.readline(): file.readline()}
    return keys_dict


keys = get_keys()
reddit = praw.Reddit(client_id=keys['personal\n'], client_secret=keys['secret\n'], user_agent='Analytics',
                     username='Kristophersson', password=keys['password\n'])


def run():
    for sub in subreddits:
        ps.get_data(reddit, reddit.subreddit(sub).new(limit=10), sub, 'new')


def visualize_post(post=None, id_post=None):
    if post:
        visualizer.create_plot(post.get_panda(), 'new')
    elif id_post:
        ps.load_post_history_element_from_db(id_post=id_post)
        visualizer.create_plot(ps.load_post_history_element_from_db(id_post=id_post), 'new')


visualize_post(id_post='b0ztaw')


def visualize_all(sub_filter):
    for sub in subreddits:
        print(sub)
        visualize_subreddit(sub, sub_filter)


def visualize_array(arr):
    pass


def visualize_subreddit(sub, sub_filter):
    try:
        date = datetime.now()
        os.chdir("../../../../../Code")
        panda = ps.get_posts_of_subreddit_by_id(sub, sub_filter, path='../Data/' + str(date.month) + "." +
                                                                      str(date.day) + "/" + sub_filter)
        visualizer.create_plot(panda, sub_filter)
    except FileNotFoundError:
        print('File doesn\'t exist at \t' + os.getcwd())


class MyThread(Thread):
    time = datetime.now().time()
    last_saved = int(time.minute)

    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        i = 0
        while not self.stopped.wait(30):
            print("running thread " + str(i))
            run()
            if int(self.time.minute) % 2 == 0:
                print('visualizing')
                # visualize_all('hot')
                self.last_saved = int(self.time.minute)
            elif int(self.time.minute) % 20 == 0:
                visualize_all('new')
            self.time = datetime.now().time()
            print('done: ' + str(self.time.hour) + ":" + str(self.time.minute))
            i = i + 1


def start_thread():
    stop_flag = Event()
    thread = MyThread(stop_flag)
    thread.start()


# ftp_writer.write(keys['ftp-password\n'])


# start_thread()
