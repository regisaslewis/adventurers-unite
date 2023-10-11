from group import Group
from adventurer import Adventurer
import string
import re

pattern = r"[^\W0-9\s]*([^\W0-9]+[\.\,!?]{0,1}[\s'\-]{0,1})+[!?]{0,1}[^\s\W]*"
regex = re.compile(pattern)


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
        print(f"{len(groups)} {'Group' if len(groups) == 1 else 'Groups'} founded on {continent.capitalize()}.")
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
        print(f"{len(groups)} {'Group' if len(groups) == 1 else 'Groups'} founded in {string.capwords(city)}.")
        for n in groups:
            print(n)
    else:
        print(f'Error: No Groups founded in "{string.capwords(city)}".')

def show_adventurers_by_alignment():
    print("Choose Alignment:")
    alignment = alignment_submenu()
    advs = Adventurer.get_alignment(alignment.capitalize())
    if len(advs) > 0:
        print(f'{len(advs)} {"Adventurer is" if len(advs) == 1 else "Adventurers are"} of the "{alignment.capitalize()}" alignment.')
        for n in advs:
            print(n)
    else:
        print(f'Error: No "{alignment.capitalize()}" Adventurers found.')

def show_adventurers_by_job():
    print("Choose Job:")
    job = job_submenu()
    advs = Adventurer.get_job(job.capitalize())
    if len(advs) > 0:
        print(f'{len(advs)} {"Adventurer is a" if len(advs) == 1 else "Adventurers are"} "{job.capitalize()}{"" if len(advs) == 1 else "s"}."')
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
        test_name(name)
        group = Group.create(name, continent, city)
        print(f"{group}\nFOUNDED")
    except Exception as exc:
        print(f"Error: Group could not be founded: {exc}")
    
def make_adventurer():
    print("Select Group to join:")
    group_id = group_id_submenu()
    try:
        if len(Group.get_by_id(group_id).get_members()) < 4:
            name = input("Adveturer's Name: ")
            test_name(name)
            print("Character Alignment:")
            alignment = alignment_submenu()
            print("Job:")
            job = job_submenu()
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
            test_name(name)
            if name.upper() != Group.get_by_id(id_).name.upper():
                if name.upper() in [n.name.upper() for n in Group.get_all()]:
                    raise ValueError("Name is already taken.")
            print(f"New home continent (prev: {group.continent}): ")
            continent = continent_submenu()
            print(f"New founding city (prev: {group.city}): ")
            city = city_submenu(continent)
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
            alignment = alignment_submenu()
            print(f"New job (prev: {adv.job}): ")
            job = job_submenu()
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
    if int(cont_choice) > 0:
        return continents[int(cont_choice) - 1]
    else:
        raise ValueError("Not an option.")

def city_submenu(continent):
    cities = [n for n in Group.CONTINENT[continent]]
    for n in cities:
        print(f"{cities.index(n) + 1}: {n}")
    city_choice = input("=}====> ")
    if int(city_choice) > 0:
        return cities[int(city_choice) - 1]
    else:
        raise ValueError("Not an option.")

def alignment_submenu():
    for n in Adventurer.ALIGNMENT:
        print(f"{Adventurer.ALIGNMENT.index(n) + 1}: {n}")
    align_choice = input("=}====> ")
    if int(align_choice) > 0:
        return Adventurer.ALIGNMENT[int(align_choice) - 1]
    else:
        raise ValueError("Not an option.")

def job_submenu():
    for n in Adventurer.JOB:
        print(f"{Adventurer.JOB.index(n) + 1}: {n}")
    job_choice = input("=}====> ")
    if int(job_choice) > 0:
        return Adventurer.JOB[int(job_choice) - 1]
    else:
        raise ValueError("Not an option.")

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
    if regex.fullmatch(name):
        pass
    else:
        raise ValueError("Name structure not accepted.")