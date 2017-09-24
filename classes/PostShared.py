from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship
from Basis import *
from User import *
from Post import *

class PostShared( Base ):
    """
    Describe columns in table PostShareds
    """

    __tablename__ = 'post_shareds'

    __table_args__ = {'extend_existing': True}

    id           = Column( Integer, primary_key = True )
    id_user      = Column( Integer, ForeignKey( 'users.id') )
    id_post      = Column( Integer, ForeignKey( 'posts.id' ) )
    date_shared  = Column( Date )
    where_shared = Column( Integer )

    user  = relationship( 'User', backref='fk_share_user' )
    post  = relationship( 'Post', backref='fk_share_post' )