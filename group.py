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
        cont_length = "_" * (len("Continent: ") + len(self.continent))
        city_length = "_" * (len("City: ") + len(self.city))
        return f"Group {self.id}: {self.name}\nCity: {self.city}\nContinent: {self.continent}\n{cont_length if cont_length > city_length else city_length}"
    
ala = Group("Ala", "Bettle", "Burg", 1)
print(ala)
becco = Group("Becco", "Rise", "Expanse", 2)
print(becco)
ciolt = Group("Ciolt", "Mollen", "Vanna's Perch", 3)
print(ciolt)