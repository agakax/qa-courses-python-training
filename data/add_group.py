from model.group import Group
import random
import string


constant = [Group(name="name1",
                  header="header1",
                  footer="footer1"),
            Group(name="name2",
                  header="header2",
                  footer="footer2"),
            Group(name="name3",
                  header="header3",
                  footer="footer3")]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Group()] + [
    Group(name=random_string(prefix="name", maxlen=10), header=random_string(prefix="header", maxlen=20),
          footer=random_string(prefix="footer", maxlen=15))
    for i in range(3)
]
