from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship
from Basis import *


class Channel( Base ):
    """
    Describe columns in table Channels
    """

    __tablename__ = 'channels'


    id           = Column( Integer, primary_key = True )
    status       = Column( String )
    type_channel = Column( String )
    user_id_list = Column( String )