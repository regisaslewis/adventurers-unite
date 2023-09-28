from group import Group
from adventurer import Adventurer

def exit_cli():
    print("LEAVING INTERFACE")
    exit()

def all_groups():
    for n in Group.get_all():
        print(n)

def all_adventurers():
    for n in Adventurer.get_all():
        print(n)

def group_by_id():
    id_ = input("Enter Group's ID: ")
    group = Group.get_by_id(id_)
    print(group) if group else print(f"Group {id_} not found.")

def adventurer_by_id():
    id_ = input("Enter Adventurer's ID: ")
    adv = Adventurer.get_by_id(id_)
    print(adv) if adv else print(f"Adventurer {id_} not found.")

def make_group():
    name = input("Enter Group's name: ")
    continent = input("Enter Home Continent: ")
    city = input("Enter Founding City: ")
    try:
        group = Group.create(name, continent, city)
        print(f"{group}\nFOUNDED")
    except Exception as exc:
        print(f"Group could not be founded: {exc}")
    
def make_adventurer():
    name = input("Name: ")
    alignment = input("Alignment: ")
    job = input("Job: ")
    level = input("Level: ")
    group_id = input("Group's ID#: ")
    try:
        adv = Adventurer.create(name, alignment, job, int(level), int(group_id))
        print(f"{adv}\nCREATED")
    except Exception as exc:
        print(f"Adventurer could not be created: {exc}")


# all_adventurers()
# all_groups()
# adventurer_by_id()
# group_by_id()
# make_group()
make_adventurer()