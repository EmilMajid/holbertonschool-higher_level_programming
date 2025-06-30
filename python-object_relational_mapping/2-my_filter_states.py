#!/usr/bin/python3
"""
Script that lists all states with a name matching the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1],
    password = sys.argv[2],
    db_name = sys.argv[3],
    state_name = sys.argv[4]
    db = MySQLdb.connect
    (host="localhost",
    port=3306,
    user=username,
    passwd=password,
    db=db_name)
    cur = db.cursor()
    q = ("SELECT * FROM states WHERE name = '{}' "
     "ORDER BY id ASC".format(state_name))
    cur.execute(q)
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    db.close()
    