from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

"""
    City class inherits from Base and defines 
    id and name and state_id
"""

class City(Base):
    """
    City class that inherits from Base
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
