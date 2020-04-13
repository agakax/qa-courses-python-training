class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        self.app.open_home_page()
        # init contact creation
        self.app.select.element_by_link_text(link_text="add new")
        # fill contact form with all possible fields
        self.app.form.fill_form_element_by_its_name(field="firstname", value=contact.first_name)
        self.app.form.fill_form_element_by_its_name(field="middlename", value=contact.middle_name)
        self.app.form.fill_form_element_by_its_name(field="lastname", value=contact.last_name)
        self.app.form.fill_form_element_by_its_name(field="nickname", value=contact.nickname)
        self.app.form.fill_form_photo(field="photo", value=contact.photo_path, delete=False)
        self.app.form.fill_form_element_by_its_name(field="title", value=contact.title)
        self.app.form.fill_form_element_by_its_name(field="company", value=contact.company)
        self.app.form.fill_form_element_by_its_name(field="address", value=contact.address)
        self.app.form.fill_form_element_by_its_name(field="home", value=contact.telephone_home)
        self.app.form.fill_form_element_by_its_name(field="mobile", value=contact.telephone_mobile)
        self.app.form.fill_form_element_by_its_name(field="work", value=contact.telephone_work)
        self.app.form.fill_form_element_by_its_name(field="fax", value=contact.telephone_fax)
        self.app.form.fill_form_element_by_its_name(field="email", value=contact.email)
        self.app.form.fill_form_element_by_its_name(field="email2", value=contact.email2)
        self.app.form.fill_form_element_by_its_name(field="email3", value=contact.email3)
        self.app.form.fill_form_element_by_its_name(field="homepage", value=contact.homepage)
        self.app.form.fill_form_element_by_dropdown_list(field="bday", value=contact.birthday_day)
        self.app.form.fill_form_element_by_dropdown_list(field="bmonth", value=contact.birthday_month)
        self.app.form.fill_form_element_by_its_name(field="byear", value=contact.birthday_year)
        self.app.form.fill_form_element_by_dropdown_list(field="aday", value=contact.anniversary_day)
        self.app.form.fill_form_element_by_dropdown_list(field="amonth", value=contact.anniversary_month)
        self.app.form.fill_form_element_by_its_name(field="ayear", value=contact.anniversary_year)
        self.app.form.fill_form_element_by_dropdown_list(field="new_group", value=contact.group)
        self.app.form.fill_form_element_by_its_name(field="address2", value=contact.secondary_address)
        self.app.form.fill_form_element_by_its_name(field="phone2", value=contact.secondary_telephone_home)
        self.app.form.fill_form_element_by_its_name(field="notes", value=contact.secondary_notes)
        # submit contact creation
        self.app.select.element_by_xpath(field="input", field_type="name", field_value="submit",
                                         field_occurrence="[2]")
        self.return_to_home_page()

    def modify_first_contact(self, contact):
        self.app.open_home_page()
        # select first contact and start editing it
        self.app.select.element_by_xpath(field="img", field_type="title", field_value="Edit")
        # edit contact form
        self.app.form.fill_form_element_by_its_name(field="firstname", value=contact.first_name)
        self.app.form.fill_form_element_by_its_name(field="middlename", value=contact.middle_name)
        self.app.form.fill_form_element_by_its_name(field="lastname", value=contact.last_name)
        self.app.form.fill_form_element_by_its_name(field="nickname", value=contact.nickname)
        self.app.form.fill_form_photo(field="photo", value=contact.photo_path, delete=contact.photo_delete)
        self.app.form.fill_form_element_by_its_name(field="title", value=contact.title)
        self.app.form.fill_form_element_by_its_name(field="company", value=contact.company)
        self.app.form.fill_form_element_by_its_name(field="address", value=contact.address)
        self.app.form.fill_form_element_by_its_name(field="home", value=contact.telephone_home)
        self.app.form.fill_form_element_by_its_name(field="mobile", value=contact.telephone_mobile)
        self.app.form.fill_form_element_by_its_name(field="work", value=contact.telephone_work)
        self.app.form.fill_form_element_by_its_name(field="fax", value=contact.telephone_fax)
        self.app.form.fill_form_element_by_its_name(field="email", value=contact.email)
        self.app.form.fill_form_element_by_its_name(field="email2", value=contact.email2)
        self.app.form.fill_form_element_by_its_name(field="email3", value=contact.email3)
        self.app.form.fill_form_element_by_its_name(field="homepage", value=contact.homepage)
        self.app.form.fill_form_element_by_dropdown_list(field="bday", value=contact.birthday_day)
        self.app.form.fill_form_element_by_dropdown_list(field="bmonth", value=contact.birthday_month)
        self.app.form.fill_form_element_by_its_name(field="byear", value=contact.birthday_year)
        self.app.form.fill_form_element_by_dropdown_list(field="aday", value=contact.anniversary_day)
        self.app.form.fill_form_element_by_dropdown_list(field="amonth", value=contact.anniversary_month)
        self.app.form.fill_form_element_by_its_name(field="ayear", value=contact.anniversary_year)
        self.app.form.fill_form_element_by_its_name(field="address2", value=contact.secondary_address)
        self.app.form.fill_form_element_by_its_name(field="phone2", value=contact.secondary_telephone_home)
        self.app.form.fill_form_element_by_its_name(field="notes", value=contact.secondary_notes)
        # submit contact modification
        self.app.select.element_by_xpath(field="input", field_type="name", field_value="update",
                                         field_occurrence="[2]")
        self.return_to_home_page()

    def modify_selected_fields_in_first_contact(self, contact):
        self.app.open_home_page()
        # select first contact and start editing it
        self.app.select.element_by_xpath(field="img", field_type="title", field_value="Edit")
        # edit contact form
        if contact.first_name != "":
            self.app.form.fill_form_element_by_its_name(field="firstname", value=contact.first_name)
        if contact.middle_name != "":
            self.app.form.fill_form_element_by_its_name(field="middlename", value=contact.middle_name)
        if contact.last_name != "":
            self.app.form.fill_form_element_by_its_name(field="lastname", value=contact.last_name)
        if contact.nickname != "":
            self.app.form.fill_form_element_by_its_name(field="nickname", value=contact.nickname)
        if contact.photo_path != "" or contact.photo_delete:
            self.app.form.fill_form_photo(field="photo", value=contact.photo_path, delete=contact.photo_delete)
        if contact.title != "":
            self.app.form.fill_form_element_by_its_name(field="title", value=contact.title)
        if contact.company != "":
            self.app.form.fill_form_element_by_its_name(field="company", value=contact.company)
        if contact.address != "":
            self.app.form.fill_form_element_by_its_name(field="address", value=contact.address)
        if contact.telephone_home != "":
            self.app.form.fill_form_element_by_its_name(field="home", value=contact.telephone_home)
        if contact.telephone_mobile != "":
            self.app.form.fill_form_element_by_its_name(field="mobile", value=contact.telephone_mobile)
        if contact.telephone_work != "":
            self.app.form.fill_form_element_by_its_name(field="work", value=contact.telephone_work)
        if contact.telephone_fax != "":
            self.app.form.fill_form_element_by_its_name(field="fax", value=contact.telephone_fax)
        if contact.email != "":
            self.app.form.fill_form_element_by_its_name(field="email", value=contact.email)
        if contact.email2 != "":
            self.app.form.fill_form_element_by_its_name(field="email2", value=contact.email2)
        if contact.email3 != "":
            self.app.form.fill_form_element_by_its_name(field="email3", value=contact.email3)
        if contact.homepage != "":
            self.app.form.fill_form_element_by_its_name(field="homepage", value=contact.homepage)
        if contact.birthday_day != "":
            self.app.form.fill_form_element_by_dropdown_list(field="bday", value=contact.birthday_day)
        if contact.birthday_month != "":
            self.app.form.fill_form_element_by_dropdown_list(field="bmonth", value=contact.birthday_month)
        if contact.birthday_year != "":
            self.app.form.fill_form_element_by_its_name(field="byear", value=contact.birthday_year)
        if contact.anniversary_day != "":
            self.app.form.fill_form_element_by_dropdown_list(field="aday", value=contact.anniversary_day)
        if contact.anniversary_month != "":
            self.app.form.fill_form_element_by_dropdown_list(field="amonth", value=contact.anniversary_month)
        if contact.anniversary_year != "":
            self.app.form.fill_form_element_by_its_name(field="ayear", value=contact.anniversary_year)
        if contact.address != "":
            self.app.form.fill_form_element_by_its_name(field="address2", value=contact.secondary_address)
        if contact.secondary_telephone_home != "":
            self.app.form.fill_form_element_by_its_name(field="phone2", value=contact.secondary_telephone_home)
        if contact.secondary_notes != "":
            self.app.form.fill_form_element_by_its_name(field="notes", value=contact.secondary_notes)
        # submit contact modification
        self.app.select.element_by_xpath(field="input", field_type="name", field_value="update",
                                         field_occurrence="[2]")
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        self.app.select.element_by_name(name="selected[]")
        # submit deletion
        self.app.select.element_by_xpath(field="input", field_type="value", field_value="Delete")
        wd.switch_to_alert().accept()
        self.app.open_home_page()

    def return_to_home_page(self):
        self.app.select.element_by_link_text(link_text="home page")
