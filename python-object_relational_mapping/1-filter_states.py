#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N) from the database.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    x = db.cursor()
    x.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    rows = x.fetchall()
    for row in rows:
        print(row)
    x.close()
    db.close()
