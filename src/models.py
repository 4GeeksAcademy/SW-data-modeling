import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    user = Column (String(25), nullable = False)
    email = Column(String(250), nullable=False)
    password = Column(String(30), nullable=False)

class Character(Base):
    __tablename__='Character'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable=False)
    eye_color = Column(String(250))
    height = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))


class Planet(Base):
    __tablename__= 'Planet'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250))
    terrain = Column(String(250))
    population = Column(Integer)
    diameter = Column(Integer)

class Vehicle(Base):
    __tablename__ = "Vehicle"
    id = Column(Integer, primary_key = True)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250))
    cost_in_credits = Column(Integer)
    Crew = Column(Integer)

class Favorites(Base):
    __tablename__ = 'Favorites'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=False, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=False, primary_key=True)

    # Relationships
    User.Favorites = relationship("Favorite", back_populates="user")
    Planet.Favorites = relationship("Favorite", back_populates="planet")
    Character.Favorites = relationship("Favorite", back_populates="character")
    Vehicle.Favorites = relationship("Favorite", back_populates="vehicle")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
