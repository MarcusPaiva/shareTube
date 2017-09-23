from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import mapper, relationship
from Basis import *


class Group( Base ):
    """
    Describe columns in table Groups
    """
    
    __tablename__ = 'groups'

    id         = Column( Integer, primary_key = True )
    name       = Column( String )
    visibility = Column( String )
    status     = Column( String )
    banner      = Column( String )
    description = Column( String )