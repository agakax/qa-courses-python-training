class Contact:

    def __init__(self, first_name="", middle_name="", last_name="", nickname="",
                 photo_path=r"", photo_delete=False, title="", company="", address="", telephone_home="",
                 telephone_mobile="", telephone_work="", telephone_fax="", email="", email2="", email3="", homepage="",
                 birthday_day="", birthday_month="-", birthday_year="", anniversary_day="", anniversary_month="-",
                 anniversary_year="", group="[none]", secondary_address="", secondary_telephone_home="",
                 secondary_notes=""):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.photo_path = photo_path
        self.photo_delete = photo_delete
        self.title = title
        self.company = company
        self.address = address
        self.telephone_home = telephone_home
        self.telephone_mobile = telephone_mobile
        self.telephone_work = telephone_work
        self.telephone_fax = telephone_fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birthday_day = birthday_day
        self.birthday_month = birthday_month
        self.birthday_year = birthday_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year
        self.group = group
        self.secondary_address = secondary_address
        self.secondary_telephone_home = secondary_telephone_home
        self.secondary_notes = secondary_notes
