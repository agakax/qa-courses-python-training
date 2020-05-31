import random
from model.group import Group
from model.contact import Contact


def test_del_group_from_contact(app, orm):
    contacts_in_groups = orm.get_all_contacts_in_groups()
    contacts = orm.get_contact_list()
    groups = orm.get_group_list()
    if len(contacts_in_groups) == 0:
        if len(contacts) == 0:
            app.contact.create(Contact(first_name="for orm"))
            contacts = orm.get_contact_list()
        if len(groups) == 0:
            app.group.create(Group(name="for orm purpose"))
            groups = orm.get_group_list()
        contact = random.choice(contacts)
        group = random.choice(groups)
        app.contact.add_contact_to_group(contact_id=contact.id, group_id=group.id)
        contacts_in_groups = orm.get_all_contacts_in_groups()
    contact = random.choice(contacts_in_groups)
    group = orm.get_group_in_contact(contact)[0]
    old_data = orm.get_contacts_in_group(group)
    app.contact.remove_contact_from_group(contact_id=contact.id, group_id=group.id)
    new_data = orm.get_contacts_in_group(group)
    assert len(old_data) - 1 == len(new_data)
    old_data.remove(contact)
    assert sorted(old_data, key=Contact.id_or_max) == sorted(new_data, key=Contact.id_or_max)
