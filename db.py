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
        with open(file_name,"r",encoding="utf-8") as f:
            MysqlConnector.config = json.load(f)
    
    @staticmethod
    def get_config():
        if MysqlConnector.config:
            return MysqlConnector.config

    @staticmethod
    def conn_mysql(host, port, user, password, database, charset="utf-8"):
        """Connetct to mysql"""
        try:
            MysqlConnector.conn = MySQLdb.connect(host=host, port=port, user=user, password=password, database=database, charset=charset)
            MysqlConnector.cur = MysqlConnector.conn.cursor()

        except Exception as e:
            logging.info('connect to mysql error')
            logging.error(e)

    @staticmethod
    def execute_sql(conn, cur, path):
        os.chdir(path)
        for each in os.listdir("."):
            count = 0 #读取数据
            sql = ""  #拼接sql语句
            if "wormhole.sql" in each:
                with open(each, "r", encoding="utf-8") as f:
                    for each_line in f.readlines():
                        #过滤数据
                        if not each_line or each_line == "\n":
                            continue
                        
                        #读取2000行数据，拼接sql
                        elif count < 2000:
                            sql += each_line
                            count += 1

                        #读取到2000行，提交，同时初始化sql，count值
                        else:
                            MysqlConnector.cur.execute(sql)
                            MysqlConnector.conn.commit()
                            sql = each_line
                            count = 1
                        #当读取文件完毕，不到2000行时，也需要对拼接的sql执行，提交
                        if sql:
                            MysqlConnector.cur.execute(sql)
                            MysqlConnector.conn.commit()