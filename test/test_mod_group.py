from random import randrange
from model.group import Group


def test_modify_group_all_fields_by_index(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test1", header="test1", footer="test1"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="modified group", header="modified header", footer="modified group footer (comment)")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index=index, group=group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test2", footer="test2"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="modified name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
