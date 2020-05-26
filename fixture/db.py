import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        cursor = self.connection.cursor()
        groups = []
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id_group, name, header, footer) = row
                groups.append(Group(id_group=str(id_group), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return groups

    def get_contact_list(self):
        cursor = self.connection.cursor()
        contacts = []
        try:

            cursor.execute(
                "SELECT id, firstname, middlename, lastname, nickname, photo, title, company, address, home, mobile, "
                "work, fax, email, email2, email3, homepage, bday, bmonth, byear, aday, amonth, ayear, address2, "
                "phone2, notes FROM addressbook WHERE deprecated = 0")

            for row in cursor:
                (id_contact, first_name, middle_name, last_name, nickname, photo_info, title, company, address,
                 telephone_home, telephone_mobile, telephone_work, telephone_fax, email, email2, email3, homepage, bday,
                 bmonth, byear, aday, amonth, ayear, address2, phone2, notes2) = row
                contacts.append(
                    Contact(id_contact=id_contact, first_name=first_name, middle_name=middle_name, last_name=last_name,
                            nickname=nickname, photo_path=photo_info, title=title, company=company, address=address,
                            telephone_home=telephone_home, telephone_mobile=telephone_mobile,
                            telephone_work=telephone_work, telephone_fax=telephone_fax, email=email, email2=email2,
                            email3=email3, homepage=homepage, birthday_day=bday, birthday_month=bmonth,
                            birthday_year=byear, anniversary_day=aday, anniversary_month=amonth, anniversary_year=ayear,
                            secondary_address=address2, secondary_telephone_home=phone2, secondary_notes=notes2))
        finally:
            cursor.close()
        return contacts

    def destroy(self):
        self.connection.close()
