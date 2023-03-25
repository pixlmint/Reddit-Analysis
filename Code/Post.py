import datetime as dt
from Code.PostHistoryElement import PostHistoryElement
from Code import database_connection as db
import pandas as pd


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
        pan = {'score': [], 'time_saved': [], 'id': self.id_post,
               'subreddit': db.get_name_of_subreddit(self.id_subreddit)}
        for element in self.post_history:
            pan['score'].append(element.score)
            d = element.time_saved.strftime("%d.%m.%Y %H:%M:%S")
            pan['time_saved'].append(d)
        panda = pd.DataFrame(pan)
        return panda

    def add_history_element(self, score, time_saved, num_comms):
        self.post_history.append(PostHistoryElement(score, time_saved, num_comms, self.id_post))

    def check_growth(self):
        growth = 0
        for element in self.post_history:
            growth += element.score
        return growth
