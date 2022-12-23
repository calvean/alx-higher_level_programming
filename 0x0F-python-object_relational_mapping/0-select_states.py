#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    a = db.cursor()
    a.execute("SELECT * FROM `states`")
    [print(state) for state in a.fetchall()]
