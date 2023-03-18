#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ connets to the hbtn_0e_0_usa database and gets all states
    starting with 'N' sorted in ascending order by states.id"""

    host = "localhost"
    port = 3306
    user = argv[1]
    password = argv[2]
    database_name = argv[3]

    connection = MySQLdb.connect(host, user, password, database_name, port)
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM states WHERE name
            LIKE BINARY 'N%' ORDER BY id;""")
    rows = cursor.fetchall()
    connection.close()

    for row in rows:
        print(row)
