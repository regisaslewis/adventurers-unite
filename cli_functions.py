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
    print("Choose Continent:")
    continent = continent_submenu()
    groups = Group.get_continent(continent.capitalize())
    if len(groups) > 0:
        for n in groups:
            print(n)
    else:
        print(f'Error: No Groups founded on "{continent.capitalize()}"')

def show_groups_by_city():
    print("Choose Continent:")
    continent = continent_submenu()
    print("Choose City:")
    city = city_submenu(continent)
    groups = Group.get_city(string.capwords(city))
    if len(groups) > 0:
        for n in groups:
            print(n)
    else:
        print(f'Error: No Groups founded in "{string.capwords(city)}".')

def show_adventurers_by_alignment():
    print("Choose Alignment:")
    alignment = alignment_submenu()
    advs = Adventurer.get_alignment(alignment.capitalize())
    if len(advs) > 0:
        for n in advs:
            print(n)
    else:
        print(f'Error: No "{alignment.capitalize()}" Adventurers found.')

def show_adventurers_by_job():
    print("Choose Job:")
    job = job_submenu()
    advs = Adventurer.get_job(job.capitalize())
    if len(advs) > 0:
        for n in advs:
            print(n)
    else:
        print(f'Error: No "{job.capitalize()}s" found.')


def make_group():
    name = input("Group's name: ")
    print("Home Continent: ")
    continent = continent_submenu()
    print("Founding City:")
    city = city_submenu(continent)
    try:
        group = Group.create(name, continent, city)
        print(f"{group}\nFOUNDED")
    except Exception as exc:
        print(f"Error: Group could not be founded: {exc}")
    
def make_adventurer():
    name = input("Name: ")
    print("Character Alignment:")
    alignment = alignment_submenu()
    print("Job:")
    job = job_submenu()
    level = input("Level (1 - 20): ")
    print("Select Group:")
    group_id = group_id_submenu()
    if len(Group.get_by_id(group_id).get_members()) < 4:
        try:
            adv = Adventurer.create(name, alignment, job, int(level), int(group_id))
            print(f"{adv}\nCREATED")
        except Exception as exc:
            print(f"Adventurer could not be created: {exc}")
    else:
        print(f'Error: Group "{Group.get_by_id(group_id).name}" is already full!')

def update_group():
    print("Choose Group:")
    id_ = group_id_submenu()
    if group := Group.get_by_id(id_):
        try:
            name = input(f"New name (prev: {group.name}): ")
            if name.upper() != Group.get_by_id(id_).name.upper():
                if name.upper() in [n.name.upper() for n in Group.get_all()]:
                    raise ValueError("Name is already taken.")
            group.name = name
            print(f"New home continent (prev: {group.continent}): ")
            continent = continent_submenu()
            group.continent = continent
            print(f"New founding city (prev: {group.city}): ")
            city = city_submenu(continent)
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
            name = input(f"New name (prev: {adv.name}): ")
            if name.upper() != Adventurer.get_by_id(id_).name.upper():
                if name.upper() in [n.name.upper() for n in Adventurer.get_all()]:
                    raise ValueError("Name is already taken.")
            adv.name = name
            print(f"New alignment (prev: {adv.alignment}): ")
            alignment = alignment_submenu()
            adv.alignment = alignment
            print(f"New job (prev: {adv.job}): ")
            job = job_submenu()
            adv.job = job
            level = input(f"New level (prev: {adv.level}): ")
            adv.level = int(level)
            print(f"New Group ID# (prev: ({Group.get_by_id(adv.group_id).id}) {Group.get_by_id(adv.group_id).name}): ")
            group_id = group_id_submenu()
            if Group.get_by_id(group_id):
                adv.group_id = group_id
            else:
                raise ValueError("Group does not exist.")
            if int(group_id) in full_groups:
                raise ValueError(f'Group ({Group.get_by_id(group_id).id}) "{Group.get_by_id(group_id).name}" is full.')
            adv.update()
            print(f"{adv}\nUPDATED")
        except Exception as exc:
            print(f"Adventurer not updated: {exc}")
    else:
        print(f"Adventurer {id_} not found.")

def delete_group():
    warning = input("Warning: this will delete all members as well.  Continue? (Y/N): ")
    if warning == "y" or warning == "Y":
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
    elif warning == "n" or warning == "N":
        print("Delete Cancelled.")
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

def continent_submenu():
    continents = [n for n in Group.CONTINENT]
    for n in continents:
        print(f"{continents.index(n) + 1}: {n}")
    cont_choice = input("=}====> ")
    try:
        return continents[int(cont_choice) - 1]
    except:
        raise ValueError("Not an option.")

def city_submenu(continent):
    cities = [n for n in Group.CONTINENT[continent]]
    for n in cities:
        print(f"{cities.index(n) + 1}: {n}")
    city_choice = input("=}====> ")
    try:
        return cities[int(city_choice) - 1]
    except Exception as exc:
        raise ValueError("Not an option.")

def alignment_submenu():
    for n in Adventurer.ALIGNMENT:
        print(f"{Adventurer.ALIGNMENT.index(n) + 1}: {n}")
    align_choice = input("=}====> ")
    try:
        return Adventurer.ALIGNMENT[int(align_choice) - 1]
    except:
        raise ValueError("Not an option.")

def job_submenu():
    for n in Adventurer.JOB:
        print(f"{Adventurer.JOB.index(n) + 1}: {n}")
    job_choice = input("=}====> ")
    try:
        return Adventurer.JOB[int(job_choice) - 1]
    except:
        raise ValueError("Not an option.")

def adv_id_submenu():
    for n in Adventurer.get_all():
        print(f"{n.id}: {n.name}")
    adv_choice = input("=}====> ")
    try:
        return adv_choice
    except:
        raise ValueError("Not an option.")

def group_id_submenu():
    for n in Group.get_all():
        print(f"{n.id}: {n.name} [{len(Group.get_by_id(n.id).get_members())}/4]")
    group_choice = input("=}====> ")
    try:
        return group_choice
    except:
        raise ValueError("Not an option.")