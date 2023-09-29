from group import Group
from adventurer import Adventurer

def exit_cli():
    print("LEAVING INTERFACE")
    exit()

def show_all_groups():
    for n in Group.get_all():
        print(n)

def show_all_adventurers():
    for n in Adventurer.get_all():
        print(n)

def show_group_by_id():
    id_ = input("Enter Group's ID: ")
    group = Group.get_by_id(id_)
    print(group) if group else print(f"Group {id_} not found.")

def show_adventurer_by_id():
    id_ = input("Enter Adventurer's ID: ")
    adv = Adventurer.get_by_id(id_)
    print(adv) if adv else print(f"Adventurer {id_} not found.")

def show_group_by_name():
    name = input("Group name: ")
    group = Group.get_by_name(name)
    if group:
        if group.name.lower() == name.lower():
            print(group)
    else:
        print(f'Group "{name}" not found.')



def make_group():
    name = input("Group's name: ")
    continent = input("Home continent: ")
    city = input("Founding city: ")
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

def update_group():
    id_ = input("Group's ID#: ")
    if group := Group.get_by_id(id_):
        try:
            name = input(f"New name (prev {group.name}): ")
            group.name = name
            continent = input(f"New home continent (prev {group.continent}): ")
            group.continent = continent
            city = input(f"New founding city (prev {group.city}): ")
            group.city = city
            group.update()
            print(f"{group}\nUPDATED")
        except Exception as exc:
            print(f"Group not updated: {exc}")
    else:
        print(f"Group {id_} not found.")

def update_adventurer():
    id_ = input("Adventurer's ID#: ")
    if adv := Adventurer.get_by_id(id_):
        try:
            name = input(f"New name (prev {adv.name}): ")
            adv.name = name
            alignment = input(f"New alignment (prev {adv.alignment}): ")
            adv.alignment = alignment
            job = input(f"New job (prev {adv.job}): ")
            adv.job = job
            level = input(f"New level (prev {adv.level}): ")
            adv.level = int(level)
            group_id = input(f"New Group ID# (prev ({Group.get_by_id(adv.group_id).id}) {Group.get_by_id(adv.group_id).name}): ")
            adv.group_id = int(group_id)
            adv.update()
            print(f"{adv}\nUPDATED")
        except Exception as exc:
            print(f"Adventurer not updated: {exc}")
    else:
        print(f"Adventurer {id_} not found.")

def delete_group():
    warning = input("Warning: this will delete all members as well.  Continue? (Y/N): ")
    if warning == "y" or warning == "Y":
        id_ = input("Group ID#: ")
        if group := Group.get_by_id(id_):
            for n in Group.get_by_id(id_).get_members():
                print(f"Deleting {n.name}....")
                n.delete()
            print(f"Deleting {group.name}....")
            group.delete()
            print(f"Group {id_} deleted.")
        else:
            print(f"Group {id_} not found.")
    elif warning == "n" or warning == "N":
        print("Delete Cancelled.")
    else:
        print("Command not recognized.")

def del_adventurer():
    id_ = input("Adventurer's ID#: ")
    if adv := Adventurer.get_by_id(id_):
        print(f"Deleting {adv.name}...")
        Group.get_by_id(adv.group_id).members -= 1
        adv.delete()
        print(f"Adventure {id_} deleted.")
    else:
        print(f"Adventurer {id_} not found.")


# show_all_adventurers()
# show_all_groups()
# show_adventurer_by_id()
# show_group_by_id()
show_group_by_name()
# make_group()
# make_adventurer()
# update_group()
# update_adventurer()
# delete_group()
# del_adventurer()