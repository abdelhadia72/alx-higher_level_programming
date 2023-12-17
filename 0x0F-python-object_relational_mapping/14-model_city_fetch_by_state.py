#!/usr/bin/python3
"""
    script that prints all City objects from the database hbtn_0e_14_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    ), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_cities = session.query(
        State,
        City).filter(
        State.id == City.state_id).order_by(
            City.id).all()

    for state, city in states_cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
