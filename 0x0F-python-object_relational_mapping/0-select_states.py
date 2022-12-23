
#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    import sys

    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user= argv[1],
        passwd= argv[2],
        db= argv[3],
    )
    cur = db.cursor()
    all_rows = cur.fetchall("SELECT * FROM states ORDER BY id ASC")
    for row in all_rows:
        print(row)
    cur.close()
    db.close()
