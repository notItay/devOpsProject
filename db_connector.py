from datetime import datetime

import pymysql


class DbConnector(object):
    SCHEMA = 'localdb'
    TABLE = 'users'

    def __init__(self, host='127.0.0.1', port=3306, user='root', passwd='root', db='LocalDb'):
        self.connection = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
        self.connection.autocommit(True)

    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            print(query)
            cursor.execute(query)
        except pymysql.err.IntegrityError as e:
            raise e
        finally:
            cursor.close()

    def get_user_name(self, user_id):
        query = "SELECT user_name From {}.{} WHERE (user_id = {});".format(self.SCHEMA,
                                                                           self.TABLE,
                                                                           user_id)
        cursor = self.connection.cursor()
        try:
            print(query)
            cursor.execute(query)
            for row in cursor:
                return row[0]
        except pymysql.err.IntegrityError as e:
            raise e
        finally:
            cursor.close()

    def insert_user(self, user_id, user_name):
        query = "INSERT into {}.{} (user_id, user_name, creation_date) VALUES ({}, '{}', '{}');".format(self.SCHEMA,
                                                                                                        self.TABLE,
                                                                                                        user_id,
                                                                                                        user_name,
                                                                                                        str(datetime.now()))
        self.execute_query(query)

    def update_user_name(self, user_id, user_name):
        query = "UPDATE {}.{} SET user_name = '{}' WHERE (user_id = {});".format(self.SCHEMA,
                                                                                 self.TABLE,
                                                                                 user_name,
                                                                                 user_id)
        self.execute_query(query)

    def delete_user(self, user_id):
        query = "DELETE FROM {}.{} WHERE (user_id = {});".format(self.SCHEMA,
                                                                 self.TABLE,
                                                                 user_id)
        self.execute_query(query)

    def close_connection(self):
        self.connection.close()


