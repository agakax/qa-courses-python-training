import pymysql.cursors
import os.path
import json

config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "target.json")
with open(config_file) as f:
    target = json.load(f)

connection = pymysql.connect(host=target["db_host"], database=target["db_name"], user=target["db_username"],
                             password=target["db_password"])

try:
    cursor = connection.cursor()
    cursor.execute(
        "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = '%s' AND TABLE_NAME = '%s'" % (
            target["db_name"], "group_list"))
    column_names = []
    for row in cursor.fetchall():
        column_names.append(row[0])
    print(tuple(column_names))
    cursor.execute("SELECT * FROM group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()
