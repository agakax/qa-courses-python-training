from selenium.webdriver.support.select import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form with all possible fields
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        if contact.photo_path != "":
            wd.find_element_by_name("photo").send_keys(contact.photo_path)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.telephone_home)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.telephone_mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.telephone_work)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.telephone_fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birthday_day)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birthday_month)
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birthday_year)
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.anniversary_day)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary_month)
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        Select(wd.find_element_by_name("new_group")).select_by_visible_text(contact.group)
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.secondary_address)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.secondary_telephone_home)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.secondary_notes)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact and start editing it
        wd.find_element_by_xpath("(//img[@title='Edit'])").click()
        # edit contact form
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        if contact.photo_path != "":
            wd.find_element_by_name("photo").send_keys(contact.photo_path)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.telephone_home)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.telephone_mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.telephone_work)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.telephone_fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birthday_day)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birthday_month)
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birthday_year)
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.anniversary_day)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary_month)
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.secondary_address)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.secondary_telephone_home)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.secondary_notes)
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
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(contact.first_name)
        if contact.middle_name != "":
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        if contact.last_name != "":
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(contact.last_name)
        if contact.nickname != "":
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(contact.nickname)
        if contact.photo_path != "":
            wd.find_element_by_name("photo").send_keys(contact.photo_path)
        if contact.title != "":
            wd.find_element_by_name("title").clear()
            wd.find_element_by_name("title").send_keys(contact.title)
        if contact.company != "":
            wd.find_element_by_name("company").clear()
            wd.find_element_by_name("company").send_keys(contact.company)
        if contact.address != "":
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys(contact.address)
        if contact.telephone_home != "":
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(contact.telephone_home)
        if contact.telephone_mobile != "":
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(contact.telephone_mobile)
        if contact.telephone_work != "":
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys(contact.telephone_work)
        if contact.telephone_fax != "":
            wd.find_element_by_name("fax").clear()
            wd.find_element_by_name("fax").send_keys(contact.telephone_fax)
        if contact.email != "":
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(contact.email)
        if contact.email2 != "":
            wd.find_element_by_name("email2").clear()
            wd.find_element_by_name("email2").send_keys(contact.email2)
        if contact.email3 != "":
            wd.find_element_by_name("email3").clear()
            wd.find_element_by_name("email3").send_keys(contact.email3)
        if contact.homepage != "":
            wd.find_element_by_name("homepage").clear()
            wd.find_element_by_name("homepage").send_keys(contact.homepage)
        if contact.birthday_day != "":
            Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birthday_day)
        if contact.birthday_month != "":
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birthday_month)
        if contact.birthday_year != "":
            wd.find_element_by_name("byear").clear()
            wd.find_element_by_name("byear").send_keys(contact.birthday_year)
        if contact.anniversary_day != "":
            Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.anniversary_day)
        if contact.anniversary_month != "":
            Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary_month)
        if contact.anniversary_year != "":
            wd.find_element_by_name("ayear").clear()
            wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        if contact.address != "":
            wd.find_element_by_name("address2").clear()
            wd.find_element_by_name("address2").send_keys(contact.secondary_address)
        if contact.secondary_telephone_home != "":
            wd.find_element_by_name("phone2").clear()
            wd.find_element_by_name("phone2").send_keys(contact.secondary_telephone_home)
        if contact.secondary_notes != "":
            wd.find_element_by_name("notes").clear()
            wd.find_element_by_name("notes").send_keys(contact.secondary_notes)
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
