import sqlite3

CONN = sqlite3.connect("silowan.db")
CURSOR = CONN.cursor()