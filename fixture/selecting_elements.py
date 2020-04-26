from selenium.common.exceptions import NoSuchElementException
import time


class SelectingElementsHelper:

    def __init__(self, app):
        self.app = app

    def element_by_name(self, name):
        wd = self.app.wd
        self.wait_for_element(element="name", value=name)
        wd.find_element_by_name(name).click()

    def element_by_link_text(self, link_text):
        wd = self.app.wd
        self.wait_for_element(element="link_text", value=link_text)
        wd.find_element_by_link_text(link_text).click()

    def element_by_xpath(self, field, field_type, field_value, field_occurrence=None):
        wd = self.app.wd
        xpath = "(//" + field + "[@" + field_type + "='" + field_value + "'])"
        if field_occurrence is not None:
            xpath = xpath + field_occurrence
        self.wait_for_element(element="xpath", value=xpath)
        wd.find_element_by_xpath(xpath).click()

    def wait_for_element(self, element, value):
        # wait up to 30 sec for element presence
        for i in range(1, 300):
            if self.check_exists(element=element, value=value):
                return
            else:
                time.sleep(0.01)
        print("Element find_element_by_%s(%s) not found" % (str(element), str(value)))

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
