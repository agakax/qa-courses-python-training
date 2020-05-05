import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index=0)
    assert clear(contact_from_home_page.telephone_home) == clear(contact_from_edit_page.telephone_home)
    assert clear(contact_from_home_page.telephone_mobile) == clear(contact_from_edit_page.telephone_mobile)
    assert clear(contact_from_home_page.telephone_work) == clear(contact_from_edit_page.telephone_work)
    assert clear(contact_from_home_page.secondary_telephone_home) == clear(
        contact_from_edit_page.secondary_telephone_home)


def test_phones_on_details_page(app):
    contact_from_details_page = app.contact.get_contact_info_from_details_page(index=0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index=0)
    assert contact_from_details_page.telephone_home == contact_from_edit_page.telephone_home
    assert contact_from_details_page.telephone_mobile == contact_from_edit_page.telephone_mobile
    assert contact_from_details_page.telephone_work == contact_from_edit_page.telephone_work
    assert contact_from_details_page.secondary_telephone_home == contact_from_edit_page.secondary_telephone_home


def clear(s):
    # returns only digits
    return re.sub("[^0-9]", "", s)
