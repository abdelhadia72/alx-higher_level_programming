#!/usr/bin/python3
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
Base = declarative_base()

"""
    City class inherits from Base and defines
    id and name and state_id
"""


class City(Base):
    """Module of a city"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
