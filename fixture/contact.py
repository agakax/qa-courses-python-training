import re
from model.contact import Contact


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
                                         field_occurrence=2)
        self.return_to_home_page()
        self.contact_cache = None

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(index=0, contact=contact)

    def modify_contact_by_index(self, index, contact):
        self.app.open_home_page()
        # select specific contact and open it (occurrences are counted from 0, xpath is counted from 1)
        self.app.select.element_by_xpath(field="img", field_type="title", field_value="Edit",
                                         field_occurrence=index + 1)
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
                                         field_occurrence=2)
        self.return_to_home_page()
        self.contact_cache = None

    contact_cache = None

    def open_contact_details_page(self, index):
        self.app.open_home_page()
        # as normally we're indexing from 0, and xpath is indexing from 1 I made such change
        self.app.select.element_by_xpath(field="img", field_type="title", field_value="Details",
                                         field_occurrence=index + 1)

    def open_contact_edit_page(self, index):
        self.app.open_home_page()
        # as normally we're indexing from 0, and xpath is indexing from 1 I made such change
        self.app.select.element_by_xpath(field="img", field_type="title", field_value="Edit",
                                         field_occurrence=index + 1)

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            string = "//table[@id='maintable']/tbody/tr[@name='entry']"
            for element in wd.find_elements_by_xpath(string):
                # title: first name, last name
                title = element.find_element_by_xpath("td[1]/input[@name='selected[]']").get_attribute("title")[8:-1]
                first_name = element.find_element_by_xpath("td[3]").text
                last_name = element.find_element_by_xpath("td[2]").text
                address = element.find_element_by_xpath("td[4]").text
                emails_all = element.find_element_by_xpath("td[5]").text
                telephones_all = element.find_element_by_xpath("td[6]").text
                id_contact = element.find_element_by_xpath("td[1]/input[@name='selected[]']").get_attribute("id")
                self.contact_cache.append(Contact(first_name=first_name,
                                                  last_name=last_name,
                                                  title=title,
                                                  address=address,
                                                  emails_all=emails_all,
                                                  telephones_all=telephones_all,
                                                  id_contact=id_contact))
        return list(self.contact_cache)

    def if_regex_exist(self, result):
        if result:
            return result.group(1)
        else:
            return ""

    def get_contact_info_from_details_page(self, index):
        wd = self.app.wd
        self.open_contact_details_page(index=index)
        text = wd.find_element_by_id("content").text
        emails_all = []
        homepage = ""
        group_id = ""
        for element in wd.find_element_by_id("content").find_elements_by_css_selector("a"):
            link = element.get_attribute("href")
            if link.startswith("mailto:"):
                emails_all.append(link[7:])
            elif link.startswith("http://localhost/addressbook/index.php?group="):
                group_id = link[45:]
            else:
                homepage = link
        # title: first name, second name, last name
        title = wd.find_element_by_xpath("//div[@id='content']/b").text
        telephone_home = self.if_regex_exist(re.search("H: (.*)", text))
        telephone_mobile = self.if_regex_exist(re.search("M: (.*)", text))
        telephone_work = self.if_regex_exist(re.search("W: (.*)", text))
        telephone_fax = self.if_regex_exist(re.search("F: (.*)", text))
        secondary_telephone_home = self.if_regex_exist(re.search("P: (.*)", text))
        id_contact = wd.find_element_by_name("id").get_attribute("value")
        return Contact(title=title,
                       telephone_home=telephone_home,
                       telephone_mobile=telephone_mobile,
                       telephone_work=telephone_work,
                       telephone_fax=telephone_fax,
                       secondary_telephone_home=secondary_telephone_home,
                       emails_all=emails_all,
                       homepage=homepage,
                       id_contact=id_contact)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_edit_page(index=index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        middle_name = wd.find_element_by_name("middlename").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        nickname = wd.find_element_by_name("nickname").get_attribute("value")
        title = wd.find_element_by_name("title").get_attribute("value")
        company = wd.find_element_by_name("company").get_attribute("value")
        address = wd.find_element_by_name("address").text
        telephone_home = wd.find_element_by_name("home").get_attribute("value")
        telephone_mobile = wd.find_element_by_name("mobile").get_attribute("value")
        telephone_work = wd.find_element_by_name("work").get_attribute("value")
        telephone_fax = wd.find_element_by_name("fax").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homepage = wd.find_element_by_name("homepage").get_attribute("value")
        birthday_day = wd.find_elements_by_name("bday")[0].text.splitlines()[0]
        birthday_month = wd.find_elements_by_name("bmonth")[0].text.splitlines()[0]
        birthday_year = wd.find_element_by_name("byear").get_attribute("value")
        anniversary_day = wd.find_elements_by_name("aday")[0].text.splitlines()[0]
        anniversary_month = wd.find_elements_by_name("amonth")[0].text.splitlines()[0]
        anniversary_year = wd.find_element_by_name("ayear").get_attribute("value")
        secondary_address = wd.find_element_by_name("address2").text
        secondary_telephone_home = wd.find_element_by_name("phone2").get_attribute("value")
        secondary_notes = wd.find_element_by_name("notes").text
        id_contact = wd.find_element_by_name("id").get_attribute("value")
        return Contact(first_name=first_name,
                       middle_name=middle_name,
                       last_name=last_name,
                       nickname=nickname,
                       title=title,
                       company=company,
                       address=address,
                       telephone_home=telephone_home,
                       telephone_mobile=telephone_mobile,
                       telephone_work=telephone_work,
                       telephone_fax=telephone_fax,
                       email=email,
                       email2=email2,
                       email3=email3,
                       homepage=homepage,
                       birthday_day=birthday_day,
                       birthday_month=birthday_month,
                       birthday_year=birthday_year,
                       anniversary_day=anniversary_day,
                       anniversary_month=anniversary_month,
                       anniversary_year=anniversary_year,
                       secondary_address=secondary_address,
                       secondary_telephone_home=secondary_telephone_home,
                       secondary_notes=secondary_notes,
                       id_contact=id_contact)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # select specific contact
        self.app.select.element_by_name_by_index(name="selected[]", index=index)
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
