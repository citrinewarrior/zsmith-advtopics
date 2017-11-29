#models file for the esports database
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base= declarative_base()

class Esports(Base):
    __tablename__ = "playerinfo"

    id= column(Integer, primary_key = True)
    #playername
    #gamename
    #kda
    #cspermin
    #pkillpart
