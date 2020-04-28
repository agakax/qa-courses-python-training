from model.contact import Contact
import time


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_contact_form(self, first_name, middle_name, last_name, nickname, photo_path, photo_delete, title,
                          company, address, telephone_home, telephone_mobile, telephone_work, telephone_fax, email,
                          email2, email3, homepage, birthday_day, birthday_month, birthday_year, anniversary_day,
                          anniversary_month, anniversary_year, group, secondary_address, secondary_telephone_home,
                          secondary_notes):
        self.app.form.fill_form_element_by_its_name(field="firstname", value=first_name)
        self.app.form.fill_form_element_by_its_name(field="middlename", value=middle_name)
        self.app.form.fill_form_element_by_its_name(field="lastname", value=last_name)
        self.app.form.fill_form_element_by_its_name(field="nickname", value=nickname)
        self.app.form.fill_form_photo(field="photo", value=photo_path, delete=photo_delete)
        self.app.form.fill_form_element_by_its_name(field="title", value=title)
        self.app.form.fill_form_element_by_its_name(field="company", value=company)
        self.app.form.fill_form_element_by_its_name(field="address", value=address)
        self.app.form.fill_form_element_by_its_name(field="home", value=telephone_home)
        self.app.form.fill_form_element_by_its_name(field="mobile", value=telephone_mobile)
        self.app.form.fill_form_element_by_its_name(field="work", value=telephone_work)
        self.app.form.fill_form_element_by_its_name(field="fax", value=telephone_fax)
        self.app.form.fill_form_element_by_its_name(field="email", value=email)
        self.app.form.fill_form_element_by_its_name(field="email2", value=email2)
        self.app.form.fill_form_element_by_its_name(field="email3", value=email3)
        self.app.form.fill_form_element_by_its_name(field="homepage", value=homepage)
        self.app.form.fill_form_element_by_dropdown_list(field="bday", value=birthday_day)
        self.app.form.fill_form_element_by_dropdown_list(field="bmonth", value=birthday_month)
        self.app.form.fill_form_element_by_its_name(field="byear", value=birthday_year)
        self.app.form.fill_form_element_by_dropdown_list(field="aday", value=anniversary_day)
        self.app.form.fill_form_element_by_dropdown_list(field="amonth", value=anniversary_month)
        self.app.form.fill_form_element_by_its_name(field="ayear", value=anniversary_year)
        self.app.form.fill_form_element_by_dropdown_list(field="new_group", value=group)
        self.app.form.fill_form_element_by_its_name(field="address2", value=secondary_address)
        self.app.form.fill_form_element_by_its_name(field="phone2", value=secondary_telephone_home)
        self.app.form.fill_form_element_by_its_name(field="notes", value=secondary_notes)

    def create(self, contact):
        self.app.open_home_page()
        # init contact creation
        self.app.select.element_by_link_text(link_text="add new")
        # fill contact form with all possible fields
        self.fill_contact_form(first_name=contact.first_name,
                               middle_name=contact.middle_name,
                               last_name=contact.last_name,
                               nickname=contact.nickname,
                               photo_path=contact.photo_path,
                               photo_delete=False,
                               title=contact.title,
                               company=contact.company,
                               address=contact.address,
                               telephone_home=contact.telephone_home,
                               telephone_mobile=contact.telephone_mobile,
                               telephone_work=contact.telephone_work,
                               telephone_fax=contact.telephone_fax,
                               email=contact.email,
                               email2=contact.email2,
                               email3=contact.email3,
                               homepage=contact.homepage,
                               birthday_day=contact.birthday_day,
                               birthday_month=contact.birthday_month,
                               birthday_year=contact.birthday_year,
                               anniversary_day=contact.anniversary_day,
                               anniversary_month=contact.anniversary_month,
                               anniversary_year=contact.anniversary_year,
                               group=contact.group,
                               secondary_address=contact.secondary_address,
                               secondary_telephone_home=contact.secondary_telephone_home,
                               secondary_notes=contact.secondary_notes)
        # submit contact creation
        self.app.select.element_by_xpath(field="input", field_type="name", field_value="submit",
                                         field_occurrence="[2]")
        self.return_to_home_page()
        self.contact_cache = None

    def modify_first_contact(self, contact):
        self.app.open_home_page()
        # select first contact and open it
        self.app.select.element_by_xpath(field="img", field_type="title", field_value="Edit")
        # edit contact form
        self.fill_contact_form(first_name=contact.first_name,
                               middle_name=contact.middle_name,
                               last_name=contact.last_name,
                               nickname=contact.nickname,
                               photo_path=contact.photo_path,
                               photo_delete=contact.photo_delete,
                               title=contact.title,
                               company=contact.company,
                               address=contact.address,
                               telephone_home=contact.telephone_home,
                               telephone_mobile=contact.telephone_mobile,
                               telephone_work=contact.telephone_work,
                               telephone_fax=contact.telephone_fax,
                               email=contact.email,
                               email2=contact.email2,
                               email3=contact.email3,
                               homepage=contact.homepage,
                               birthday_day=contact.birthday_day,
                               birthday_month=contact.birthday_month,
                               birthday_year=contact.birthday_year,
                               anniversary_day=contact.anniversary_day,
                               anniversary_month=contact.anniversary_month,
                               anniversary_year=contact.anniversary_year,
                               group=None,
                               secondary_address=contact.secondary_address,
                               secondary_telephone_home=contact.secondary_telephone_home,
                               secondary_notes=contact.secondary_notes)
        # submit contact modification
        self.app.select.element_by_xpath(field="input", field_type="name", field_value="update",
                                         field_occurrence="[2]")
        self.return_to_home_page()
        self.contact_cache = None

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            string = "//table[@id='maintable']/tbody/tr[@name='entry']"
            for element in wd.find_elements_by_xpath(string):
                title = element.find_element_by_xpath("td[1]/input[@name='selected[]']").get_attribute("title")[8:-1]
                first_name = element.find_element_by_xpath("td[3]").text
                last_name = element.find_element_by_xpath("td[2]").text
                address = element.find_element_by_xpath("td[4]").text
                id_contact = element.find_element_by_xpath("td[1]/input[@name='selected[]']").get_attribute("id")
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, title=title,
                                                  address=address, id_contact=id_contact))
        return list(self.contact_cache)

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        self.app.select.element_by_name(name="selected[]")
        # submit deletion
        self.app.select.element_by_xpath(field="input", field_type="value", field_value="Delete")
        wd.switch_to_alert().accept()
        # waiting for it to be sure deleting went fully
        wd.find_element_by_css_selector("div.msgbox")
        self.app.open_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        string = "selected[]"
        return len(wd.find_elements_by_name(string))

    def return_to_home_page(self):
        self.app.select.element_by_link_text(link_text="home page")
