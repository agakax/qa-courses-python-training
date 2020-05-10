# -*- coding: utf-8 -*-
import re
from model.contact import Contact
import pytest
import random
import string


def random_value(maxlen):
    symbols = string.ascii_letters + string.digits + "./@:-+" + " " * 10
    word = re.sub(' +', ' ', "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]).strip())
    return random.choice([word, None])


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
    for i in range(5)
]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact_with_some_fields(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
