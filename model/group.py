from sys import maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, id_group=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id_group

    def __repr__(self):
        return "%s: %s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               self.check_for_none(self.name, other.name)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def check_for_none(self, first, second):
        return first == second or (first is None and second == "") or (first == "" and second is None)
