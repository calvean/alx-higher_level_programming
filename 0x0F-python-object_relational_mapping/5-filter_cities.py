#!/usr/bin/python3
"""
takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
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
    stat = """SELECT cities.name
                 FROM cities, states
                 WHERE BINARY states.name = %s
                 AND cities.state_id = states.id
                 ORDER BY cities.id ASC"""
    c.execute(stat, (argv[4],))
    all_rows = cur.fetchall()
    print(", ".join(row[0] for row in all_rows))
    c.close()
    db.close()
