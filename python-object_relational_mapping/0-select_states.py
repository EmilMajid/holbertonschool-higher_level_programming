#!/usr/bin/python3
"""
This script connects to a MySQL database and lists all states
from the 'states' table in the specified database, ordered 
by id in ascending order.
It takes three command-line arguments: username, password, and database name.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    # Create a cursor object
    cursor = db.cursor()
    # Execute the query to select all states, ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    # Fetch all rows
    rows = cursor.fetchall()
    # Print each row
    for row in rows:
        print(row)
    # Close cursor and database connection
    cursor.close()
    db.close()
