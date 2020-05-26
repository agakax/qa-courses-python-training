import random
from model.group import Group


def test_modify_group(app, db, json_group):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test1", header="test1", footer="test1"))
    old_groups = db.get_group_list()
    group_to_modify = random.choice(old_groups)
    group = json_group
    group.id = group_to_modify.id
    app.group.modify_group_by_id(group=group)
    assert len(old_groups) == len(db.get_group_list())
    new_groups = app.group.get_group_list()
    old_groups.remove(group_to_modify)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
