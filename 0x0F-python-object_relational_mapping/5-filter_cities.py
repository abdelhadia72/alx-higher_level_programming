#!/usr/bin/python3

"""
    script that takes in the name of a state as an argument
    and lists all cities of that state, using the database
    hbtn_0e_4_usa
"""

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
    cur.execute(
        """
        SELECT cities.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (keyword,)
    )
    query_rows = cur.fetchall()
    list = []
    for row in query_rows:
        list.append(row[0])
    print(', '.join(list))
    cur.close()
    db.close()
