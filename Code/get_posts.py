import datetime as dt
import os

import pandas as pd

global posts, subreddits, reddit
posts = []
subreddits = []


def get_data(reddit_instance, subreddit_instance, subreddit_name, sub_filter):
    """New Posts"""
    print('Getting data for ' + subreddit_name)
    c = None

    for subredd in subreddits:
        c = create_subreddit(subredd, subreddit_name, sub_filter)

    '''safety measure'''
    if c is None:
        print('\tc is None, adding first sub now: ' + subreddit_name)
        c = MySubreddit(subreddit_name, sub_filter)
        subreddits.append(c)
    global reddit
    reddit = reddit_instance
    '''
    loop through submissions in subreddit instance
        if the post isn't in the list found in MySubreddit instance and the post isn't older than 6 hours, crete new Post instance
    add new data into new PostHistoryElement, add to list in Post
    '''
    arr_posts = get_ids_of_posts_in_subreddit(subreddit_name, '../Data/' + str(dt.datetime.now().month) + '.' +
                                              str(dt.datetime.now().day) + '/hot')
    print(c.get_posts_younger_than(arr_posts))
    arr_gotten_posts = []
    for submission in subreddit_instance:
        if submission.id not in c.get_posts_younger_than(arr_posts):
            if not c.check_if_post_is_in_list(post_id=submission.id):
                print('submission ' + submission.id + " is saved")
                a = Post(submission.title, submission.id, submission.url, submission.created)
                c.threads.append(a)
                a.create_post_history_elements_from_panda(get_panda_from_csv(submission.id, subreddit_name, sub_filter))
            else:
                print('\t\tsubmission already in list')
                a = c.get_post_by_id(submission.id)
            a.post_history.append(PostHistoryElement(submission.score, dt.datetime.now().strftime('%Y-%m-%d %H-%M-%S'), submission.num_comments))
            arr_gotten_posts.append(submission.id)

    for submission in c.get_posts_younger_than(arr_posts):
        try:
            if submission not in arr_gotten_posts:
                a = c.get_post_by_id(submission)
                c.threads.append(a)
                a.create_post_history_elements_from_panda(get_panda_from_csv(a.id, subreddit_name, sub_filter))
                tmp_sub = reddit.submission(id=submission)
                a.post_history.append(PostHistoryElement(tmp_sub.score, dt.datetime.now().strftime('%Y-%m-%d %H-%M-%S'), tmp_sub.num_comments))
        except AttributeError:
            print('An Error occured while getting data for %s' % submission)
    '''Save data to csv file'''
    c.save_posts_to_file(sub_filter)


def create_subreddit(subreddit_instance, name, sub_filter):
    """
    if this subreddit (MySubreddit instance) isn't in list 'subreddits': create new instance, put in list.
    else: get instance
    """
    if str(subreddit_instance) == name and subreddit_instance.filter == sub_filter:
        print('\tSubreddit ' + name + ' found in list.')
        c = subreddit_instance
        return c
    else:
        print('\tSubreddit ' + name + ' not found in list, creating it now')
        c = MySubreddit(name, sub_filter)
        subreddits.append(c)
        return c


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
            os.chdir('../../../../')
            go_in_directory(dir, arr)
        else:
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
            try:
                thread.save_post_to_file(self.name, sub_filter)
            except AttributeError:
                pass

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
        ret_arr = []
        for post_id in arr:
            change_directory(self.name, post_id, str(dt.datetime.now().month) + '.' + str(dt.datetime.now().day), self.filter)
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
        self.create_metadata_file()

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
        """create txt file with post info if it doesn't yet exist."""
        try:
            file = open(self.id + '.txt', 'r')
        except FileNotFoundError:
            print('File not found, creating it now')
            file = open(self.id + '.txt', 'w+')
            file.write(self.id + ';' + self.url + ';' + self.title + ';' + str(self.created))
            file.close()

    def create_post_history_elements_from_panda(self, panda):
        print(panda)
        try:
            for line in range(len(panda['time_saved'])):
                self.post_history.append(PostHistoryElement(panda['score'][line], panda['time_saved'][line], panda['comms_num'][line]))
        except TypeError:
            print('NoneType error')
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
    except FileNotFoundError:
        print('file %s.csv not found' % post_id)


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
