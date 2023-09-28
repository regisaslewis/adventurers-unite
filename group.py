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
        return f"{pick_length()}\n{name_}\n{cont_}\n{city_}\n{pick_length()}"
    
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
        
    # Creating, Deleting, and Saving the Table
    @classmethod
    def make_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS groups (
            id INTEGER PRIMARY KEY,
            name TEXT,
            continent TEXT,
            city TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def remove_table(self):
        sql = """
            DROP TABLE IF EXISTS groups;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save_new_row(self):
        sql = """
            INSERT INTO groups (name, continent, city)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql,(self.name, self.continent, self.city))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self #(this adds it to the 'all' dictionary, with the new self.id as the key!)
    #==================================
    # CRUD for the SQL Database
    @classmethod
    def create(cls, name, continent, city):
        group = cls(name, continent, city)
        group.save_new_row()
        return group
    
    def update(self):
        sql = """
        UPDATE groups
        SET name = ?, continent = ?, city = ?
        WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.continent, self.city, self.id))
        CONN.commit()

    def delete(self):
        sql = """
        DELETE FROM groups
        WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id] #(removes from 'all' dictionary)
        self.id = None #(key no longer associated with that id)
    #==================================
    # Class Methods to view Group Information

    @classmethod
    def instance_from_database(cls, row):
        group = cls.all.get(row[0])
        if group:
            group.name = row[1]
            group.continent = row[2]
            group.city = row[3]
        else:
            group = cls(row[1], row[2], row[3])
            group.id = row[0]
            cls.all[group.id] = group
        return group
        # just a mediator method for the other methods that actually let one view the contents of the database
    
    @classmethod
    def get_all(cls):
        sql = """
        SELECT *
        FROM groups
        """
        database = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_database(n) for n in database]
    
    @classmethod
    def get_by_id(cls, id):
        sql = """
        SELECT *
        FROM groups
        WHERE id = ?
        """
        n = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_database(n) if n else None
    
    @classmethod
    def get_by_name(cls, name):
        sql = """
        SELECT *
        FROM groups
        WHERE name = ?
        """
        n = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_database(n) if n else None
    





Group.remove_table()
Group.make_table()
ala = Group.create("The Party of Ala", "Jidoth", "Lord's Port")
becco = Group.create("Becco", "Mollen", "len city")
ciolta = Group.create("Ciolta's Lookouts", "RISE", "expanse")
destructors = Group.create("The Destructors", "Mollen", "vanna's perch")
# for n in Group.get_all():
#     print(n)
print(Group.get_by_id(2))
print(Group.get_by_name("The Party of Ala"))