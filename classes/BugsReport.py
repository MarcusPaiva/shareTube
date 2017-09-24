from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship
from Basis import *
from User import *


class BugReport( Base ):
    """
    Describe columns in table Posts
    """
    
    __tablename__ = 'repports'

    __table_args__ = {'extend_existing': True}

    id          = Column( Integer, primary_key = True )
    id_user     = Column( Integer, ForeignKey( 'users.id') )
    description = Column( String )
    bug_type    = Column( String )
    report_date = Column( Date )