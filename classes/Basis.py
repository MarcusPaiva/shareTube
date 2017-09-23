from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

relationship_users = Table(
                                'relationship_users',
                                Base.metadata,
                                Column( 'id_user_first', Integer, ForeignKey( 'users.id' ) ),
                                Column( 'id_user_second', Integer, ForeignKey( 'users.id' ) ),
                                Column( 'date_relationship', Date ),
                                Column( 'status', String )
)

user_posts = Table(
                                'user_posts',
                                Base.metadata,
                                Column( 'id_user', Integer, ForeignKey( 'users.id' ) ),
                                Column( 'id_post', Integer, ForeignKey( 'posts.id' ) ),
                                Column( 'date_post', Date ),
                                Column( 'status', String )
)