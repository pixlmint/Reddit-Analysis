import os
from threading import Thread, Event

import praw

import Code.database_connection as db
import Code.get_posts as ps
import Code.visualizer as visualizer
from datetime import datetime
from Code.config import reddit as reddit_keys

subreddits = ['dankmemes', 'askreddit']


reddit = praw.Reddit(client_id=reddit_keys['personal'], client_secret=reddit_keys['secret'], user_agent='Analytics',
                     username=reddit_keys['username'], password=reddit_keys['password'])


def run():
    for sub in subreddits:
        ps.get_data(reddit, reddit.subreddit(sub).new(limit=10), sub, 'new')


def visualize_post(post=None, id_post=None):
    if post:
        try:
            visualizer.create_plot(post.get_panda(), 'new')
        except Exception:
            print('unable to visualize a post')
    elif id_post:
        ps.load_post_history_element_from_db(id_post=id_post)
        visualizer.create_plot(ps.load_post_history_element_from_db(id_post=id_post), 'new')


def visualize_all():
    for post in ps.posts:
        visualize_post(post=post)


def visualize_array(arr):
    pass


def visualize_todays_posts():
    posts = db.get_posts_by_date(datetime.now())
    for post in posts:
        visualize_post(posts[post])
    print('visualized posts')


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
        thread_count = 1
        while not self.stopped.wait(30):
            print("running thread " + str(thread_count))
            run()
            self.time = datetime.now().time()
            print('done: ' + self.time.strftime('%H:%M'))
            thread_count += 1


stop_thread = Event()


def start_thread():
    thread = MyThread(stop_thread)
    thread.start()


# ftp_writer.write(keys['ftp-password\n'])

# start_thread()
