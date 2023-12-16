#!/usr/bin/python3
"""
python file that contains the class definition
of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class State(Base):
    """State class inherits from Base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return f"{self.id}: {self.name}"


if __name__ == "__main__":
    from sqlalchemy import create_engine
    import sys
    ur = sys.argv[1]
    ps = sys.argv[2]
    db = sys.argv[3]
    p = 3306

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    ), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State).order_by(State.id).all()
    for state in data:
        print(state)
