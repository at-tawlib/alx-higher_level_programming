#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    """
    script takes 4 arguments: mysql username, mysql password, database name
    and state name (SQL injection free!)
    script connects to a MySQL server running on localhost at port 3306
    Results sorted in ascending order by cities.id
    execute() used only once
    """

    host = "localhost"
    port = 3306
    user = argv[1]
    password = argv[2]
    database_name = argv[3]
    name = argv[4]

    connection = MySQLdb.connect(host, user, password, database_name, port)
    cursor = connection.cursor()
    cursor.execute("SELECT cities.name FROM cities JOIN states WHERE \
            cities.state_id = states.id  and states.name LIKE BINARY %s\
            ORDER BY cities.id ASC; ", (name, ))

    rows = cursor.fetchall()
    connection.close()

    for row in rows:
        if row == rows[-1]:
            print(row[0], end=" ")
        else:
            print(row[0], end=", ")
    print()
