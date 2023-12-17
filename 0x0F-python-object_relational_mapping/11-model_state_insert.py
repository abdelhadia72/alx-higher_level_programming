#!/usr/bin/python3
"""
    script that adds the State object
    “Louisiana” to the database hbtn_0e_6_usa
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from model_state import State, Base


Base = declarative_base()

if __name__ == "__main__":
    from sqlalchemy import create_engine
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    ), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    toAdd = State(name='Louisiana')
    session.add(toAdd)
    session.commit()
    print(toAdd.id)
    session.close()
