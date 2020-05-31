from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id_group = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups", lazy=True)

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        id_contact = PrimaryKey(int, column="id")
        first_name = Optional(str, column="firstname")
        middle_name = Optional(str, column="middlename")
        last_name = Optional(str, column="lastname")
        nickname = Optional(str, column="nickname")
        photo_info = Optional(str, column="photo")
        title = Optional(str, column="title")
        company = Optional(str, column="company")
        address = Optional(str, column="address")
        telephone_home = Optional(str, column="home")
        telephone_mobile = Optional(str, column="mobile")
        telephone_work = Optional(str, column="work")
        telephone_fax = Optional(str, column="fax")
        email = Optional(str, column="email")
        email2 = Optional(str, column="email2")
        email3 = Optional(str, column="email3")
        homepage = Optional(str, column="homepage")
        birthday_day = Optional(str, column="bday")
        birthday_month = Optional(str, column="bmonth")
        birthday_year = Optional(str, column="byear")
        anniversary_day = Optional(str, column="aday")
        anniversary_month = Optional(str, column="amonth")
        anniversary_year = Optional(str, column="ayear")
        address2 = Optional(str, column="address2")
        phone2 = Optional(str, column="phone2")
        notes2 = Optional(str, column="notes")
        deprecated = Optional(datetime, column="deprecated")
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts", lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind("mysql", host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id_group=str(group.id_group), name=group.name, header=group.header, footer=group.footer)

        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id_contact=str(contact.id_contact), first_name=contact.first_name,
                           middle_name=contact.middle_name, last_name=contact.last_name, nickname=contact.nickname,
                           photo_path=contact.photo_info, title=contact.title, company=contact.company,
                           address=contact.address, telephone_home=contact.telephone_home,
                           telephone_mobile=contact.telephone_mobile, telephone_work=contact.telephone_work,
                           telephone_fax=contact.telephone_fax, email=contact.email, email2=contact.email2,
                           email3=contact.email3, homepage=contact.homepage, birthday_day=contact.birthday_day,
                           birthday_month=contact.birthday_month, birthday_year=contact.birthday_year,
                           anniversary_day=contact.anniversary_day, anniversary_month=contact.anniversary_month,
                           anniversary_year=contact.anniversary_year, secondary_address=contact.address2,
                           secondary_telephone_home=contact.phone2, secondary_notes=contact.notes2)

        return list(map(convert, contacts))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id_group == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id_group == group.id))[0]
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))

    @db_session
    def get_group_in_contact(self, contact):
        orm_contact = list(select(c for c in ORMFixture.ORMContact if c.deprecated is None and c.id_contact == contact.id))[0]
        return self.convert_groups_to_model(orm_contact.groups)

    def get_all_contacts_in_groups(self):
        contacts_in_groups = []
        groups = self.get_group_list()
        for group in groups:
            contacts = self.get_contacts_in_group(group)
            if len(contacts) > 0:
                for contact in contacts:
                    contacts_in_groups.append(contact)
        return contacts_in_groups

    def get_all_contacts_not_in_groups(self):
        contacts_not_in_groups = self.get_contact_list()
        groups = self.get_group_list()
        for group in groups:
            contacts = self.get_contacts_in_group(group)
            if len(contacts) > 0:
                for contact in contacts:
                    contacts_not_in_groups.remove(contact)
        return contacts_not_in_groups
