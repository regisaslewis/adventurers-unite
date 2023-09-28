from __init__ import CURSOR, CONN
from group import Group

JOB = [
    "Brawler",
    "Director",
    "Feral",
    "Hopeless",
    "Lookout",
    "Preacher",
    "Shade",
    "Zealot"
]

ALIGNMENT = [
    "Apathetic",
    "Anarchic",
    "Commercial",
    "Philanthropic",
    "Political",
    "Religious",
    "Social"
]

class Adventurer:

    all = {}

    def __init__(self, name, alignment, job, level, group_id, id=None):
        self.id = id
        self.name = name
        self.job = job
        self.alignment = alignment
        self.level = level
        self.group_id = group_id

    def __repr__(self):
        name_ = f"Adventurer {self.id}: {self.name}"
        job_ = f"Job: {self.job} |{self.level}|"   
        alignment_ = f"Alignment: {self.alignment}"
        group_ = f"Group:({self.group_id}) {Group.get_by_id(self.group_id).name}"
        def pick_length():
            if len(name_) >= len(job_) and len(name_) >= len(alignment_) and len(name_) >= len(group_):
                return "_" * len(name_)
            if len(job_) >= len(alignment_) and len(job_) >= len(group_):
                return "_" * len(job_)
            if len(alignment_) >= len(group_):
                return "_" * len(alignment_)
            return "_" * len(group_)
        return f"{pick_length()}\n{name_}\n{job_}\n{alignment_}\n{group_}\n{pick_length()}"
    
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
    def alignment(self):
        return self._alignment
    
    @alignment.setter
    def alignment(self, alignment):
        if alignment.capitalize() in ALIGNMENT:
            self._alignment = alignment.capitalize()
        else:
            raise ValueError(f"{alignment.capitalize()} is not a valid alignment.")
    
    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self, job):
        if job.capitalize() in JOB:
            self._job = job.capitalize()
        else:
            raise ValueError(f"{job.capitalize()} is not a valid job.")
        
    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, level):
        if isinstance(level, int) and (0 < level <= 20):
            self._level = level
        else:
            raise ValueError(f"Level must be a number between 1 and 20. (provided {level})")
        
    @property
    def group_id(self):
        return self._group_id
    
    @group_id.setter
    def group_id(self, group_id):
        if Group.get_by_id(group_id) and (Group.get_by_id(group_id).members < 4):
            Group.get_by_id(group_id).members += 1
            self._group_id = group_id
        else:
            raise ValueError("Full Group or Invalid Group ID#")
    
    # Creating, Deleting, and Saving the Table
    @classmethod
    def make_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS adventurers (
        id INTEGER PRIMARY KEY,
        name TEXT,
        alignment TEXT,
        job TEXT,
        level INTEGER,
        group_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def remove_table(cls):
        sql = """
        DROP TABLE IF EXISTS adventurers;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save_new_row(self):
        sql = """
        INSERT INTO adventurers (name, alignment, job, level, group_id)
        VALUES(?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.alignment, self.job, self.level, self.group_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    #==================================
    # CRUD for the SQL Database
    @classmethod
    def create(cls, name, alignment, job, level, group_id):
        adv = cls(name, alignment, job, level, group_id)
        adv.save_new_row()
        return adv
    
    def update(self):
        sql = """
        UPDATE adventurers
        SET name = ?, alignment = ?, job = ?, level = ?, group_id = ?
        """
        CURSOR.execute(sql, (self.name, self.alignment, self.job, self.level, self.group_id))
        CONN.commit()

    def delete(self):
        sql = """
        DELETE FROM adventurers
        WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None
    #==================================
    # Class Methods to Search Adventurer Information
    @classmethod
    def instance_from_database(cls, row):
        adv = cls.all.get(row[0])
        if adv:
            adv.name = row[1]
            adv.alignment = row[2]
            adv.job = row[3]
            adv.level = row[4]
            adv.group_id = row[5]
        else:
            adv = cls(row[1], row[2], row[3], row[4], row[5])
            adv.id = row[0]
            cls.all[adv.id] = adv
        return adv
    
    @classmethod
    def get_all(cls):
        sql = """
        SELECT *
        FROM adventurers
        """
        database = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_database(n) for n in database]
    
# for n in Adventurer.get_all():
#     print(n)