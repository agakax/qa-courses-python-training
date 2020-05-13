from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.form import FillingFormHelper
from fixture.selecting_elements import SelectingElementsHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox(executable_path=r'C:\Windows\SysWOW64\geckodriver.exe')
        elif browser == "chrome":
            self.wd = webdriver.Chrome(executable_path=r'C:\Windows\SysWOW64\chromedriver.exe')
        elif browser == "ie":
            self.wd = webdriver.Ie(executable_path=r'C:\Windows\SysWOW64\IEDriverServer.exe')
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.form = FillingFormHelper(self)
        self.select = SelectingElementsHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/addressbook/") or
                wd.current_url.endswith("/index.php")):
            wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
