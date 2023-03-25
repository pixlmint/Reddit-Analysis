class PostHistoryElement:
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
