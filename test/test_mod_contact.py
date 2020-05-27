import random
from model.contact import Contact


def test_modify_contact(app, db, json_contact, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="test1"))
    old_contacts = db.get_contact_list()
    contact_to_modify = random.choice(old_contacts)
    contact = json_contact
    contact.id = contact_to_modify.id
    app.contact.modify_contact_by_id(contact=contact)
    assert len(old_contacts) == len(db.get_contact_list())
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact_to_modify)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted((map(lambda x: clean(x), new_contacts)), key=Contact.id_or_max) == \
               sorted((map(lambda x: clean(x), app.contact.get_contact_list())), key=Contact.id_or_max)


def clean(contact):
    return Contact(id_contact=str(contact.id), first_name=contact.first_name.strip(),
                   last_name=contact.last_name.strip(), address=contact.address.strip())
