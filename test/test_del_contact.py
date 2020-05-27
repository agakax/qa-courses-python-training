import random
from model.contact import Contact


def test_delete_first_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == len(db.get_contact_list())
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted((map(lambda x: clean(x), new_contacts)), key=Contact.id_or_max) == \
               sorted((map(lambda x: clean(x), app.contact.get_contact_list())), key=Contact.id_or_max)


def clean(contact):
    return Contact(id_contact=str(contact.id), first_name=contact.first_name.strip(),
                   last_name=contact.last_name.strip(), address=contact.address.strip())
