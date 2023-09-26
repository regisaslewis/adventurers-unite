import sqlite3

CONN = sqlite3.connect("teams.db")
CURSOR = CONN.cursor()