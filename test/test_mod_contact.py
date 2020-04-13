from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(
        first_name="Lev",
        middle_name="Nikolayevich",
        last_name="Tolstoy",
        photo_path=r"C:\Users\agakax\Downloads\avatar.png",
        address=r"Yasnaya Polyana",
        birthday_day="9",
        birthday_month="September",
        birthday_year="1828",
        anniversary_day="20",
        anniversary_month="November",
        anniversary_year="1910",
    ))
    app.session.logout()


def test_modify_first_contact_with_photo_deletion(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(
        first_name="Jan",
        last_name="Brzechwa",
        photo_delete=True,
        address=r"Kresy Wschodnie",
        birthday_day="15",
        birthday_month="August",
        birthday_year="1898",
        anniversary_day="2",
        anniversary_month="July",
        anniversary_year="1966",
    ))
    app.session.logout()
