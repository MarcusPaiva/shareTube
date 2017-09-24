from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship
from Basis import *
from User import *
from Video import *

class VideoShared( Base ):
    """
    Describe columns in table VideoShareds
    """

    __tablename__ = 'video_shareds'

    __table_args__ = {'extend_existing': True}

    id           = Column( Integer, primary_key = True )
    id_user      = Column( Integer, ForeignKey( 'users.id') )
    id_video     = Column( Integer, ForeignKey( 'videos.id' ) )
    date_shared  = Column( Date )
    where_shared = Column( Integer )

    user  = relationship( 'User', backref='fk_shared_user' )
    video  = relationship( 'Video', backref='fk_shared_video' )