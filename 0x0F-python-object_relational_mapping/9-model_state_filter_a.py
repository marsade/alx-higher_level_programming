#!/usr/bin/python3
"""lists all states objects that contain the letter a """
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
    for instance in sess.query(State).order_by(State.id).filter(
                                    State.name.like("%a%")):
        print(instance.id, instance.name, sep=": ")
