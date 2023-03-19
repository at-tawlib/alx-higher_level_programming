#!/usr/bin/python3
"""
Change the name of the State where id = 2 to New Mexico
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """
    script takes 3 arguments: mysql username, mysql password and database name
    script should connect to a MySQL server running on localhost at port 3306
    Change the name of the State where id = 2 to New Mexico
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    session.commit()
    session.close()
