#!/usr/bin/python3
"""
scripts that list all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    script takes 3 arguments: mysql username, mysql password and database name
    script connects to a MySQL server running on localhost at port 3306
    Results sorted in ascending order by cities.id
    execute() used only once
    """
    host = "localhost"
    port = 3306
    user = argv[1]
    password = argv[2]
    database_name = argv[3]

    connection = MySQLdb.connect(host, user, password, database_name, port)
    cursor = connection.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
            JOIN states WHERE cities.state_id = states.id \
            ORDER BY cities.id ASC; ")

    rows = cursor.fetchall()
    connection.close()

    for row in rows:
        print(row)
