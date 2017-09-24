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

channel_messages = Table(
                                'channel_messages',
                                Base.metadata,
                                Column( 'id_channel', Integer, ForeignKey( 'channels.id' ) ),
                                Column( 'id_message', Integer, ForeignKey( 'messages.id' ) ),
                                Column( 'date_sended', Date ),
                                Column( 'status', String )
)

group_posts = Table(
                                'group_posts',
                                Base.metadata,
                                Column( 'id_group', Integer, ForeignKey( 'groups.id' ) ),
                                Column( 'id_post', Integer, ForeignKey( 'posts.id' ) ),
                                Column( 'date_post', Date ),
                                Column( 'status', String )
)

page_posts = Table(
                                'page_posts',
                                Base.metadata,
                                Column( 'id_page', Integer, ForeignKey( 'pages.id' ) ),
                                Column( 'id_post', Integer, ForeignKey( 'posts.id' ) ),
                                Column( 'date_post', Date ),
                                Column( 'status', String )
)

post_comments = Table(
                                'post_comments',
                                Base.metadata,
                                Column( 'id_user', Integer, ForeignKey( 'users.id' ) ),
                                Column( 'id_post', Integer, ForeignKey( 'posts.id' ) ),
                                Column( 'date_posted', Date ),
                                Column( 'text', String ),
                                Column( 'like', String ),
                                Column( 'status', String )
)

relationship_users = Table(
                                'relationship_users',
                                Base.metadata,
                                Column( 'id_user_first', Integer, ForeignKey( 'users.id' ) ),
                                Column( 'id_user_second', Integer, ForeignKey( 'users.id' ) ),
                                Column( 'date_relationship', Date ),
                                Column( 'status', String )
)

user_bans = Table(
                                'user_bans',
                                Base.metadata,
                                Column( 'id_user', Integer, ForeignKey( 'users.id' ) ),
                                Column( 'date_ban', reason ),
                                Column( 'reason', String )
)

user_channels = Table(
                                'user_channels',
                                Base.metadata,
                                Column( 'id_user', Integer, ForeignKey( 'users.id' ) ),
                                Column( 'id_channel', Integer, ForeignKey( 'channel.id' ) )
)

user_groups = Table(
                                'user_groups',
                                Base.metadata,
                                Column( 'id_user', Integer, ForeignKey( 'users.id' ) ),
                                Column( 'id_group', Integer, ForeignKey( 'groups.id' ) ),
                                Column( 'date_joined', Date ),
                                Column( 'status', String ),
                                Column( 'is_admin', String )
)

user_pages = Table(
                                'user_groups',
                                Base.metadata,
                                Column( 'id_user', Integer, ForeignKey( 'users.id' ) ),
                                Column( 'id_page', Integer, ForeignKey( 'pages.id' ) ),
                                Column( 'date_joined', Date ),
                                Column( 'status', String ),
                                Column( 'is_admin', String )
)

user_posts = Table(
                                'user_posts',
                                Base.metadata,
                                Column( 'id_user', Integer, ForeignKey( 'users.id' ) ),
                                Column( 'id_post', Integer, ForeignKey( 'posts.id' ) ),
                                Column( 'date_post', Date ),
                                Column( 'status', String )
)

user_videos = Table(
                                'user_posts',
                                Base.metadata,
                                Column( 'id_user', Integer, ForeignKey( 'users.id' ) ),
                                Column( 'date_posted', Date ),
                                Column( 'status', String ),
                                Column( 'font', String ),
                                Column( 'url', String ),
                                Column( 'is_live', String ),
                                Column( 'clicks', Integer ),
                                Column( 'views', Integer ),
                                Column( 'genre', Integer )
)