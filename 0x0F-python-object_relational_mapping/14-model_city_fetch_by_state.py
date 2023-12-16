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

    city = session.query(State, City).join(City).order_by(City.id)
    for state, city in city:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
