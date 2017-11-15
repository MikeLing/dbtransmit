conn_sql = Connect_mysql()
config = conn_sql.get_config()  # get configuration
# Connect to mysql，若需切换数据库，只要替换“dev”为所需数据库即可
conn, cur = conn_sql.conn_mysql(config["dev"]["host"], config["dev"]["port"], config["dev"]["user"],
                                config["dev"]["password"], config["dev"]["database"], config["dev"]["charset"])
