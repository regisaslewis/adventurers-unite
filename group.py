from __init__ import CURSOR, CONN

class Group:

    def __init__(self, name, continent, city, id=None):
        self.id = id
        self.name = name
        self.continent = continent
        self.city = city