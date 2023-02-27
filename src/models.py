import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planets(Base):
    __tablename__ = 'Planets'
    ID = Column(Integer, primary_key=True)
    Name = Column(String(100))
    Rotation = Column(Integer)
    Orbital_Period = Column(Integer)
    Diameter = Column(Integer)
    Climate = Column(String)
    Gravity = Column(Integer)
    Terrain = Column(String)
    Population = Column(Integer, ForeignKey("Species.ID"))
    Residents = Column(String, ForeignKey("People.ID"))
    #Relationship
    People = relationship("People")
    Species = relationship("Species")
    

class People(Base):
    __tablename__ = 'People'
    ID = Column(Integer, primary_key=True)
    Name = Column(String(100))
    Height = Column(Integer)
    Mass = Column(Integer)
    Hair_Color = Column(String(50))
    Eye_color = Column(String(50))
    Birth_year = Column(Integer)
    Homeworld = Column(String(100), ForeignKey("Planets.ID"))
    Starships = Column(String(100), ForeignKey("Starships.ID"))
    #Relationship   
    Planets = relationship("Planets")
    Starships = relationship("Starships")


class Starships(Base):
        __tablename__ = "Starships"
        ID = Column(Integer, primary_key=True)
        Name = Column(String(100))
        Model = Column(String(250))
        Manufacturer = Column(String(250))
        Cost = Column(Integer)
        Length = Column(Integer)
        Max_Speed = Column(Integer)
        Crew = Column(Integer)
        Passengers = Column(Integer)
        Cargo = Column(Integer)
        Speed_Rating = Column(Integer)
        Pilots = Column(String(100), ForeignKey("People.ID"))
        #Relationships
        People = relationship("People")


class Species(Base):
        __tablename__ = "Species"
        ID = Column(Integer, primary_key=True)
        Name = Column(String(100))
        Classification = Column(String(250))
        Designation = Column(String(250))
        Average_Height = Column(Integer)
        Average_Lifespan = Column(Integer)
        Homeworld = Column(String(100), ForeignKey("Planets.ID"))
        Language = Column(String(100))
        People = Column(String(100), ForeignKey("People.ID"))
        #  Relationships
        Planets = relationship("Planets")
        People = relationship("People")

class Habitants_of_Planets(Base):
        __tablename__ = "Habitants of Planets"
        Planet_ID = Column(Integer, ForeignKey("Planets.ID"), primary_key=True)
        People_ID = Column(Integer, ForeignKey("People.ID"))
         #  Relationships
        Planets = relationship("Planets")
        People = relationship("People")


def to_dict(self):
        return {}
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
