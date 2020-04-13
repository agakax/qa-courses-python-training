from model.group import Group


def test_modify_first_group_all(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test1", header="test1", footer="test1"))
    app.group.modify_first_group(
        Group(name="modified group", header="modified header", footer="modified group footer (comment)"))


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test2", footer="test2"))
    app.group.modify_first_group(Group(name="modified name"))
