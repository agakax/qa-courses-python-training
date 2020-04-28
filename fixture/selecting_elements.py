from selenium.common.exceptions import NoSuchElementException
import time


class SelectingElementsHelper:

    def __init__(self, app):
        self.app = app

    def element_by_name(self, name):
        wd = self.app.wd
        wd.find_element_by_name(name).click()

    def element_by_link_text(self, link_text):
        wd = self.app.wd
        wd.find_element_by_link_text(link_text).click()

    def element_by_xpath(self, field, field_type, field_value, field_occurrence=None):
        wd = self.app.wd
        xpath = "(//" + field + "[@" + field_type + "='" + field_value + "'])"
        if field_occurrence is not None:
            xpath = xpath + field_occurrence
        wd.find_element_by_xpath(xpath).click()
