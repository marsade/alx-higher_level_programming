#!/usr/bin/python3
"""lists all states objects that contain the letter a """
import sys
from model_state import State, Base
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
       sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sess = Session()
    for instance in (sess.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id)):
        print(instance[0] + ": (" + str(instance[1]) + ") " + instance[2])
