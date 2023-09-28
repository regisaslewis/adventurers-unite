from __init__ import CONN, CURSOR
from group import Group
from adventurer import Adventurer

def seed_sample():
    Group.remove_table()
    Adventurer.remove_table()
    Group.make_table()
    Adventurer.make_table()
    Group.create("The Party of Ala", "Jidoth", "Lord's Port")
    Group.create("Becco", "Mollen", "len city")
    Group.create("Ciolta's Lookouts", "RISE", "expanse")
    Group.create("The Destructors", "Mollen", "vanna's perch")
    Group.create("Ergo, Goodness", "Mollen", "Len City")
    Group.create("Fantico", "Mollen", "The Villages of Southern Aldon")
    Group.create("Golemite", "Bettle", "Lei")
    Group.create("Hellions Risen", "Rise", "Mouth")

    Adventurer.create("adam", "social", "preacher", 12, 2)
    Adventurer.create("Banderax", "PHILANTHROPIC", "FeRaL", 20, 1)
    Adventurer.create("Collest", "Religious", "HopeLess", 18, 1)
    Adventurer.create("Duotim Penrose IV", "Political", "director", 10, 1)
    Adventurer.create("Ed G.G. Lodo", "Anarchic", "lookout", 3, 3)
    Adventurer.create("Franky", "Apathetic", "Zealot", 12, 1)
    Adventurer.create("Glo", "Commercial", "Director", 1, 8)
    Adventurer.create("Helena Forsyth", "Social", "Director", 8, 5)
    Adventurer.create("Inicio", "social", "preacher", 14, 5)
    


seed_sample()
print("Example Groups seeded.")
print("Example Adventurers seeded.")