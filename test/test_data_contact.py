import re
from random import randrange
from model.contact import Contact


def test_data_for_all_contacts_on_home_page(app, db, json_contact):
    if len(db.get_contact_list()) == 0:
        app.contact.create(json_contact)
    db_all_contacts = sorted(db.get_contact_list(), key=Contact.id_or_max)
    ui_all_contacts = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    assert len(db_all_contacts) == len(ui_all_contacts)
    for x,y in zip(db_all_contacts, ui_all_contacts):
        assert str(x.id) == y.id
        assert x.first_name == y.first_name
        assert x.last_name == y.last_name
        assert x.address == y.address
        assert merge_emails(x) == y.emails_all
        assert merge_phones_like_on_home_page(x).strip() == clear_number(y.telephones_all).strip()


def test_data_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(
            first_name="Asta",
            middle_name="Bakasta",
            last_name="Orphan",
            address=r"Clover Kingdom",
            telephone_home=r"+81 (246) 246-114",
            telephone_mobile=r"+81 (48) 8000-938",
            telephone_fax=r"+81 (906) 2377-225",
            email=r"asta@clover.jp",
            email3="blackbull@clover.jp",
            homepage=r"https://www.viz.com/black-clover",
            secondary_telephone_home=r"+81-9067282833",
        ))
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index=index)
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.emails_all == merge_emails(
        contact_from_edit_page)
    assert clear_number(contact_from_home_page.telephones_all).strip() == merge_phones_like_on_home_page(
        contact_from_edit_page).strip()


def test_data_on_details_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(
            first_name="Yuno",
            middle_name="Sylph",
            last_name="Orphan",
            address=r"Clover Kingdom",
            telephone_home=r"+81 (246) 246-114",
            telephone_mobile=r"+81 (48) 8000-938",
            telephone_fax=r"+81 (906) 2377-225",
            email=r"yuno@clover.jp",
            email3="goldendawn@clover.jp",
            homepage=r"https://www.viz.com/black-clover",
            secondary_telephone_home=r"+81-9067282833",
        ))
    index = randrange(app.contact.count())
    contact_from_details_page = app.contact.get_contact_info_from_details_page(index=index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index=index)
    assert contact_from_details_page.title == merge_name_like_on_details_page(contact_from_edit_page)
    assert contact_from_details_page.telephone_home == contact_from_edit_page.telephone_home
    assert contact_from_details_page.telephone_mobile == contact_from_edit_page.telephone_mobile
    assert contact_from_details_page.telephone_work == contact_from_edit_page.telephone_work
    assert contact_from_details_page.telephone_fax == contact_from_edit_page.telephone_fax
    assert contact_from_details_page.secondary_telephone_home == contact_from_edit_page.secondary_telephone_home
    assert "\n".join(contact_from_details_page.emails_all) == merge_emails(
        contact_from_edit_page)
    assert contact_from_details_page.homepage == contact_from_edit_page.homepage


def clear_number(s):
    # returns only digits separated by new lines
    return re.sub("[^0-9\n]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_number(x),
                                filter(lambda x: x is not None,
                                       [contact.telephone_home, contact.telephone_mobile, contact.telephone_work,
                                        contact.secondary_telephone_home]))))


def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "" and x is not None,
                            map(lambda x: x.strip(), [contact.email, contact.email2, contact.email3])))


def merge_name_like_on_details_page(contact):
    return " ".join(
        filter(lambda x: x != "" and x is not None, [contact.first_name, contact.middle_name, contact.last_name]))
