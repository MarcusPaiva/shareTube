from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship
from Basis import *
from Post import *
from Page import *

class PagePost( Base ):
    """
    Describe columns in table PagePosts
    """

    __tablename__ = 'page_posts'

    __table_args__ = {'extend_existing': True}

    id        = Column( Integer, primary_key = True )
    id_page   = Column( Integer, ForeignKey( 'pages.id') )
    id_post   = Column( Integer, ForeignKey( 'posts.id' ) )
    date_post = Column( Date )
    status    = Column( String )

    page = relationship( 'Page', backref='fk_page_post' )
    post = relationship( 'Post', backref='fk_post_page' )