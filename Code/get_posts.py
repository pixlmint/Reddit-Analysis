import datetime as dt
import database_connection as db

import pandas as pd

global reddit
posts = []
subreddits = []


def get_data(reddit_instance, subreddit_instance, subreddit_name, sub_filter):
    global reddit
    reddit = reddit_instance
    if subreddit_name not in subreddits:
        print('subreddit %s not in array' % subreddit_name)
        if not db.subreddit_in_db(subreddit_name):
            print('subreddit %s not in db' % subreddit_name)
            db.write_subreddit_to_db(subreddit_name)
        subreddits.append(subreddit_name)
    for post_id in get_posts_to_be_kept_up_to_date(subreddit_instance):
        print('loading %s' % post_id)
        for post in posts:
            if post_id is post.id_post:
                print('\tpost %s already already existing' % post.id_post)
                break
        else:
            create_new_post(post_id)
        for post in posts:
            if post_id is post.id_post:
                print('now creating post history element for post %s' % post.id_post)
                create_new_post_history_element(post)
    '''for submission in subreddit_instance:
        if submission.id not in posts:
            if not db.post_in_db(submission.id):
                t = dt.datetime.utcfromtimestamp(submission.created)
                post = Post(submission.title, submission.id, submission.url, t, 1)
                db.write_post_to_db(post.get_dict())
                posts.append(post)
            else:
                print('post %s already in db' % submission.id)
        else:
            posts.append(submission.id)
        posthistoryelement = {'saved': dt.datetime.now(),
                              'score': submission.score,
                              'num_comments': submission.num_comments,
                              'id_post': submission.id}
        db.write_posthistoryelement_to_db(posthistoryelement)'''


def get_posts_to_be_kept_up_to_date(subreddit_instance):
    """:returns array with id's of posts that must be updated"""
    arr_post_ids = []
    for post in posts:
        timediff = (dt.datetime.now() - post.created).seconds / 3600
        if timediff > 5:
            growth = post.check_growth()
            if growth <= 2:
                print("Post %s too old, removing it now" % post.id_post)
                posts.remove(post)
        else:
            arr_post_ids.append(post.id_post)

    for submission in subreddit_instance:
        for post in posts:
            if post.id_post is submission.id:
                break
        else:
            arr_post_ids.append(submission.id)
    return arr_post_ids


def create_new_post(id_post):
    submission = reddit.submission(id=id_post)
    post = Post(submission.title, id_post, submission.url, submission.created,
                db.get_id_of_subreddit(submission.subreddit)[0])
    posts.append(post)
    if not db.post_in_db(id_post):
        db.write_post_to_db(post.get_dict())


def create_new_post_history_element(post):
    submission = reddit.submission(id=post.id_post)
    element = PostHistoryElement(submission.score, dt.datetime.now(), submission.num_comments, post.id_post)
    post.post_history.append(element)
    db.write_posthistoryelement_to_db(element.get_dict())


def is_loadable(date_created):
    now = dt.datetime.now()
    ret = date_created + dt.timedelta(hours=6) - dt.timedelta(hours=float(now.hour), minutes=float(now.minute))
    print('ret: ' + str(ret))


class Post:
    def __init__(self, title, id_post, url, created, id_subreddit):
        self.title = title
        self.id_post = id_post
        self.url = url
        try:
            self.created = dt.datetime.fromtimestamp(created)
        except:
            self.created = created
        self.id_subreddit = id_subreddit
        self.post_history = []

    def get_dict(self):
        post = {'title': self.title,
                'url': self.url,
                'id_post': self.id_post,
                'created': self.created,
                'id_subreddit': self.id_subreddit
                }
        return post

    def get_panda(self):
        return pd.DataFrame(self.get_dict())

    def add_history_element(self, score, time_saved, num_comms):
        self.post_history.append(PostHistoryElement(score, time_saved, num_comms))

    def check_growth(self):
        growth = 0
        for element in self.post_history:
            growth += element.score
        return growth


class PostHistoryElement:
    score = 0
    time_saved = None
    comms_num = None

    def __str__(self):
        return 'score: ' + str(self.score) + '\tNumber of comments: ' + str(self.comms_num) + \
               '\ttime saved: ' + str(self.time_saved)

    def __init__(self, score, time_saved, num_comms, id_post):
        self.score = score
        self.time_saved = time_saved
        self.comms_num = num_comms
        self.id_post = id_post

    def get_element(self):
        return [self.score, self.time_saved, self.comms_num]

    def get_dict(self):
        ret = {'score': self.score,
               'saved': self.time_saved,
               'num_comments': self.comms_num,
               'id_post': self.id_post}
        return ret
