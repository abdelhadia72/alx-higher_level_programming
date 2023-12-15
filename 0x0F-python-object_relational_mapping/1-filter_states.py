#!/usr/bin/python3

'''
    script that lists all states with a name starting
    with N (upper N) from the database hbtn_0e_0_usa:
'''

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1].startswith("N"):
            print(row)
    cur.close()
    db.close()
