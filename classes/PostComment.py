from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship
from Basis import *
from User import *
from Post import *

class PostComment( Base ):
    """
    Describe columns in table PostComment
    """

    __tablename__ = 'post_comments'

    __table_args__ = {'extend_existing': True}

    id          = Column( Integer, primary_key = True )
    id_user     = Column( Integer, ForeignKey( 'users.id') )
    id_user     = Column( Integer, ForeignKey( 'posts.id') )
    date_posted = Column( Date )
    status      = Column( String )
    text        = Column( String )
    like        = Column( Integer )

    user = relationship( 'User', backref='fk_comment_user' )
    post = relationship( 'Post', backref='fk_comment_post' )