from model.group import Group


def test_modify_first_group_all(app):
    app.group.modify_first_group(
        Group(name="modified group", header="modified header", footer="modified group footer (comment)"))


def test_modify_first_group_name(app):
    app.group.modify_first_group(Group(name="modified name"))
