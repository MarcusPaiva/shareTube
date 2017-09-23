from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship
from Basis import *
from Post import *
from Group import *

class GroupPost( Base ):
    """
    Describe columns in table GroupPosts
    """

    __tablename__ = 'group_posts'

    __table_args__ = {'extend_existing': True}

    id        = Column( Integer, primary_key = True )
    id_group   = Column( Integer, ForeignKey( 'groups.id') )
    id_post   = Column( Integer, ForeignKey( 'posts.id' ) )
    date_post = Column( Date )
    status    = Column( String )

    group = relationship( 'Group', backref='fk_group_post' )
    post = relationship( 'Post', backref='fk_post_group' )