import datetime as dt
import database_connection as db

import pandas as pd

global posts, subreddits, reddit
posts = []
subreddits = []


def get_data(reddit_instance, subreddit_instance, subreddit_name, sub_filter):
    """if subreddit_name not in subreddits:
        if not db.subreddit_in_db(subreddit_name):
            db.write_subreddit_to_db(subreddit_name)
        subreddits.append(subreddit_name)"""
    for submission in subreddit_instance:
        if not db.post_in_db(submission.id):
            print('writing post %s to db' % submission.id)
            t = dt.datetime.utcfromtimestamp(submission.created)
            post = {'title': submission.title,
                    'url': submission.url,
                    'score': submission.score,
                    'id_post': submission.id,
                    'created': t,
                    'id_subreddit': db.get_id_of_subreddit(subreddit_name)
                    }
            db.write_post_to_db(post)
        else:
            print('post %s already in db' % submission.id)
        posthistoryelement = {'saved': dt.datetime.now(),
                              'score': submission.score,
                              'num_comments': submission.num_comments,
                              'id_post': submission.id}
        db.write_posthistoryelement_to_db(posthistoryelement)


def get_posts_to_be_kept_up_to_date():
    """:returns array with id's of posts that must be updated"""
    arr_newest_posts = db.get_posts_younger_than(6)


def is_loadable(date_created):
    now = dt.datetime.now()
    ret = date_created + dt.timedelta(hours=6) - dt.timedelta(hours=float(now.hour), minutes=float(now.minute))
    print('ret: ' + str(ret))


class MySubreddit:
    def __str__(self):
        return self.name

    def __init__(self, name, filter):
        self.name = name
        self.filter = filter
        self.threads = []

    def save(self):
        ret = []
        for thread in self.threads:
            ret.append(thread.save())
        return ret

    def check_if_post_is_in_list(self, post_id=None):
        for thread in self.threads:
            if thread.id == post_id:
                return True
        return False

    def get_post_by_id(self, id):
        for thread in self.threads:
            if thread.id == id:
                return thread

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

    def get_array_from_csv_by_id(self, ids, sub_filter):
        temp = {'time_saved': [], 'score': [], 'id': [], 'subreddit': self.name}
        for id in ids:
            try:
                temp2 = temp
                a = get_panda_from_csv(id, self.name, sub_filter)
                temp2['score'].append(a['score'])
                temp2['time_saved'].append(a['time_saved'])
                temp2['id'].append(id)
                temp = temp2
            except TypeError:
                print("Type Error with: " + str(id))
        return temp

    def get_posts_younger_than(self, arr):
        ret_arr = []
        for post_id in arr:
            change_directory(self.name, post_id, str(dt.datetime.now().month) + '.' + str(dt.datetime.now().day),
                             self.filter)
            try:
                file = open(post_id + '.txt', 'r')
                arr_file = file.readline().split(';')
                file.close()
                date_posted = arr_file[-1]
                datetime_object = dt.datetime.strptime(date_posted, '%Y-%m-%d %H:%M:%S')
                compare_date = dt.datetime.now() - dt.timedelta(hours=6)
                if datetime_object >= compare_date:
                    print('post %s not too old' % post_id)
                    ret_arr.append(post_id)
            except FileNotFoundError:
                print('file %s doesn\'t exist.' % post_id)
            except ValueError:
                print('Couldn\'t get date from post id %s' % post_id)
        return ret_arr


class Post:
    def __init__(self, title, id, url, created):
        self.title = title
        self.id = id
        self.url = url
        self.created = dt.datetime.fromtimestamp(created)
        self.post_history = []

    def get_dict(self):
        ret = {'score': [], 'comms_num': [], 'time_saved': []}
        for element in self.post_history:
            ret['score'].append(element.score)
            ret['comms_num'].append(element.comms_num)
            ret['time_saved'].append(element.time_saved)
        return ret

    def get_panda(self):
        return pd.DataFrame(self.get_dict())

    def add_history_element(self, score, time_saved, num_comms):
        self.post_history.append(PostHistoryElement(score, time_saved, num_comms))


class PostHistoryElement:
    score = 0
    time_saved = None
    comms_num = None

    def __str__(self):
        return 'score: ' + str(self.score) + '\tNumber of comments: ' + str(self.comms_num) + \
               '\ttime saved: ' + str(self.time_saved)

    def __init__(self, score, time_saved, num_comms):
        self.score = score
        self.time_saved = time_saved
        self.comms_num = num_comms

    def get_element(self):
        return [self.score, self.time_saved, self.comms_num]

