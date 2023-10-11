from group import Group
from adventurer import Adventurer
import string
import re

name_pattern = r"[^\W0-9\s]*([^\W0-9]+[\.\,!?]?[\s'\-]?)+[^\s\W]+"
group_pattern = r"[^\W0-9\s]*([^\W0-9]+[\.\,!?]?[\s'\-]?)+[^\s\W]+[!?]?"
name_regex = re.compile(name_pattern)
group_regex = re.compile(group_pattern)

def exit_cli():
    print("Closing the Program...")
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
    name = input("Group name (case sensitive): ")
    group = Group.get_by_name(name)
    print(group) if group else print(f'Group "{name}" not found.')

def show_adventurer_by_name():
    name = input("Adventurer's name (case sensitive): ")
    adv = Adventurer.get_by_name(name)
    print(adv) if adv else print(f'"{name}" not found.')

def show_groups_by_continent():
    print("Choose Continent:")
    continent = selection_submenu(Group.CONTINENT)
    groups = Group.get_continent(continent.capitalize())
    if len(groups) > 0:
        print(f"{len(groups)} {'Group' if len(groups) == 1 else 'Groups'} founded on {continent.capitalize()}.")
        for n in groups:
            print(n)
    else:
        print(f'Error: No Groups founded on {continent.capitalize()}')

def show_groups_by_city():
    print("Choose Continent:")
    continent = selection_submenu(Group.CONTINENT)
    print("Choose City:")
    city = selection_submenu(Group.CONTINENT[continent])
    groups = Group.get_city(string.capwords(city))
    if len(groups) > 0:
        print(f"{len(groups)} {'Group' if len(groups) == 1 else 'Groups'} founded in {string.capwords(city)}.")
        for n in groups:
            print(n)
    else:
        print(f'Error: No Groups founded in {string.capwords(city)}.')

def show_adventurers_by_alignment():
    print("Choose Alignment:")
    alignment = selection_submenu(Adventurer.ALIGNMENT)
    advs = Adventurer.get_alignment(alignment.capitalize())
    if len(advs) > 0:
        print(f'{len(advs)} {"Adventurer is" if len(advs) == 1 else "Adventurers are"} of the "{alignment.capitalize()}" alignment.')
        for n in advs:
            print(n)
    else:
        print(f'Error: No "{alignment.capitalize()}" Adventurers found.')

def show_adventurers_by_job():
    print("Choose Job:")
    job = selection_submenu(Adventurer.JOB)
    advs = Adventurer.get_job(job.capitalize())
    if len(advs) > 0:
        print(f'{len(advs)} {"Adventurer is a" if len(advs) == 1 else "Adventurers are"} "{job.capitalize()}{"" if len(advs) == 1 else "s"}."')
        for n in advs:
            print(n)
    else:
        print(f'Error: No {job.capitalize()}s found.')

def make_group():
    try:
        name = input("Group's name: ")
        test_group_name(name)
        print("Home Continent: ")
        continent = selection_submenu(Group.CONTINENT)
        print("Founding City:")
        city = selection_submenu(Group.CONTINENT[continent])
        group = Group.create(name, continent, city)
        print(f"{group}\nFOUNDED")
    except Exception as exc:
        print(f"Group could not be founded: {exc}")
    
def make_adventurer():
    print("Select Group to join:")
    group_id = group_id_submenu()
    try:
        if len(Group.get_by_id(group_id).get_members()) < 4:
            name = input("Adveturer's Name: ")
            test_name(name)
            print("Character Alignment:")
            alignment = selection_submenu(Adventurer.ALIGNMENT)
            print("Job:")
            job = selection_submenu(Adventurer.JOB)
            level = input("Level (1 - 20): ")
        else:
            raise ValueError(f'{Group.get_by_id(group_id).name} is already full!')
        adv = Adventurer.create(name, alignment, job, int(level), int(group_id))
        print(f"{adv}\nCREATED")
    except Exception as exc:
        print(f"Adventurer could not be created: {exc}")

def update_group():
    print("Choose Group:")
    id_ = group_id_submenu()
    if group := Group.get_by_id(id_):
        try:
            name = input(f"New name (prev: {group.name}): ")
            test_group_name(name)
            if name.upper() != Group.get_by_id(id_).name.upper():
                if name.upper() in [n.name.upper() for n in Group.get_all()]:
                    raise ValueError("Name is already taken.")
            print(f"New home continent (prev: {group.continent}): ")
            continent = selection_submenu(Group.CONTINENT)
            print(f"New founding city (prev: {group.city}): ")
            city = selection_submenu(Group.CONTINENT[continent])
            group.name = name
            group.continent = continent
            group.city = city
            group.update()
            print(f"{group}\nUPDATED")
        except Exception as exc:
            print(f"Group not updated: {exc}")
    else:
        print(f"Error: Group {id_} not found.")

def update_adventurer():
    full_groups = [n.id for n in Group.get_all() if n.is_full()]
    print("Choose Adventurer:")
    id_ = adv_id_submenu()
    if adv := Adventurer.get_by_id(id_):
        try:
            print(f"New Group ID# (prev: ({Group.get_by_id(adv.group_id).id}) {Group.get_by_id(adv.group_id).name}): ")
            group_id = group_id_submenu()
            if Group.get_by_id(group_id):
                pass
            else:
                raise ValueError("Group does not exist.")
            if int(group_id) in full_groups:
                raise ValueError(f'Group ({Group.get_by_id(group_id).id}) "{Group.get_by_id(group_id).name}" is already full.')
            name = input(f"New name (prev: {adv.name}): ")
            if name.upper() != Adventurer.get_by_id(id_).name.upper():
                if name.upper() in [n.name.upper() for n in Adventurer.get_all()]:
                    raise ValueError("Name is already taken.")
            test_name(name)
            print(f"New alignment (prev: {adv.alignment}): ")
            alignment = selection_submenu(Adventurer.ALIGNMENT)
            print(f"New job (prev: {adv.job}): ")
            job = selection_submenu(Adventurer.JOB)
            level = input(f"New level (prev: {adv.level}): ")
            adv.name = name
            adv.group_id = group_id
            adv.alignment = alignment
            adv.job = job
            adv.level = int(level)
            adv.update()
            print(f"{adv}\nUPDATED")
        except Exception as exc:
            print(f"Adventurer not updated: {exc}")
    else:
        print(f"Adventurer {id_} not found.")

def delete_group():
    warning = input("Warning: this will delete all members as well.  Continue? (Y/N): ").upper()
    if warning == "Y" or warning == "YES":
        print("Choose Group:")
        id_ = group_id_submenu()
        if group := Group.get_by_id(id_):
            for n in Group.get_by_id(id_).get_members():
                print(f"Deleting {n.name}....")
                n.delete()
            print(f"Deleting {group.name}....")
            group.delete()
            print(f"Group {id_} deleted.")
        else:
            print(f"Group {id_} not found.")
    elif warning == "N" or warning == "NO":
        print("Deletion Cancelled.")
    else:
        print("Command not recognized.")

def delete_adventurer():
    print("Choose Adventurer:")
    id_ = adv_id_submenu()
    if adv := Adventurer.get_by_id(id_):
        print(f"Deleting {adv.name}...")
        adv.delete()
        print(f"Adventurer {id_} deleted.")
    else:
        print(f"Adventurer {id_} not found.")

def show_adventurers_by_group():
    print("Choose Group:")
    id_ = group_id_submenu()
    if group := Group.get_by_id(id_):
        for n in group.get_members():
            print(n)
    else:
        print(f"Group {id_} not found.")

def selection_submenu(class_constant):
    list = [n for n in class_constant]
    for n in list:
        print(f"{list.index(n) + 1}: {n}")
    list_choice = input("=}====> ")
    if 0 < int(list_choice) <= len(list):
        return list[int(list_choice) - 1]
    else:
        raise ValueError(list_choice, "is not an option.")

def adv_id_submenu():
    for n in Adventurer.get_all():
        print(f"{n.id}: {n.name}")
    adv_choice = input("=}====> ")
    return adv_choice

def group_id_submenu():
    for n in Group.get_all():
        print(f"{n.id}: {n.name} [{len(Group.get_by_id(n.id).get_members())}/4]")
    group_choice = input("=}====> ")
    return group_choice
    
def test_name(name):
    if name_regex.fullmatch(name):
        pass
    else:
        raise ValueError("Name structure not accepted.")

def test_group_name(name):
    if group_regex.fullmatch(name):
        pass
    else:
        raise ValueError("Group name structure not accepted.")