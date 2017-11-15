# -*- coding: UTF-8 -*-

from db import MysqlConnector
import pdb

MysqlConnector.set_config('config.toml')
config = MysqlConnector.get_config()  # get configuration

# Connect to mysql，若需切换数据库，只要替换“localhost”为所需数据库即可
for machine in config.keys():
    pdb.set_trace()
    MysqlConnector.conn_mysql(config[machine]["host"], config[machine]["user"], 
                          config[machine]["password"], config[machine]["database"], 
                          config[machine]["port"])
    MysqlConnector.execute_sql('./sql')