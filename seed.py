from __init__ import CONN, CURSOR
from group import Group
from adventurer import Adventurer

def seed_sample():
    Group.remove_table()
    Adventurer.remove_table()
    Group.make_table()
    Adventurer.make_table()
    a = Group.create("The Party of Ala", "Jidoth", "Lord's Port")
    b = Group.create("Becco", "Mollen", "len city")
    c = Group.create("Ciolta's Lookouts", "RISE", "expanse")
    d = Group.create("The Destructors", "Mollen", "vanna's perch")
    e = Group.create("Ergo, Goodness", "Mollen", "Len City")
    f = Group.create("Fantico", "Mollen", "The Villages of Southern Aldon")
    g = Group.create("Golemite", "Bettle", "Lei")
    h = Group.create("Hellions Risen", "Rise", "Mouth")

    Adventurer.create("adam", "social", "preacher", 12, b.id)
    Adventurer.create("Banderax", "PHILANTHROPIC", "FeRaL", 20, a.id)
    Adventurer.create("Collest", "Religious", "HopeLess", 18, a.id)
    Adventurer.create("Duotim Penrose IV", "Political", "director", 10, a.id)
    Adventurer.create("Ed G.G. Lodo", "Anarchic", "lookout", 3, c.id)
    Adventurer.create("Franky", "Apathetic", "Zealot", 12, a.id)
    Adventurer.create("Glo", "Commercial", "Director", 1, h.id)
    Adventurer.create("Helena Forsyth", "Social", "Director", 8, g.id)
    Adventurer.create("Inicio", "social", "preacher", 14, e.id)
    


seed_sample()
print("Example Groups seeded.")
print("Example Adventurers seeded.")