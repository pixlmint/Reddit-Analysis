import datetime as dt
import os

import pandas as pd

global posts, subreddits, reddit
posts = []
subreddits = []


def get_data(redd, subreddit, sub, sub_filter):
    """New Posts"""
    print('Getting data for ' + sub)
    c = None
    """
    if this subreddit (MySubreddit instance) isn't in list 'subreddits': create new instance, put in list.
    else: get instance
    """
    print('\tlength of subreddits: ' + str(len(subreddits)))
    for subredd in subreddits:
        if str(subredd) == sub and subredd.filter == sub_filter:
            print('\tSubreddit ' + sub + ' found in list.')
            c = subredd
            print('\t\tbreaking')
            break
        else:
            print('\tSubreddit ' + sub + ' not found in list, creating it now')
            c = MySubreddit(sub, sub_filter)
            subreddits.append(c)
            print('\t\tbreaking')
            break

    '''safety measure'''
    if c is None:
        print('\tc is None, adding first sub now: ' + sub)
        c = MySubreddit(sub, sub_filter)
        subreddits.append(c)
    global reddit
    reddit = redd

    '''
    loop through submissions in subreddit instance
        if the post isn't in the list found in MySubreddit instance, crete new Post instance
    add new data into new PostHistoryElement, add to list in Post
    '''
    arr_posts = get_ids_of_posts_in_subreddit(sub, '../Data/' + str(dt.datetime.now().month) + '.' + str(dt.datetime.now().day) + '/hot')
    for submission in subreddit:
        if submission.id in arr_posts and not c.check_if_post_is_in_list(post_id=submission.id):
            print('submission ' + submission.id + " is saved")
            a = Post(submission.title, submission.id, submission.url, submission.created)
            c.threads.append(a)
            # print(get_panda_from_csv(submission.id, sub, sub_filter))
            a.create_post_history_elements_from_panda(get_panda_from_csv(submission.id, sub, sub_filter))
        elif not c.check_if_post_is_in_list(post_id=submission.id):
            print('\t\tsubmission ' + submission.id + ' not in list in ' + sub + ', creating it now.')
            a = Post(submission.title, submission.id, submission.url, submission.created)
            c.threads.append(a)
        else:
            print('\t\tsubmission already in list')
            a = c.get_post_by_id(submission.id)
        print('\tcreating new post_history object for post id: ' + a.id)
        a.post_history.append(PostHistoryElement(submission.score, dt.datetime.now().strftime('%Y-%m-%d %H-%M-%S'), submission.num_comments))
        print('\t\t\tlength of post history: ' + str(len(a.post_history)))

    '''Save data to csv file'''
    c.save_posts_to_file(sub_filter)


def is_loadable(date_created):
    now = dt.datetime.now()
    ret = date_created + dt.timedelta(hours=6) - dt.timedelta(hours=float(now.hour), minutes=float(now.minute))
    print('ret: ' + str(ret))


def get_posts_of_subreddit_by_id(sub, sub_filter, path=None):
    """
    :rtype: dictionary of thread data
    """
    arr = go_in_directory(path + "/" + sub, [])
    c = MySubreddit(sub, sub_filter)
    subreddits.append(c)
    return c.get_array_from_csv_by_id(arr, sub_filter)


def get_ids_of_posts_in_subreddit(sub, path):
    return go_in_directory(path + "/" + sub, [])


def go_in_directory(dir, arr):
    try:
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
    except FileNotFoundError:
        if 'Code' in os.getcwd().split(os.sep):
            os.chdir('../Data')
        elif 'Data' not in os.getcwd().split(os.sep):
            print(os.getcwd())
            os.chdir('../../../../')
            go_in_directory(dir, arr)
        else:
            print(os.getcwd())
            return []
    return arr


def create_date_dir():
    if os.getcwd().split(os.sep)[-1] == 'Code' or os.getcwd().split(os.sep)[-1] == 'Data':
        os.chdir('../Data')
        os.mkdir(str(dt.datetime.now().month) + "." + str(dt.datetime.now().day))
    else:
        os.chdir('../')
        create_date_dir()


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

    def save_posts_to_file(self, sub_filter):
        """
        :param sub_filter: filter used to get subreddit data (hot/new/top...)
        """
        try:
            create_date_dir()
        except FileExistsError:
            pass
        for thread in self.threads:
            thread.save_post_to_file(self.name, sub_filter)

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
        pass


class Post:
    def __init__(self, title, id, url, created):
        if title.__contains__(','):
            temp = title.split(',')
            title = ''
            for slice in temp:
                title += slice
        self.title = title
        self.id = id
        self.url = url
        self.created = dt.datetime.fromtimestamp(created)
        self.post_history = []

    def get_dict(self):
        # ret = {'title': self.title, 'score': [], 'id': self.id, 'url': self.url, 'comms_num': [],
        #       'created': self.created, 'time_saved': []}
        ret = {'score': [], 'comms_num': [], 'time_saved': []}
        for element in self.post_history:
            ret['score'].append(element.score)
            ret['comms_num'].append(element.comms_num)
            ret['time_saved'].append(element.time_saved)
        print(ret)
        return ret

    def get_panda(self):
        return pd.DataFrame(self.get_dict())

    def save_post_to_file(self, sub, sub_filter):
        if not os.getcwd().split(os.sep)[-1] == str(self.id):
            date = dt.datetime.now().date()
            change_directory(sub, str(self.id), date=str(date.month) + "." + str(date.day), filter=sub_filter)
        path = str(self.id + '.csv')
        try:
            os.remove(path)
        except FileNotFoundError:
            print("File " + path + " doesn't exist, creating it now.")
        except PermissionError:
            pass
        try:
            self.get_panda().to_csv(path, index=True)
        except PermissionError:
            print("Can't access file at " + path)

    def get_panda_from_csv(self, sub, sub_filter):
        date = dt.datetime.now().date()
        if not os.getcwd().split(os.sep)[-1] == self.id:
            change_directory(sub, str(self.id), date=str(date.month) + "." + str(date.day), filter=sub_filter)
        path = str(self.id + '.csv')
        ret = None
        try:
            return pd.read_csv(path)
        except UnicodeDecodeError:
            print("error")
            return

    def add_history_element(self, score, time_saved, num_comms):
        self.post_history.append(PostHistoryElement(score, time_saved, num_comms))

    def create_metadata_file(self):
        """TODO create metadata file. html or txt, probably txt due to readability"""
        pass

    def create_post_history_elements_from_panda(self, panda):
        print(panda)
        for line in range(len(panda['time_saved'])):
            self.post_history.append(PostHistoryElement(panda['score'][line], panda['time_saved'][line], panda['comms_num'][line]))
        print('all post history elements created')


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


def get_panda_from_csv(post_id, sub, sub_filter):
    date = dt.datetime.now().date()
    if not os.getcwd().split(os.sep)[-1] == post_id:
        change_directory(sub, str(post_id), date=str(date.month) + "." + str(date.day), filter=sub_filter)
    path = str(post_id + '.csv')
    ret = None
    try:
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
