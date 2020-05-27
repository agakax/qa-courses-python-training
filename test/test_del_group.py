import random
from model.group import Group


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    assert len(old_groups) - 1 == len(db.get_group_list())
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted((map(lambda x: clean(x), new_groups)), key=Group.id_or_max) == \
               sorted((map(lambda x: clean(x), app.group.get_group_list())), key=Group.id_or_max)


def clean(group):
    return Group(id_group=group.id, name=group.name.strip())
