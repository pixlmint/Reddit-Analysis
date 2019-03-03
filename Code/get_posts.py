import datetime as dt
import os
import traceback

import pandas as pd


global posts
posts = []
global subreddits
subreddits = []
global reddit


def get_data(redd, subreddit, sub):
    global reddit
    reddit = redd

    c = MySubreddit(sub)
    subreddits.append(c)
    first_run = True
    for submission in subreddit:
        a = Post(submission.title, submission.score, submission.id, submission.url, submission.num_comments,
                 submission.created)
        if first_run:
            c.threads = []
            first_run = False
        c.threads.append(a)
    c.save_posts_to_file()


def get_posts_of_subreddit_by_id(sub, path=None):
    arr = go_in_directory(path + "/" + sub, [])
    print(arr)
    c = MySubreddit(sub)
    subreddits.append(c)
    return c.get_array_from_csv_by_id(arr)


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


class MySubreddit:
    threads = []
    name = ""

    def __str__(self):
        return self.name

    def __init__(self, name):
        self.name = name

    def save(self):
        ret = []
        for thread in self.threads:
            ret.append(thread.save())
        return ret

    def get_panda(self):
        temp = {'title': [], 'score': [], 'id': [], 'url': [], 'comms_num': [], 'created': [], 'time_saved': []}
        for thread in self.threads:
            temp['title'].append(thread.title)
            temp['score'].append(thread.score)
            temp['id'].append(thread.id)
            temp['url'].append(thread.url)
            temp['comms_num'].append(thread.comms_num)
            temp['created'].append(thread.created)
            temp['time_saved'].append(thread.time_saved)
        return pd.DataFrame(temp)

    def save_posts_to_file(self):
        for thread in self.threads:
            thread.save_post_to_file(self.name)


    '''
        def get_panda_from_csv(self):
            temp = {'score': [], 'time_saved': []}
            for thread in self.threads:
                pan = thread.get_panda_from_csv(self.name)
                temp['score'].append(pan['score'])
                temp['time_saved'].append(pan['time_saved'])
            return pd.DataFrame(temp)
    '''
    def get_array_from_csv(self):
        temp = {'time_saved': [], 'score': [], 'id': "", 'subreddit': self.name}
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

    def get_array_from_csv_by_id(self, ids):
        temp = {'time_saved': [], 'score': [], 'id': [], 'subreddit': self.name}
        for id in ids:
            try:
                temp2 = temp
                a = get_panda_from_csv(id, self.name)
                temp2['score'].append(a['score'])
                r = a['time_saved']
                temp2['time_saved'].append(a['created'][0])
                temp2['time_saved'].append(r)
                temp2['score'].insert(0, [0])
                temp2['id'].append(a['id'][0])
                temp = temp2
            except TypeError:
                print("Type Error with: " + str(id))
        return temp


class Post:
    title = ''
    score = 0
    id = 0
    url = ''
    comms_num = 0
    created = None
    time_saved = None

    def __init__(self, title, score, id, url, comms_num, created):
        self.title = title
        self.score = score
        self.id = id
        self.url = url
        self.comms_num = comms_num
        self.created = dt.datetime.fromtimestamp(created)
        self.time_saved = dt.datetime.now()

    def get_dict(self):
        ret = {'title': self.title, 'score': self.score, 'id': self.id, 'url': self.url, 'comms_num': self.comms_num,
               'created': self.created, 'time_saved': self.time_saved}
        return ret

    def get_panda(self):
        return pd.DataFrame(self.get_dict(), index=[0])

    def save(self):
        return {'url': self.url, 'id': self.id, 'score': self.score, 'title': self.title, 'comms_num': self.comms_num,
                'created': self.created}

    def save_post_to_file(self, sub):
        if not os.getcwd().split(os.sep)[-1] == str(self.id):
            date = dt.datetime.now().date()
            change_directory(sub, str(self.id), date=str(date.month) + "." + str(date.day), filter="Hot")
        path = str(self.id + '.csv')
        if not os.path.isfile(path):
            self.get_panda().to_csv(path, index=True)
        else:
            try:
                with open(path, 'a') as fd:
                    try:
                        self.get_panda().to_csv(fd, header=False)
                    except UnicodeEncodeError:
                        print(os.getcwd())
            except PermissionError:
                print("Couldn't read file at " + os.getcwd())

    def get_panda_from_csv(self, sub):
        date = dt.datetime.now().date()
        if not os.getcwd().split(os.sep)[-1] == self.id:
            change_directory(sub, str(self.id), date=str(date.month) + "." + str(date.day), filter="Hot")
        path = str(self.id + '.csv')
        ret = None
        try:
            return pd.read_csv(path)
        except UnicodeDecodeError:
            print("error")
            return


def get_panda_from_csv(post_id, sub):
    date = dt.datetime.now().date()
    if not os.getcwd().split(os.sep)[-1] == post_id:
        change_directory(sub, str(post_id), date=str(date.month) + "." + str(date.day), filter="Hot")
    path = str(post_id + '.csv')
    ret = None
    try:
        print(path + ": \n" + str(pd.read_csv(path)['score'].dtype))
        return pd.read_csv(path)
    except UnicodeDecodeError:
        print("error")
        return


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
