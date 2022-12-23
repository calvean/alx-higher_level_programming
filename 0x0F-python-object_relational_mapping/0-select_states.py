#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    all_rows = cur.fetchall()
    for row in all_rows:
        print(row)
    cur.close()
    db.close()
