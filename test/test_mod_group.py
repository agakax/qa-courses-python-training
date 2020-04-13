from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="30 modified group", footer="modified group footer (comment)"))
    app.session.logout()


def test_modify_selected_fields_in_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_selected_fields_in_first_group(Group(name="40 modified name"))
    app.session.logout()
