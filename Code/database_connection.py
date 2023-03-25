import mysql.connector
import pandas as pd
import datetime as dt
from Code.Post import Post
from Code.config import db

mydb = mysql.connector.connect(
    host=db['host'],
    user=db['user'],
    password=db['password'],
    database=db['database']
)
columns_dict = {'post_columns': [], 'subreddit_columns': [],
                'posthistoryelement_columns': []}

mycursor = mydb.cursor(buffered=True)


def cursor_to_dict(result_cursor):
    head = []
    ret = []
    for col in result_cursor.description:
        head.append(col[0])
    for row in result_cursor:
        this_head = {}
        for col in range(len(row)):
            this_head[head[col]] = row[col]
        ret.append(this_head)
    return ret


def get_column_names(table):
    ret = []
    mycursor.execute('SHOW columns FROM ' + table)
    for column in mycursor:
        ret.append(column[0])
    return ret


def create_dict(columns, table):
    ret = {}
    for column in columns:
        ret[column] = []
        mycursor.execute('Select ' + column + ' From ' + table)
        for data in mycursor:
            ret[column].append(data[0])
    return ret


def create_panda(table):
    dictionary = create_dict(columns_dict[table + '_columns'], table)
    dataframe = pd.DataFrame(dictionary)
    return dataframe


def get_dict_of_columns(table_name):
    ret = {}
    for col in columns_dict[table_name]:
        ret[col] = []
    return ret


def get_panda_of_posthistoryelements(post_id):
    query = 'SELECT * FROM posthistoryelement WHERE id_post = %s' % post_id
    mycursor.execute(query)
    tmp = get_dict_of_columns('posthistoryelement')
    for row in mycursor:
        pass


def write_post_to_db(post):
    query = "INSERT INTO `post` (`id_post`, `url`, `date_posted`, `id_subreddit`, `title`) " \
            "VALUES (%s, %s, %s, %s, %s)"
    data = (post['id_post'], post['url'], post['created'], post['id_subreddit'], post['title'])
    try:
        mycursor.execute(query, data)
        mydb.commit()
    except Exception:
        print('an error occured while writing posts to database with query' + query + " and data " + str(data))


def write_subreddit_to_db(subreddit_name):
    query = "INSERT INTO `subreddit` (`name`) VALUES (%s)"
    mycursor.execute(query, (subreddit_name,))
    mydb.commit()


def write_posthistoryelement_to_db(posthistoryelements):
    query = "INSERT INTO `posthistoryelement` (`date_saved`, `score`, `num_comms`) VALUES"
    first = True
    for element in posthistoryelements:
        if not first:
            query += ","
        first = False
        element = element.get_dict()
        query += "('" + str(element['saved']) + "', " + str(element['score']) + ", " + str(element['num_comments']) + ")"
    query += ";"
    mycursor.execute(query)
    mydb.commit()


def write_graph(id_post, graph):
    query = "UPDATE `post` SET `graph`='%s' WHERE `id_post`='%s'"
    graph = ''.join(str(graph).split("'"))
    data = (graph, id_post)
    try:
        mycursor.execute(query, data)
        mydb.commit()
    except mysql.connector.Error as error:
        mydb.rollback()
        print("Failed inserting BLOB data into MySQL table {}".format(error))


def post_in_db(post_id):
    query = "SELECT id FROM post WHERE id_post = '%s'" % post_id
    try:
        mycursor.execute(query)
    except mysql.connector.ProgrammingError:
        print('SQL Programming Error at id ' + post_id)
    else:
        return cursor_has_elements()


def subreddit_in_db(subreddit_name):
    query = "Select id FROM subreddit WHERE name = '%s'" % subreddit_name
    mycursor.execute(query)
    return cursor_has_elements()


def cursor_has_elements():
    for x in mycursor:
        return True
    return False

def get_posts_younger_than(amount_hours):
    query = "SELECT * FROM post WHERE DATE(date_posted) < DATE_SUB(CURDATE(), INTERVAL %s HOUR)" % amount_hours
    mycursor.execute(query)
    ret = []
    for x in mycursor:
        ret.append(x)
    return ret


def get_todays_posts():
    query = "Select id_post From post Where DAY(`date_posted`)=%s" % dt.datetime.now().strftime('%d')
    data = (dt.datetime.now().strftime('%d'), )
    mycursor.execute(query)
    ret = []
    for x in mycursor:
        ret.append(x[0])
    return ret


def get_posts_by_date(date):
    query = "select * from post left join posthistoryelement p on post.id_post = p.id_post where post.date_posted <= '2019-11-30' or post.date_posted >= '2019-11-30';"
    mycursor.execute(query)
    posts = {}
    post_dict = cursor_to_dict(mycursor)
    for row in post_dict:
        if row['id_post'] not in posts:
            post = Post(row['title'], row['id_post'], row['url'], row['date_posted'], row['id_subreddit'])
            posts[row['id_post']] = post
        else:
            post = posts[row['id_post']]
        post.add_history_element(row['score'], row['date_saved'], row['num_comms'])
    return posts


def get_posthistoryelements(id_post):
    query = "Select * FROM posthistoryelement WHERE id_post = '%s'" % id_post
    mycursor.execute(query)
    ret = {'date_saved': [], 'score': [], 'num_comms': []}
    for x in mycursor:
        ret['date_saved'].append(x[1])
        ret['score'].append(x[3])
        ret['num_comms'].append(x[4])
    return ret


def get_post(id_post):
    query = "Select * FROM post WHERE id_post = %s"
    mycursor.execute(query, (id_post,))
    for x in mycursor:
        post = {'title': x[5],
                'url': x[2],
                'id_post': x[1],
                'created': x[3],
                'id_subreddit': x[4]
                }
        return post


def get_id_of_subreddit(subreddit_name):
    query = "SELECT id FROM subreddit WHERE name = '%s'" % subreddit_name
    mycursor.execute(query)
    for x in mycursor:
        return x
    return (1,)


def get_name_of_subreddit(subreddit_id):
    query = "SELECT name FROM subreddit WHERE id = '%s'" % subreddit_id
    mycursor.execute(query)
    for x in mycursor:
        print(type(x[0]))
        return x[0]


create_panda('post')
columns_dict['post_columns'] = get_column_names('post')
columns_dict['posthistoryelement_columns'] = get_column_names('posthistoryelement')
columns_dict['subreddit_columns'] = get_column_names('subreddit')
