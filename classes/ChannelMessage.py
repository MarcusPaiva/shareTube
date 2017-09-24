from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship
from Basis import *
from User import *
from Channel import *

class ChannelMessage( Base ):
    """
    Describe columns in table UserGroups
    """

    __tablename__ = 'channel_messages'

    __table_args__ = {'extend_existing': True}

    id          = Column( Integer, primary_key = True )
    id_channel  = Column( Integer, ForeignKey( 'chanels.id') )
    id_message  = Column( Integer, ForeignKey( 'messages.id' ) )
    date_sended = Column( Date )
    status      = Column( String )

    channel = relationship( 'Channel', backref='fk_channel' )
    message = relationship( 'Message', backref='fk_message' )