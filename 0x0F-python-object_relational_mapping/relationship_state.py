#!/usr/bin/python3
"""
python file that contains the class definition
of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from relationship_city import Base


class State(Base):
    """State class inherits from Base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    def __repr__(self):
        return f"{self.id}: {self.name}"


if __name__ == "__main__":
    from sqlalchemy import create_engine
    import sys
    ur = sys.argv[1]
    ps = sys.argv[2]
    db = sys.argv[3]
    p = 3306
    pool_pre_ping = True
    pn = True
    engine = create_engine(f'mysql+mysqldb://{ur}:{ps}@localhost:{p}/{db}', pn)

    Base.metadata.create_all(engine)
