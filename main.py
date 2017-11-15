# -*- coding: UTF-8 -*-

from db import MysqlConnector
import pdb

MysqlConnector.set_config('config.toml')
config = MysqlConnector.get_config()  # get configuration

# Connect to mysql，若需切换数据库，只要替换“localhost”为所需数据库即可
conn, cur = MysqlConnector.conn_mysql(config["localhost"]["host"], config["localhost"]["port"], 
                                      config["localhost"]["user"], config["localhost"]["password"], 
                                      config["localhost"]["database"], config["localhost"]["charset"])
