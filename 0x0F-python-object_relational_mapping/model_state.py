#!/usr/bin/python3
"""
python file that contains the class definition
of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class inherits from Base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    from sqlalchemy import create_engine
    import sys
    ur = sys.argv[1]
    ps = sys.argv[2]
    db = sys.argv[2]
    p = 3306
    pool_pre_ping = True
    pn = pool_pre_ping
    engine = create_engine(f'mysql+mysqldb://{ur}:{ps}@localhost:{p}/{db}', pn)

    Base.metadata.create_all(engine)
