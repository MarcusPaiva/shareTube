from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import mapper, relationship
from Basis import *

class User( Base ):
    """
    Describe columns in table Users
    """

    __tablename__ = 'users'

    id           = Column( Integer, primary_key = True )
    name         = Column( String )
    email        = Column( String )
    password     = Column( String )
    type         = Column( String )
    brief        = Column( String )
    genre        = Column( Integer )
    status       = Column( String )
    facebook_url = Column( String )
    twitter      = Column( String )
    youtube_url  = Column( String )
    dailymotion  = Column( String )
    country      = Column( Integer )
    language     = Column( Integer )