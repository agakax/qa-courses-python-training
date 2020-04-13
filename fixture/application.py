from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.form import FillingFormHelper
from fixture.selecting_elements import SelectingElementsHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.form = FillingFormHelper(self)
        self.select = SelectingElementsHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/addressbook/") or
                wd.current_url.endswith("/index.php") or
                wd.current_url.startswith("?", 29) or
                wd.current_url.startswith("index.php?", 29)):
            wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
