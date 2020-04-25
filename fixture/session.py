from selenium.common.exceptions import NoSuchElementException
import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        self.app.open_home_page()
        self.app.form.fill_form_element_by_its_name(field="user", value=username)
        self.app.form.fill_form_element_by_its_name(field="pass", value=password)
        self.app.select.element_by_xpath(field="input", field_type="value", field_value="Login")

    def logout(self):
        wd = self.app.wd
        self.app.select.element_by_link_text(link_text="Logout")

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username=username, password=password)

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        string = "(//div[@id='top']/form/b)[1]"
        self.wait_for_element(element="xpath", value=string)
        return wd.find_element_by_xpath(string).text == "(" + username + ")"

    def wait_for_element(self, element, value):
        # wait up to 30 sec for element presence
        for i in range(1, 300):
            if self.check_exists(element=element, value=value):
                return
            else:
                time.sleep(0.01)
        print("Element %s not found" % str(element))

    def check_exists(self, element, value):
        wd = self.app.wd
        try:
            if element == "xpath":
                wd.find_element_by_xpath(value)
            if element == "name":
                wd.find_element_by_name(value)
            if element == "css_selector":
                wd.find_element_by_css_selector(value)
            if element == "link_text":
                wd.find_element_by_link_text(value)
        except NoSuchElementException:
            return False
        return True
