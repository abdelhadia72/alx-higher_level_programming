#!/usr/bin/python3

'''
    script that takes in an argument and displays
    all values in the states table of
    hbtn_0e_0_usa where name matches the argument
'''

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        exit(1)

    username, password = sys.argv[1], sys.argv[2]
    database, keyword = sys.argv[3], sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}'".format(keyword))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
