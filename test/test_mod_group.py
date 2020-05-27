import random
from model.group import Group


def test_modify_group(app, db, json_group, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test1", header="test1", footer="test1"))
    old_groups = db.get_group_list()
    group_to_modify = random.choice(old_groups)
    group = json_group
    group.id = group_to_modify.id
    app.group.modify_group_by_id(group=group)
    assert len(old_groups) == len(db.get_group_list())
    new_groups = db.get_group_list()
    old_groups.remove(group_to_modify)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted((map(lambda x: clean(x), new_groups)), key=Group.id_or_max) == \
               sorted((map(lambda x: clean(x), app.group.get_group_list())), key=Group.id_or_max)


def clean(group):
    return Group(id_group=group.id, name=group.name.strip())