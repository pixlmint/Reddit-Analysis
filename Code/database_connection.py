import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd=""
)

post_columns = ['id', 'url', 'date_posted', 'id_subreddit', 'title']
subreddit_columns = ['id', 'name']
posthistoryelement_columns = ['id', 'date_save', 'score', 'num_comms', 'id_post']
columns_dict = {'post_columns': post_columns, 'subreddit_columns': subreddit_columns, 'posthistoryelement_columns': posthistoryelement_columns}


def get_panda_from_sql(query):
    pass


mycursor = mydb.cursor()


def get_column_names(table):
    """deprecated"""
    ret = []
    mycursor.execute('SELECT * FROM reddit_analysis.INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N\'post\'')
    for column in mycursor:
        ret.append(column)
    return ret


def create_dict(columns, table):
    ret = {}
    for column in columns:
        ret[column] = []
        mycursor.execute('Select ' + column + ' From reddit_analysis.' + table)
        for data in mycursor:
            ret[column].append(data[0])
    return ret


def get_panda(table):
    dictionary = create_dict(columns_dict[table + '_columns'], table)
    dataframe = pd.DataFrame(dictionary)
    print(dataframe)
    return dataframe


def get_panda_of_posthistoryelements(post_id):
    pass


get_panda('post')
