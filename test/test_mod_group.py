from model.group import Group


def test_modify_first_group_all(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(
        Group(name="modified group", header="modified header", footer="modified group footer (comment)"))
    app.session.logout()


def test_modify_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="modified name"))
    app.session.logout()
