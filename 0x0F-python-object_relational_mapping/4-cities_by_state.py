#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""
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
    c = db.cursor()
    stat = """SELECT cities.id, cities.name, states.name
                 FROM cities, states
                 WHERE cities.state_id = states.id
                 ORDER BY cities.id ASC"""
    c.execute(stat)
    all_rows = c.fetchall()
    for row in all_rows:
        print(row)
    c.close()
    db.close()
