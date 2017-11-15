# -*- coding: UTF-8 -*-

import os
import pdb
import json
import logging
import MySQLdb

class MysqlConnector(object):
    """Get Configuration and Connect to Mysql! """

    config = None

    conn = None

    cur = None

    @staticmethod
    def set_config(file_name="config"):
        with open(file_name, "r") as f:
            MysqlConnector.config = json.load(f)
    
    @staticmethod
    def get_config():
        if MysqlConnector.config:
            return MysqlConnector.config

    @staticmethod
    def conn_mysql(host, user, password, database = None, port = None):
        """Connetct to mysql"""
        try:
            # pdb.set_trace()
            MysqlConnector.conn = MySQLdb.connect(host=host, user=user, passwd=password)
            MysqlConnector.cur = MysqlConnector.conn.cursor()

        except Exception as e:
            logging.info('connect to mysql error')
            logging.error(e)

    @staticmethod
    def execute_sql(path):
        os.chdir(path)
        for each in os.listdir("."):
            sql = ""  #拼接sql语句
            if "sql" in each:
                with open(each, "r") as f:
                    full_sql = f.read()
                    sql_commands = full_sql.replace('\n', '').split(';')[:-1]
                    if len(sql_commands) > 0:
                        _ = [MysqlConnector.cur.execute(i) for i in sql_commands]
                MysqlConnector.conn.commit()
                        