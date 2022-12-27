#!/usr/bin/python3
""" Module 3-my_safe_filter_states"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8",
    )
    cur = db.cursor()
    statement = """SELECT *FROM states
    WHERE BINARY states.name = %s ORDER BY states.id ASC"""
    cur.execute(statement, (argv[4],))
    all_rows = cur.fetchall()
    for row in all_rows:
        print(row)
    cur.close()
    db.close()
