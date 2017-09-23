from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship
from Basis import *
from User import *

class UserVideo( Base ):
    """
    Describe columns in table UserVideo
    """

    __tablename__ = 'user_videos'

    __table_args__ = {'extend_existing': True}

    id          = Column( Integer, primary_key = True )
    id_user     = Column( Integer, ForeignKey( 'users.id') )
    date_posted = Column( Date )
    status      = Column( String )
    font        = Column( String )
    url         = Column( String )
    is_live     = Column( String )
    clicks      = Column( Integer )
    views       = Column( Integer )
    genre       = Column( Integer )

    user = relationship( 'User', backref='fk_user' )