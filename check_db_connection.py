import pymysql.cursors
import os.path
import json
from fixture.db import DbFixture

config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "target.json")
with open(config_file) as f:
    target = json.load(f)

db = DbFixture(host=target["db"]["host"], name=target["db"]["name"], user=target["db"]["user"],
               password=target["db"]["password"])

try:
    groups = db.get_group_list()
    for group in groups:
        print(group)
    print(len(groups))
finally:
    db.destroy()
