from __init__ import CURSOR, CONN

class Group:

    all = {}
    
    CONTINENT = {
        "Bettle": ["Burg", "Hommoch", "Lei"],
        "Jidoth": ["Lord's Port", "Oth", "Tirena", "Videlsen"],
        "Mollen": ["Aldon", "Exigot", "Len City", "Pelta", "Vanna's Perch"],
        "Rise": ["Expanse", "Mouth", "Shelf"]
    }

    def __init__(self, name, continent, city, id=None):
        self.id = id
        self.name = name
        self.continent = continent
        self.city = city
    
    def __repr__(self):
        return f"Group {self.id}: {self.name} of {self.city}, {self.continent}"