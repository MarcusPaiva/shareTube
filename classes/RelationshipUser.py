from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship
from Basis import *
from User import *

class RelationshipUser( Base ):
    """
    Describe columns in table RelationshipUsers
    """

    __tablename__ = 'relationship_users'

    __table_args__ = {'extend_existing': True}

    id                 = Column( Integer, primary_key = True )
    id_user_first      = Column( Integer, ForeignKey( 'users.id') )
    id_user_second     = Column( Integer, ForeignKey( 'users.id' ) )
    date_relationship  = Column( Date )
    status             = Column( String )

    user  = relationship( 'User', backref='fk_users' )