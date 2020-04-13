class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        self.app.select.element_by_link_text(link_text="groups")

    def fill_group_form(self, name, header, footer):
        self.app.form.fill_form_element_by_its_name(field="group_name", value=name)
        self.app.form.fill_form_element_by_its_name(field="group_header", value=header)
        self.app.form.fill_form_element_by_its_name(field="group_footer", value=footer)

    def create(self, group):
        self.open_groups_page()
        # init group creation
        self.app.select.element_by_name(name="new")
        # fill group form
        self.fill_group_form(name=group.name, header=group.header, footer=group.footer)
        # submit group creation
        self.app.select.element_by_name(name="submit")
        self.return_to_groups_page()

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

    def delete_first_group(self):
        self.open_groups_page()
        # select first group
        self.app.select.element_by_name(name="selected[]")
        # submit deletion
        self.app.select.element_by_name(name="delete")
        self.return_to_groups_page()

    def return_to_groups_page(self):
        self.app.select.element_by_link_text(link_text="group page")
