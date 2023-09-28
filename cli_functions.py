from classes.group import Group
from classes.adventurer import Adventurer

def exit_cli():
    print("LEAVING INTERFACE")
    exit()

def all_groups():
    for n in Group.get_all():
        print(n)

def groups_by_id():
    id_ = input("Enter the Group's ID: ")
    group = Group.get_by_id(id_)
    print(group) if group else print(f"Group {id_} not found.")


# all_groups()
groups_by_id()