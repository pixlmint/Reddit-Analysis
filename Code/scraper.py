import datetime as dt
import Code.database_connection as db
from Code.Post import Post
from Code.PostHistoryElement import PostHistoryElement

global reddit
posts = []
subreddits = []
subreddit_posts = {}


def get_data(reddit_instance, subreddit_instance, subreddit_name, sub_filter):
    global reddit
    reddit = reddit_instance
    if subreddit_name not in subreddits:
        print('subreddit %s not in array' % subreddit_name)
        if not db.subreddit_in_db(subreddit_name):
            print('subreddit %s not in db' % subreddit_name)
            db.write_subreddit_to_db(subreddit_name)
        subreddits.append(subreddit_name)
        subreddit_posts[subreddit_name] = []
    try:
        all_post_ids = get_posts_to_be_kept_up_to_date(subreddit_instance, subreddit_name)
    except Exception:
        return None
    ids2 = [i if i.startswith('t3_') else f't3_{i}' for i in all_post_ids]
    elements = []
    for submission in reddit.info(ids2):
        for post in subreddit_posts[subreddit_name]:
            if submission.id is post.id_post:
                break
        else:
            create_new_post(submission, subreddit_name)
        for post in posts:
            if submission.id is post.id_post:
                elements.append(create_new_post_history_element(post, submission))
    db.write_posthistoryelement_to_db(elements)
    print('posts updated: ' + str(len(all_post_ids)))
    print(all_post_ids)


def get_posts_to_be_kept_up_to_date(subreddit_instance, subreddit_name):
    """:returns array with id's of posts that must be updated"""
    arr_post_ids = []
    for post in subreddit_posts[subreddit_name]:
        timediff = (dt.datetime.now() - post.created).seconds / 3600
        if timediff > 30:
            growth = post.check_growth()
            if growth <= 2:
                print("Post %s too old, removing it now" % post.id_post)
                posts.remove(post)
        else:
            if post.id_post not in arr_post_ids:
                arr_post_ids.append(post.id_post)

    for submission in subreddit_instance:
        for post in posts:
            if post.id_post is submission.id:
                break
        else:
            arr_post_ids.append(submission.id)
    return arr_post_ids


def create_new_post(submission, subreddit_name):
    post = Post(submission.title, submission.id, submission.url, submission.created,
                db.get_id_of_subreddit(submission.subreddit)[0])
    posts.append(post)
    subreddit_posts[subreddit_name].append(post)
    if not db.post_in_db(submission.id):
        db.write_post_to_db(post.get_dict())
    return post


def create_new_post_history_element(post, submission):
    element = PostHistoryElement(submission.score, dt.datetime.now(), submission.num_comments, post.id_post)
    post.post_history.append(element)
    return element


def load_post_from_db(id_post):
    for post in posts:
        if post.id_post is id_post:
            return post
    if db.post_in_db(id_post):
        post = db.get_post(id_post)
        post_obj = Post(post['title'], id_post, post['url'], post['created'], post['id_subreddit'])
        posts.append(post_obj)
        return post_obj


def load_post_history_element_from_db(id_post=None, post=None):
    post = post
    if id_post:
        post = load_post_from_db(id_post)
    elements = db.get_posthistoryelements(post.id_post)
    for i in range(len(elements['score'])):
        post.add_history_element(elements['score'][i], elements['date_saved'][i], elements['num_comms'][i])
    panda = post.get_panda()
    return panda
