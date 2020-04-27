# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact_with_some_fields(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(
        first_name="Anna",
        last_name="German",
        birthday_year="1936",
        birthday_month="February",
        birthday_day="14")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_contact_empty(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact())
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_contact_with_all_fields(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(
        first_name="Andrzej",
        middle_name="Sebastian",
        last_name="Duda",
        nickname="Adrian",
        photo_path=r"C:\Users\agakax\Downloads\avatar.png",
        title="President",
        company=r"PiS",
        address=r"Krakowskie Przedmieście 48/50, 00-071 Warszawa",
        telephone_home=r"+48 22 695-29-00",
        telephone_mobile=r"+48 22 694-16-00",
        telephone_work=r"+48 22 694-14-26",
        telephone_fax=r"+48 22 695-22-38",
        email=r"listy@prezydent.pl",
        email2=r"witryna.obywatelska@prezydent.pl",
        email3="rkubas@nw.senat.gov.pl",
        homepage=r"https://www.prezydent.pl/",
        birthday_day="16",
        birthday_month="May",
        birthday_year="1972",
        anniversary_day="6",
        anniversary_month="August",
        anniversary_year="2015",
        group="[none]",
        secondary_address=r"Wiejska 4/6/8, 00-902 Warszawa",
        secondary_telephone_home=r"+48 22 694-25-00",
        secondary_notes="nothing worth mentioning"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
