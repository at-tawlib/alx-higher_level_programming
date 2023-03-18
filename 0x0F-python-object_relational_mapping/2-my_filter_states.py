#!/usr/bin/python3
"""takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    the script should take 4 arguments: mysql username, mysql password,
    database name and state name searched (no argument validation needed)
    results must be sorted in ascending order by states.id
    """
    host = "localhost"
    port = 3306
    user = argv[1]
    password = argv[2]
    database_name = argv[3]
    name = argv[4]

    connection = MySQLdb.connect(host, user, password, database_name, port)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
                   ORDER BY id".format(name))
    rows = cursor.fetchall()
    connection.close()

    for row in rows:
        print(row)
