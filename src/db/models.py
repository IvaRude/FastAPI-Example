from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Unit(Base):
    __tablename__ = 'units'

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('units.id'), nullable=True)
    name = Column(String, nullable=False)
    price = Column(Integer)
    is_deleted = Column(Boolean, nullable=False)
