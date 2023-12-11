import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from datetime import datetime
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
  __tablename__ = 'user'
  id = Column(Integer, primary_key=True)
  name = Column(String(25), nullable=False)
  last_name = Column(String(25), nullable=False)
  email = Column(String(250), nullable=False)
  password = Column(String(25), nullable=False)
 
class Planets(Base):
  __tablename__ = 'planets'
  id = Column(Integer, primary_key=True)
  name = Column(String(250), nullable=False)
  diameter = Column(Integer, nullable=False)
  climate = Column(String(250), nullable=True)
  population = Column(Integer, nullable=True)

class Characters(Base):
  __tablename__= 'characters'
  id = Column(Integer, primary_key=True)
  name = Column(String(250), nullable=True)
  eye_color = Column(String(250), nullable=True)
  birth_year= Column(Integer, nullable=True)
  gender = Column(String(250), nullable=True)

class Vehicles(Base):
  __tablename__ = 'vehicles'
  id = Column(Integer, primary_key=True)
  model = Column(String(250), nullable=True)
  length = Column(Integer, nullable=True)
  crew = Column(Integer, nullable=True)
  manufactor = Column(String(250), nullable=True)


class Favorites(Base):
  __tablename__= 'favorites'
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey('user.id'))
  planet_id = Column(Integer, ForeignKey('planets.id'))
  character_id = Column(Integer, ForeignKey('characters.id'))
  vehicles_id = Column(Integer, ForeignKey('vehicles.id'))

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')