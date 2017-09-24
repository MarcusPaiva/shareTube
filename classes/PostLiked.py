from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship
from Basis import *
from User import *
from Post import *

class PostLiked( Base ):
    """
    Describe columns in table PostLikeds
    """

    __tablename__ = 'post_likeds'

    __table_args__ = {'extend_existing': True}

    id           = Column( Integer, primary_key = True )
    id_user      = Column( Integer, ForeignKey( 'users.id') )
    id_post      = Column( Integer, ForeignKey( 'post.id' ) )
    date_liked  = Column( Date )

    user  = relationship( 'User', backref='fk_like_user' )
    post  = relationship( 'Post', backref='fk_like_post' )