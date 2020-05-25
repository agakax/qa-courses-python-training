from model.contact import Contact
import re
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_value(maxlen):
    symbols = string.ascii_letters + string.digits + "./@:-+" + " " * 10
    word = re.sub(' +', ' ', "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]).strip())
    return random.choice([word, word, word, None])


test_data = [Contact()] + [
    Contact(first_name=random_value(maxlen=10),
            middle_name=random_value(maxlen=5),
            last_name=random_value(maxlen=20),
            nickname=random_value(maxlen=15),
            title=random_value(maxlen=8),
            company=random_value(maxlen=10),
            address=random_value(maxlen=30),
            telephone_home=random_value(maxlen=10),
            telephone_mobile=random_value(maxlen=10),
            telephone_work=random_value(maxlen=10),
            telephone_fax=random_value(maxlen=10),
            secondary_address=random_value(maxlen=10),
            secondary_telephone_home=random_value(maxlen=10),
            secondary_notes=random_value(maxlen=20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))
