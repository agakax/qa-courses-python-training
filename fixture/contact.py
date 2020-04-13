from selenium.webdriver.support.select import Select


class ContactHelper:

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

    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form with all possible fields
        self.fill_form_element_by_its_name(field="firstname", value=contact.first_name)
        self.fill_form_element_by_its_name(field="middlename", value=contact.middle_name)
        self.fill_form_element_by_its_name(field="lastname", value=contact.last_name)
        self.fill_form_element_by_its_name(field="nickname", value=contact.nickname)
        self.fill_form_photo(field="photo", value=contact.photo_path, delete=False)
        self.fill_form_element_by_its_name(field="title", value=contact.title)
        self.fill_form_element_by_its_name(field="company", value=contact.company)
        self.fill_form_element_by_its_name(field="address", value=contact.address)
        self.fill_form_element_by_its_name(field="home", value=contact.telephone_home)
        self.fill_form_element_by_its_name(field="mobile", value=contact.telephone_mobile)
        self.fill_form_element_by_its_name(field="work", value=contact.telephone_work)
        self.fill_form_element_by_its_name(field="fax", value=contact.telephone_fax)
        self.fill_form_element_by_its_name(field="email", value=contact.email)
        self.fill_form_element_by_its_name(field="email2", value=contact.email2)
        self.fill_form_element_by_its_name(field="email3", value=contact.email3)
        self.fill_form_element_by_its_name(field="homepage", value=contact.homepage)
        self.fill_form_element_by_dropdown_list(field="bday", value=contact.birthday_day)
        self.fill_form_element_by_dropdown_list(field="bmonth", value=contact.birthday_month)
        self.fill_form_element_by_its_name(field="byear", value=contact.birthday_year)
        self.fill_form_element_by_dropdown_list(field="aday", value=contact.anniversary_day)
        self.fill_form_element_by_dropdown_list(field="amonth", value=contact.anniversary_month)
        self.fill_form_element_by_its_name(field="ayear", value=contact.anniversary_year)
        self.fill_form_element_by_dropdown_list(field="new_group", value=contact.group)
        self.fill_form_element_by_its_name(field="address2", value=contact.secondary_address)
        self.fill_form_element_by_its_name(field="phone2", value=contact.secondary_telephone_home)
        self.fill_form_element_by_its_name(field="notes", value=contact.secondary_notes)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact and start editing it
        wd.find_element_by_xpath("(//img[@title='Edit'])").click()
        # edit contact form
        self.fill_form_element_by_its_name(field="firstname", value=contact.first_name)
        self.fill_form_element_by_its_name(field="middlename", value=contact.middle_name)
        self.fill_form_element_by_its_name(field="lastname", value=contact.last_name)
        self.fill_form_element_by_its_name(field="nickname", value=contact.nickname)
        self.fill_form_photo(field="photo", value=contact.photo_path, delete=contact.photo_delete)
        self.fill_form_element_by_its_name(field="title", value=contact.title)
        self.fill_form_element_by_its_name(field="company", value=contact.company)
        self.fill_form_element_by_its_name(field="address", value=contact.address)
        self.fill_form_element_by_its_name(field="home", value=contact.telephone_home)
        self.fill_form_element_by_its_name(field="mobile", value=contact.telephone_mobile)
        self.fill_form_element_by_its_name(field="work", value=contact.telephone_work)
        self.fill_form_element_by_its_name(field="fax", value=contact.telephone_fax)
        self.fill_form_element_by_its_name(field="email", value=contact.email)
        self.fill_form_element_by_its_name(field="email2", value=contact.email2)
        self.fill_form_element_by_its_name(field="email3", value=contact.email3)
        self.fill_form_element_by_its_name(field="homepage", value=contact.homepage)
        self.fill_form_element_by_dropdown_list(field="bday", value=contact.birthday_day)
        self.fill_form_element_by_dropdown_list(field="bmonth", value=contact.birthday_month)
        self.fill_form_element_by_its_name(field="byear", value=contact.birthday_year)
        self.fill_form_element_by_dropdown_list(field="aday", value=contact.anniversary_day)
        self.fill_form_element_by_dropdown_list(field="amonth", value=contact.anniversary_month)
        self.fill_form_element_by_its_name(field="ayear", value=contact.anniversary_year)
        self.fill_form_element_by_its_name(field="address2", value=contact.secondary_address)
        self.fill_form_element_by_its_name(field="phone2", value=contact.secondary_telephone_home)
        self.fill_form_element_by_its_name(field="notes", value=contact.secondary_notes)
        # submit contact modification
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_home_page()

    def modify_selected_fields_in_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact and start editing it
        wd.find_element_by_xpath("(//img[@title='Edit'])").click()
        # edit contact form
        if contact.first_name != "":
            self.fill_form_element_by_its_name(field="firstname", value=contact.first_name)
        if contact.middle_name != "":
            self.fill_form_element_by_its_name(field="middlename", value=contact.middle_name)
        if contact.last_name != "":
            self.fill_form_element_by_its_name(field="lastname", value=contact.last_name)
        if contact.nickname != "":
            self.fill_form_element_by_its_name(field="nickname", value=contact.nickname)
        if contact.photo_path != "" or contact.photo_delete:
            self.fill_form_photo(field="photo", value=contact.photo_path, delete=contact.photo_delete)
        if contact.title != "":
            self.fill_form_element_by_its_name(field="title", value=contact.title)
        if contact.company != "":
            self.fill_form_element_by_its_name(field="company", value=contact.company)
        if contact.address != "":
            self.fill_form_element_by_its_name(field="address", value=contact.address)
        if contact.telephone_home != "":
            self.fill_form_element_by_its_name(field="home", value=contact.telephone_home)
        if contact.telephone_mobile != "":
            self.fill_form_element_by_its_name(field="mobile", value=contact.telephone_mobile)
        if contact.telephone_work != "":
            self.fill_form_element_by_its_name(field="work", value=contact.telephone_work)
        if contact.telephone_fax != "":
            self.fill_form_element_by_its_name(field="fax", value=contact.telephone_fax)
        if contact.email != "":
            self.fill_form_element_by_its_name(field="email", value=contact.email)
        if contact.email2 != "":
            self.fill_form_element_by_its_name(field="email2", value=contact.email2)
        if contact.email3 != "":
            self.fill_form_element_by_its_name(field="email3", value=contact.email3)
        if contact.homepage != "":
            self.fill_form_element_by_its_name(field="homepage", value=contact.homepage)
        if contact.birthday_day != "":
            self.fill_form_element_by_dropdown_list(field="bday", value=contact.birthday_day)
        if contact.birthday_month != "":
            self.fill_form_element_by_dropdown_list(field="bmonth", value=contact.birthday_month)
        if contact.birthday_year != "":
            self.fill_form_element_by_its_name(field="byear", value=contact.birthday_year)
        if contact.anniversary_day != "":
            self.fill_form_element_by_dropdown_list(field="aday", value=contact.anniversary_day)
        if contact.anniversary_month != "":
            self.fill_form_element_by_dropdown_list(field="amonth", value=contact.anniversary_month)
        if contact.anniversary_year != "":
            self.fill_form_element_by_its_name(field="ayear", value=contact.anniversary_year)
        if contact.address != "":
            self.fill_form_element_by_its_name(field="address2", value=contact.secondary_address)
        if contact.secondary_telephone_home != "":
            self.fill_form_element_by_its_name(field="phone2", value=contact.secondary_telephone_home)
        if contact.secondary_notes != "":
            self.fill_form_element_by_its_name(field="notes", value=contact.secondary_notes)
        # submit contact modification
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
