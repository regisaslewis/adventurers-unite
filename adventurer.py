from __init__ import CURSOR, CONN
from group import Group

class Adventurer:

    all = {}

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
        "Philanthropical",
        "Political",
        "Religious",
        "Social"
    ]

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
            if len(name_) > len(job_) and len(name_) > len(alignment_):
                return "_" * len(name_)
            if len(job_) > len(alignment_):
                return "_" * len(job_)
            return "_" * len(alignment_)
        return f"{name_}\n{job_}\n{alignment_}\nGroup ID: {self.group_id}\n{pick_length()}"
    
ted = Adventurer("Ted", "Social", "Preacher", 11, 2, 1)
marta = Adventurer("Marta", "Philanthropical", "Feral", 11, 3, 2)
allendiuminiolle = Adventurer("Allen Diumini Olle", "Commercial", "Director", 17, 2, 3)
print(ted)
print(marta)
print(allendiuminiolle)