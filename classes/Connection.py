from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

db = create_engine( 'mysql://sharetube:mypasswd@localhost/sharetube', pool_size=20, max_overflow=0, pool_recycle=1 )
"""
Describe connection to dadabase
"""

class Connection:

	def connect( self ):
		"""
		Start connection whith database
		"""
		Session = sessionmaker( bind = db )
		session = Session()
return session