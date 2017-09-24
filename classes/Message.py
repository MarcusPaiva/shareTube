from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import mapper, relationship
from Basis import *


class Message( Base ):
    """
    Describe columns in table Messages
    """
    
    __tablename__ = 'messages'

    id         = Column( Integer, primary_key = True )
    user       = Column( Integer, ForeignKey( 'users.id' ) )
    post       = Column( String )