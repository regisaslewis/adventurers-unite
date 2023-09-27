from __init__ import CURSOR, CONN
import string

CONTINENT = {
    "Bettle": ["Burg", "Hommoch", "Lei"],
    "Jidoth": ["Lord's Port", "Oth", "Tirena", "Videlsen"],
    "Mollen": ["Aldon", "Exigot", "Len City", "Pelta", "Vanna's Perch"],
    "Rise": ["Expanse", "Mouth", "Shelf"]
}

class Group:

    all = {}

    def __init__(self, name, continent, city, id=None):
        self.id = id
        self.name = name
        self.continent = continent
        self.city = city
    
    def __repr__(self):
        name_ = f"Group {self.id}: {self.name}"
        cont_ = f"Continent: {self.continent}"
        city_ = f"City: {self.city}"
        def pick_length():
            if len(name_) >= len(cont_) and len(name_) >= len(city_):
                return "_" * len(name_)
            if len(cont_) >= len(city_):
                return "_" * len(cont_)
            return "_" * len(city_)
        return f"{name_}\n{cont_}\n{city_}\n{pick_length()}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string.")
    
    @property
    def continent(self):
        return self._continent
    
    @continent.setter
    def continent(self, continent):
        if continent.title() in CONTINENT:
            self._continent = continent.title()
        else:
            raise ValueError(f"{continent.title()} is not a valid continent.")
        
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, city):
        if string.capwords(city) in CONTINENT[self.continent]:
            self._city = string.capwords(city)
        else:
            raise ValueError(f"{string.capwords(city)} is not a valid city in {self.continent}.")

# ala = Group("Ala's Defilers", "jidoth", "Lord's Port", 1)
# print(ala)
# becco = Group("Becco", "Mollen", "len city", 2)
# print(becco)
# ciolta = Group("Ciolta", "RISE", "Expanse", 3)
# print(ciolta)