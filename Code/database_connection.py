import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    database='reddit_analysis'
)
columns_dict = {'post_columns': [], 'subreddit_columns': [],
                'posthistoryelement_columns': []}

mycursor = mydb.cursor(buffered=True)


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
    mycursor.execute(query, data)
    mydb.commit()


def write_subreddit_to_db(subreddit_name):
    query = "INSERT INTO `subreddit` (`name`) VALUES (%s)"
    mycursor.execute(query, (subreddit_name, ))
    mydb.commit()


def write_posthistoryelement_to_db(posthistoryelement):
    query = "INSERT INTO `posthistoryelement` (`date_saved`, `score`, `num_comms`, `id_post`) " \
            "VALUES (%s, %s, %s, %s);"
    data = (posthistoryelement['saved'], posthistoryelement['score'], posthistoryelement['num_comments'], posthistoryelement['id_post'])
    mycursor.execute(query, data)
    mydb.commit()


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


def get_posthistoryelements(id_post):
    query = "Select * FROM posthistoryelement WHERE id_post = %s"
    mycursor.execute(query, (id_post[0], ))
    ret = {'date_saved': [], 'score': [], 'num_comms': []}
    for x in mycursor:
        ret['date_saved'].append(x[1])
        ret['score'].append(x[3])
        ret['num_comms'].append(x[4])
    return ret


def get_id_of_subreddit(subreddit_name):
    query = "SELECT id FROM subreddit WHERE name = '%s'" % subreddit_name
    mycursor.execute(query)
    for x in mycursor:
        return x
    return (1, )


create_panda('post')
columns_dict['post_columns'] = get_column_names('post')
columns_dict['posthistoryelement_columns'] = get_column_names('posthistoryelement')
columns_dict['subreddit_columns'] = get_column_names('subreddit')
