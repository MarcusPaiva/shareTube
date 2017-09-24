from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship
from Basis import *
from User import *

class SupportMessage( Base ):
    """
    Describe columns in table UserBans
    """

    __tablename__ = 'support_messages'

    __table_args__ = {'extend_existing': True}

    id            = Column( Integer, primary_key = True )
    id_user       = Column( Integer, ForeignKey( 'users.id') )
    type_message  = Column( Integer )
    date_received = Column( Date )
    message       = Column( String )

    user = relationship( 'User', backref='fk_user_ban' )