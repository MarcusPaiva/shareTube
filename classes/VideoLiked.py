from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship
from Basis import *
from User import *
from Video import *

class VideoLiked( Base ):
    """
    Describe columns in table VideoLikeds
    """

    __tablename__ = 'video_likeds'

    __table_args__ = {'extend_existing': True}

    id           = Column( Integer, primary_key = True )
    id_user      = Column( Integer, ForeignKey( 'users.id') )
    id_video      = Column( Integer, ForeignKey( 'videos.id' ) )
    date_liked  = Column( Date )

    user  = relationship( 'User', backref='fk_liked_user' )
    video  = relationship( 'Video', backref='fk_like_video' )