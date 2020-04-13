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
        # waiting for application to logout
        wd.find_element_by_name("user")
