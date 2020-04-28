from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        string = "new"
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name(string)) > 0):
            self.app.select.element_by_link_text(link_text="groups")

    def fill_group_form(self, name, header, footer):
        self.app.form.fill_form_element_by_its_name(field="group_name", value=name)
        self.app.form.fill_form_element_by_its_name(field="group_header", value=header)
        self.app.form.fill_form_element_by_its_name(field="group_footer", value=footer)

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            string = "span.group"
            for element in wd.find_elements_by_css_selector(string):
                text = element.text
                id_group = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id_group=id_group))
        return list(self.group_cache)

    def create(self, group):
        self.open_groups_page()
        # init group creation
        self.app.select.element_by_name(name="new")
        # fill group form
        self.fill_group_form(name=group.name, header=group.header, footer=group.footer)
        # submit group creation
        self.app.select.element_by_name(name="submit")
        self.return_to_groups_page()
        self.group_cache = None

    def modify_first_group(self, group):
        self.open_groups_page()
        # find first group and open it
        self.app.select.element_by_name(name="selected[]")
        self.app.select.element_by_xpath(field="input", field_type="name", field_value="edit",
                                         field_occurrence="[2]")
        # edit group form
        self.fill_group_form(name=group.name, header=group.header, footer=group.footer)
        # submit group modification
        self.app.select.element_by_name(name="update")
        self.return_to_groups_page()
        self.group_cache = None

    def delete_first_group(self):
        self.open_groups_page()
        # select first group
        self.app.select.element_by_name(name="selected[]")
        # submit deletion
        self.app.select.element_by_name(name="delete")
        self.return_to_groups_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        string = "selected[]"
        return len(wd.find_elements_by_name(string))

    def return_to_groups_page(self):
        self.app.select.element_by_link_text(link_text="group page")
