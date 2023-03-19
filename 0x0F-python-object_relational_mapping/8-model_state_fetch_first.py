#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """
    script takes 3 arguments: mysql username, mysql password and database name
    import State and Base from model_state
    script should connect to a MySQL server running on localhost at port 3306
    state displayed must be the first in states.id
    If the table states is empty, print Nothing followed by a new line
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()

    if state is not None:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")
