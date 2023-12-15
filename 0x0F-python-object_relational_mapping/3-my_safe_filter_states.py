#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        exit(1)

    username, password, database, keyword = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s", (keyword,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()