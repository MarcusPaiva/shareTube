from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship
from Basis import *
from User import *

class UserBan( Base ):
    """
    Describe columns in table UserBans
    """

    __tablename__ = 'user_bans'

    __table_args__ = {'extend_existing': True}

    id          = Column( Integer, primary_key = True )
    id_user     = Column( Integer, ForeignKey( 'users.id') )
    date_ban    = Column( Date )
    reason      = Column( String )

    user = relationship( 'User', backref='fk_user_ban' )