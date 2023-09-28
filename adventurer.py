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
        def pick_length():
            if len(name_) >= len(job_) and len(name_) >= len(alignment_):
                return "_" * len(name_)
            if len(job_) >= len(alignment_):
                return "_" * len(job_)
            return "_" * len(alignment_)
        return f"{pick_length()}\n{name_}\n{job_}\n{alignment_}\nGroup ID: {self.group_id}\n{pick_length()}"
    
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

        
# adam = Adventurer("adam", "social", "preacher", 12, 1, 1)
# print(adam)
# banderax = Adventurer("Banderax", "PHILANTHROPIC", "FeRaL", 20, 1, 2)
# print(banderax)
# collest = Adventurer("Collest", "Religious", "HopeLess", 18, 1, 3)
# print(collest)
# duotim = Adventurer("Duotim Penrose IV", "Political", "director", 10, 1, 4)
# print(duotim)