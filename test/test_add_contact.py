# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact_with_some_fields(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(
        first_name="Anna",
        last_name="German",
        birthday_year="1936",
        birthday_month="February",
        birthday_day="14"))
    app.session.logout()


def test_add_contact_empty(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact())
    app.session.logout()


def test_add_contact_with_all_fields(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(
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
        secondary_notes="nothing worth mentioning"
    ))
    app.session.logout()
