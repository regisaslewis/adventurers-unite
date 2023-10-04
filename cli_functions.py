from group import Group
from adventurer import Adventurer
import string

def exit_cli():
    print("Closing the Program...")
    exit()

def show_all_groups():
    Adventurer.get_all() #included to populate Group.members
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
    name = input("Group name (case sensitive): ")
    group = Group.get_by_name(name)
    print(group) if group else print(f'Group "{name}" not found.')

def show_adventurer_by_name():
    name = input("Adventurer's name (case sensitive): ")
    adv = Adventurer.get_by_name(name)
    print(adv) if adv else print(f'"{name}" not found.')

def show_groups_by_continent():
    continent = input("Continent: ")
    groups = Group.get_continent(continent.capitalize())
    if len(groups) > 0:
        for n in groups:
            print(n)
    else:
        print(f'Error: No Groups founded on "{continent.capitalize()}"')

def show_groups_by_city():
    city = input("City: ")
    groups = Group.get_city(string.capwords(city))
    if len(groups) > 0:
        for n in groups:
            print(n)
    else:
        print(f'Error: No Groups founded in "{string.capwords(city)}".')

def show_adventurers_by_alignment():
    alignment = input("Alignment: ")
    advs = Adventurer.get_alignment(alignment.capitalize())
    if len(advs) > 0:
        for n in advs:
            print(n)
    else:
        print(f'Error: No "{alignment.capitalize()}" Adventurers found.')

def show_adventurers_by_job():
    job = input("Job: ")
    advs = Adventurer.get_job(job.capitalize())
    if len(advs) > 0:
        for n in advs:
            print(n)
    else:
        print(f'Error: No "{job.capitalize()}s" found.')


def make_group():
    name = input("Group's name: ")
    continent = input("Home continent: ")
    city = input("Founding city: ")
    try:
        group = Group.create(name, continent, city)
        print(f"{group}\nFOUNDED")
    except Exception as exc:
        print(f"Error: Group could not be founded: {exc}")
    
def make_adventurer():
    name = input("Name: ")
    alignment = input("Alignment: ")
    job = input("Job: ")
    level = input("Level: ")
    group_id = input("Group's ID#: ")
    if len(Group.get_by_id(group_id).get_members()) < 4:
        try:
            adv = Adventurer.create(name, alignment, job, int(level), int(group_id))
            print(f"{adv}\nCREATED")
        except Exception as exc:
            print(f"Adventurer could not be created: {exc}")
    else:
        print(f'Error: Group "{Group.get_by_id(group_id).name}" is already full!')

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
            print(f"Error: Group not updated: {exc}")
    else:
        print(f"Error: Group {id_} not found.")

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
            print(f"Error: Adventurer not updated: {exc}")
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

def delete_adventurer():
    id_ = input("Adventurer's ID#: ")
    if adv := Adventurer.get_by_id(id_):
        print(f"Deleting {adv.name}...")
        adv.delete()
        print(f"Adventurer {id_} deleted.")
    else:
        print(f"Adventurer {id_} not found.")

def show_adventurers_by_group():
    id_ = input("Group's ID#: ")
    if group := Group.get_by_id(id_):
        for n in group.get_members():
            print(n)
    else:
        print(f"Group {id_} not found.")