#!/usr/bin/python3
"""
prints all City objects from database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import State, Base


if __name__ == "__main__":
    """
    script should take 3 arguments: mysql username, mysql password and database name
    script should connect to a MySQL server running on localhost at port 3306
    Results must be sorted in ascending order by cities.id
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State).join(State)

    for city, state in cities.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()

