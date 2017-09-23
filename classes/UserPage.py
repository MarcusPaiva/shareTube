from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship
from Basis import *
from User import *
from Page import *

class UserPage( Base ):
    """
    Describe columns in table UserPages
    """

    __tablename__ = 'user_pages'

    __table_args__ = {'extend_existing': True}

    id          = Column( Integer, primary_key = True )
    id_user     = Column( Integer, ForeignKey( 'users.id') )
    id_page    = Column( Integer, ForeignKey( 'pages.id' ) )
    date_joined = Column( Date )
    status      = Column( String )
    is_admin    = Column( String )

    user = relationship( 'User', backref='fk_user' )
    page = relationship( 'Page', backref='fk_page' )