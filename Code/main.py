import os
from threading import Thread, Event

import praw
import get_posts as ps
import visualizer
from datetime import datetime
import ftp_writer


def get_keys():
    file = open('keys.txt', 'r')
    keys_dict = {file.readline(): file.readline().split()[0][:14],
                 file.readline(): file.readline().split()[0][:27],
                 file.readline(): file.readline().split()[0][:16],
                 file.readline(): file.readline()}
    global keys
    return keys_dict


global keys
keys = get_keys()
reddit = praw.Reddit(client_id=keys['personal\n'], client_secret=keys['secret\n'], user_agent='Analytics',
                     username='Kristophersson', password=keys['password\n'])

subreddits = ['dankmemes']


def run():
    for sub in subreddits:
        ps.get_data(reddit, reddit.subreddit(sub).hot(limit=50), sub)


"""
for i in range(len(subreddits)):
    ps.subreddits[i].save_posts_to_file()
    print(ps.subreddits[i].get_panda())
"""

# visualizer.create_plot(ps.subreddits[0].get_array_from_csv())


def visualize_post(post):
    visualizer.create_plot(ps.subreddits[post].get_array_from_csv())


def visualize_all():
    for sub in ps.subreddits:
        print(sub)
        visualizer.create_plot(sub.get_array_from_csv())


def go_in_directory(dir, arr):
    os.chdir(dir)
    dirs = os.listdir(".")
    for dirc in dirs:
        if os.path.isdir(dirc):
            arr = go_in_directory(dirc, arr)
        elif dirc.endswith('.csv'):
            arr.append([dirc][0][:6])
            os.chdir('../')
            return arr
        elif dirc.endswith('.png'):
            pass
        else:
            while not os.path.isdir(dirc):
                os.chdir('../')
            go_in_directory(dirc, arr)
    return arr


def visualize_subreddit(sub):
    """
    Pseudo Code:
        get all posts in (sub) folder
        get data from those csv files
    how to get all file id's in a folder:
        make use of go_in_directory
    """
    panda = ps.get_posts_of_subreddit_by_id('askreddit', path='../Data/3.3/Hot')
    visualizer.create_plot(panda)


# visualize_subreddit('askreddit')


'''    
def get_array_from_csv(sub):
    temp = {'time_saved': [], 'score': [], 'id': "", 'subreddit': sub}
    for thread in self.threads:
        pan = thread.get_panda_from_csv(self.name)
        try:
            temp['score'].append(pan['score'])
            temp['score'].append(0)
            r = pan['time_saved']
            temp['time_saved'].append([thread.created])
            temp['time_saved'].append(r)
            temp['score'].insert(0, [0])
            temp['id'] = pan['id'][0]
            print('id: ' + str(pan['id'][0]))
        except TypeError:
            print(TypeError)
    return temp
'''


# visualize_subreddit('dankmemes')


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
            if int(self.time.minute) >= self.last_saved + 5:
                print('visualizing')
                # visualize_all()
                self.last_saved = int(self.time.minute)
            self.time = datetime.now().time()
            print('done: ' + str(self.time.hour) + ":" + str(self.time.minute))
            i = i + 1


def start_thread():
    stop_flag = Event()
    thread = MyThread(stop_flag)
    thread.start()


# ftp_writer.write(keys['ftp-password\n'])


start_thread()
