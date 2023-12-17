#!/usr/bin/python3
"""
Script that prints all City objects from the database
"""
from model_city import City, Base
from model_state import State
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    data = (session.query(State.name, City.id, City.name)
            .filter(State.id == City.state_id).order_by(City.id))
    for isinstance in data:
        print(isinstance[0] + ": (" + str(isinstance[1]) + ") "
              + str(isinstance[2]))
    session.close()
