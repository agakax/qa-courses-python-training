import random
from model.group import Group
from model.contact import Contact


def test_add_group_to_contact(app, orm):
    contacts = orm.get_all_contacts_not_in_groups()
    if contacts == 0:
        app.contact.create(Contact(first_name="adding groups"))
        contacts = orm.get_all_contacts_not_in_groups()
    contact = random.choice(contacts)
    groups = orm.get_group_list()
    if groups == 0:
        app.group.create(Group(name="for orm purpose"))
        groups = orm.get_group_list()
    group = random.choice(groups)
    old_data = orm.get_group_in_contact(group)
    app.contact.add_contact_to_group(contact_id=contact.id, group_id=group.id)
    new_data = orm.get_group_in_contact(group)
    assert len(old_data) + 1 == len(new_data)
    old_data.append(contact)
    assert sorted(old_data, key=Contact.id_or_max) == sorted(new_data, key=Contact.id_or_max)
