#!/usr/bin/python3
"""prints the first state object in the database"""
import sys
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
           sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sess = Session()
    first_state = sess.query(State).order_by(State.id).first()
    if first_state:
        print(first_state.id, first_state.name, sep=": ")
    else:
        print("Nothing")
