import pymysql.cursors
import os.path
import json
from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact

config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "target.json")
with open(config_file) as f:
    target = json.load(f)

db = ORMFixture(host=target["db"]["host"], name=target["db"]["name"], user=target["db"]["user"],
                password=target["db"]["password"])

try:
    l = db.get_all_contacts_in_groups()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass # db.destroy()
