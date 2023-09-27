from __init__ import CURSOR, CONN
from group import Group

class Adventurer:

    def __init__(self, name, job, alignment, level, group_id, id=None):
        self.id = id
        self.name = name
        self.job = job
        self.alignment = alignment
        self.level = level
        self.group_id = group_id