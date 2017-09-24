from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship
from Basis import *
from User import *
from Channel import *

class UserMessege( Base ):
    """
    Describe columns in table UserMesseges
    """

    __tablename__ = 'user_channels'

    __table_args__ = {'extend_existing': True}

    id           = Column( Integer, primary_key = True )
    id_user      = Column( Integer, ForeignKey( 'users.id') )
    id_channel   = Column( Integer, ForeignKey( 'channels.id') )

    user    = relationship( 'User', backref='fk_channel_user' )
    channel = relationship( 'Channel', backref='fk_user_channel' )