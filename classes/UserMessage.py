from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship
from Basis import *
from User import *
from Message import *

class UserMessege( Base ):
    """
    Describe columns in table UserMesseges
    """

    __tablename__ = 'user_posts'

    __table_args__ = {'extend_existing': True}

    id           = Column( Integer, primary_key = True )
    to_id_user   = Column( Integer, ForeignKey( 'users.id') )
    from_id_user = Column( Integer, ForeignKey( 'users.id') )
    id_message   = Column( Integer, ForeignKey( 'messages.id' ) )
    date_messege = Column( Date )
    status       = Column( String )

    user    = relationship( 'User', backref='fk_user_messege' )
    message = relationship( 'Messege', backref='fk_messege' )