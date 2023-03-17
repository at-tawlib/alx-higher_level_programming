#!/usr/bin/python3
"""list all states from database hbtn_0e_0_usa"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ connects to the hbtn_0e_0_usa database and gets
    all states in sorted ascending order by states.id"""

    host = "localhost"
    port = 3306
    user = argv[1]
    password = argv[2]
    database_name = argv[3]

    connection = MySQLdb.connect(host, user, password, database_name, port)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id;")
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    connection.close()
