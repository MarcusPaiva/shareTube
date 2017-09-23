from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import mapper, relationship
from Basis import *


class Page( Base ):
    """
    Describe columns in table Pages
    """
    
    __tablename__ = 'pages'

    id          = Column( Integer, primary_key = True )
    name        = Column( String )
    visibility  = Column( String )
    status      = Column( String )
    banner      = Column( String )
    description = Column( String )