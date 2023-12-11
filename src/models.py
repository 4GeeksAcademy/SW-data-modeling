import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Characters(Base):
    __tablename__='Characters'
    id = Column(Integer, primary_key = True)
    name = Column(String(250))
    eye_color = Column(String(250))
    height = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))


class Planets(Base):
    __tablename__= 'Planets'
    id = Column(Integer, primary_key = True)
    name = Column(String(250))
    climate = Column(String(250))
    terrain = Column(String(250))
    population = Column(Integer)
    diameter = Column(Integer)



class Vehicles(Base):
    __tablename__ = "Vehicles"
    id = Column(Integer, primary_key = True)
    name = Column(String(250))
    model = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(Integer)
    Crew = Column(Integer)

class Favorites(Base):
    __tablename__ = 'Favorites'
    id = Column(Integer, primary_key = True)
    favorite_id = Column(Integer, )
    name = Column(String(250))

class User(Base):
    __tablename__ = 'User'
    user = Column (String(25), primary_key=True, nullable = False)
    email = Column(String(250))
    password = Column(String(30), nullable=False)
    favorite_planets = relationship('Planets', )
    favorite_characters = relationship('Character')
    favorite_vehicles = relationship('Vehicles')



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
