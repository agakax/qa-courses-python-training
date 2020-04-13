class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        self.app.form.fill_form_element_by_its_name(field="user", value=username)
        self.app.form.fill_form_element_by_its_name(field="pass", value=password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        # waiting for application to logout
        wd.find_element_by_name("user")
