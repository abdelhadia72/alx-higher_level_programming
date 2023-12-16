from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

#Base
Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Person(id={self.id}, name={self.name}, age={self.age})"


class Thing(Base):
    __tablename__ = 'thing'
    tid = Column(Integer, primary_key=True, autoincrement=True)
    descrption = Column(String(145))
    owner = Column(Integer, ForeignKey("people.id"))

    def __init__(self, descrption, owner):
        self.descrption = descrption
        self.owenr = owner

    def __rapr__(self):
        return (f"{self.tid} : {self.descrption} Owed by {self.owenr}")

# create engine
engine = create_engine(f'mysql+mysqldb://root:hello123@localhost:3306/along', pool_pre_ping=True)
Base.metadata.create_all(bind=engine)

# create session
Session = sessionmaker(bind=engine)
session = Session()

# create person
p1 = Person(name='Fin', age=34)
# session.add(person)
# session.commit()

# quraey data
# data = session.query(Person).all()

#? filter
# data = session.query(Person).filter(Person.name == 'John')

#? like
# data = session.query(Person).filter(Person.name.like('%J%'))

#? 
data = session.query(Person).filter(Person.name.like('%J%'))

for d in data:
    print(d)

#! creating new thing

t1 = Thing("Be diff", p1.id)
session.add(t1)
session.commit()