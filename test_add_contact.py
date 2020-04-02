# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("first name")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("middle name")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("last name")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("nickname")
        wd.find_element_by_name("photo").send_keys(r"C:\Users\agakax\Downloads\avatar.png")
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("title")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("company")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("address")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("home telephone")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("mobile telephone")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("work telephone")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("fax telephone")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("e-mail1")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("e-mail2")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("e-mail3")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("homepage")
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("January")
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1990")
        Select(wd.find_element_by_name("aday")).select_by_visible_text("1")
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("April")
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2020")
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("secondary address")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("secondary home")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("secondary notes")
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("home page").click()
        wd.find_element_by_link_text("Logout").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
