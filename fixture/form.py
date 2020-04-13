from selenium.webdriver.support.select import Select


class FillingFormHelper:

    def __init__(self, app):
        self.app = app

    def fill_form_element_by_its_name(self, field, value):
        wd = self.app.wd
        wd.find_element_by_name(field).click()
        wd.find_element_by_name(field).clear()
        wd.find_element_by_name(field).send_keys(value)

    def fill_form_element_by_dropdown_list(self, field, value):
        wd = self.app.wd
        Select(wd.find_element_by_name(field)).select_by_visible_text(value)

    def fill_form_photo(self, field, value, delete, delete_field="delete_photo"):
        wd = self.app.wd
        if value != "":
            wd.find_element_by_name(field).send_keys(value)
        if delete:
            wd.find_element_by_name(delete_field).click()
