from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test1"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(
        first_name="Lev",
        middle_name="Nikolayevich",
        last_name="Tolstoy",
        photo_path=r"C:\Users\agakax\Downloads\avatar.png",
        address=r"Yasnaya Polyana",
        birthday_day="9",
        birthday_month="September",
        birthday_year="1828",
        anniversary_day="20",
        anniversary_month="November",
        anniversary_year="1910")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_first_contact_with_photo_deletion(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(nickname="test2"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(
        first_name="Jan",
        last_name="Brzechwa",
        photo_delete=True,
        address=r"Kresy Wschodnie",
        birthday_day="15",
        birthday_month="August",
        birthday_year="1898",
        anniversary_day="2",
        anniversary_month="July",
        anniversary_year="1966",
    ))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
