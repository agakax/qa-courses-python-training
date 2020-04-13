class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.app.form.fill_form_element_by_its_name(field="group_name", value=group.name)
        self.app.form.fill_form_element_by_its_name(field="group_header", value=group.header)
        self.app.form.fill_form_element_by_its_name(field="group_footer", value=group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def modify_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # find first group and enter it
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("(//input[@name='edit'])[2]").click()
        # edit group form
        self.app.form.fill_form_element_by_its_name(field="group_name", value=group.name)
        self.app.form.fill_form_element_by_its_name(field="group_header", value=group.header)
        self.app.form.fill_form_element_by_its_name(field="group_footer", value=group.footer)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def modify_selected_fields_in_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # find first group and enter it
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("(//input[@name='edit'])[2]").click()
        # edit group form
        if group.name != "":
            self.app.form.fill_form_element_by_its_name(field="group_name", value=group.name)
        if group.header != "":
            self.app.form.fill_form_element_by_its_name(field="group_header", value=group.header)
        if group.footer != "":
            self.app.form.fill_form_element_by_its_name(field="group_footer", value=group.footer)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
