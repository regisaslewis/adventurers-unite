from __init__ import CONN, CURSOR
from group import Group
from adventurer import Adventurer

def seed_sample():
    Group.remove_table()
    Group.make_table()
    Group.create("The Party of Ala", "Jidoth", "Lord's Port")
    Group.create("Becco", "Mollen", "len city")
    Group.create("Ciolta's Lookouts", "RISE", "expanse")
    Group.create("The Destructors", "Mollen", "vanna's perch")
    Group.create("Ergo, Goodness", "Mollen", "Len City")
    Group.create("Fantico", "Mollen", "The Villages of Southern Aldon")