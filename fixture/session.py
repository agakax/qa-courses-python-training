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
        string = "Logout"
        return len(wd.find_elements_by_link_text(string)) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        string = "(//div[@id='top']/form/b)[1]"
        return wd.find_element_by_xpath(string).text[1:-1] == username
