from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import mapper, relationship
from Basis import *


class Post( Base ):
    """
    Describe columns in table Posts
    """
    
    __tablename__ = 'posts'

    id         = Column( Integer, primary_key = True )
    post       = Column( String )
    type       = Column( String )
    status     = Column( String )
    visibility = Column( String )
    like       = Column( String )