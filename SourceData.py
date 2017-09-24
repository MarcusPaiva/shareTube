from classes.User import *
from classes.UserVideo import *
from classes.UserPost import *
from classes.Post import *

class SourceCode:
    def __init__( self, session=None ):
        self.session = session
    
    #####################
    #   crud: User      #
    #####################
    def new_user( self, name=None, gender=None, email=None, password=None, is_admin=None, brief=None, genere=None, status=None, facebook_url=None, twitter=None, youtube_url=None, dailymotion=None, country=None, languange=None ):
        user = User()
        user.name = name
        user.gender = gender
        user.password = password
        user.is_admin = is_admin
        user.brief = brief
        user.genre = genre
        user.status = status
        user.facebook_url = facebook_url
        user.twitter = twitter
        user.youtube_url = youtube_url
        user.dailymotion = dailymotion
        user.country = country
        user.languange = languange

        self.session.add( user )
        self.session.commit()

        return user

    def update_user( self, user_id=None, name=None, gender=None, email=None, is_admin=None, brief=None, genere=None, status=None, facebook_url=None, twitter=None, youtube_url=None, dailymotion=None, country=None, languange=None ):
        user = self.search_user_by_id( user_id )

        user.name = name
        user.gender = gender
        user.is_admin = is_admin
        user.brief = brief
        user.genre = genre
        user.status = status
        user.facebook_url = facebook_url
        user.twitter = twitter
        user.youtube_url = youtube_url
        user.dailymotion = dailymotion
        user.country = country
        user.languange = languange

        self.session.add( user )
        self.session.commit()

        return user

    def change_password_user( self, user_id=None, password=None ):
        user = self.search_user_by_id( user_id )

        user.password = password

        self.session.add( user )
        self.session.commit()

        return user

    def delete_user( self, user_id=None ):
        user = self.search_user_by_id( user_id )

        user.password = password

        self.session.delete( user )
        self.session.commit()

    def search_user_by_id( self, user_id=None ):
        return self.session.query( User ).filter_by( id=user_id ).first()

    def search_users_by_name( self, user_name=None ):
        return self.session.query( User ).filter_by( name=user_name ).all()

    def search_users_by_genre( self, user_genre=None ):
        return self.session.query( User ).filter_by( genre=user_genre ).all()

    def search_user_by_country( self, user_country=None ):
        return self.session.query( User ).filter_by( country=user_country ).all()

    #################################
    #       Crud: User video        #
    #################################
    def new_user_video( self, name=None, id_user=None, date_posted=None, status=None, font=None, url=None, is_live=None, clicks=None, views=None, genre=None ):
        user_video = UserVideo()
        user_video.name = name
        user_video.id_user = id_user
        user_video.date_posted = date_posted
        user_video.status = status
        user_video.font = font
        user_video.url = url
        user_video.is_live = is_live
        user_video.clicks = clicks
        user_video.views = views
        user_video.genre = genre

        self.session.add( user_video )
        self.session.commit()

        return user_video

    def update_user_video( self, video_id=None, name=None, id_user=None, status=None, font=None, url=None, genre=None ):
        user_video = self.search_video_by_id( video_id )
        user_video.name = name
        user_video.id_user = id_user
        user_video.status = status
        user_video.font = font
        user_video.url = url
        user_video.genre = genre

        self.session.add( user_video )
        self.session.commit()

        return user_video

    def remove_user_video( self, video_id=None ):
        self.session.delete( self.search_video_by_id( video_id ) )

    def search_video_by_id( self, video_id=None ):
        return self.session.query( UserVideo ).filter_by( id=video_id ).first()

    def search_video_by_name( self, video_name=None ):
        return self.session.query( UserVideo ).filter_by( name=video_name ).all()

    #########################
    #       Crud: Post      #
    #########################
    def new_post( self, user_id=None, date_post=None, status=None, posting=None, type=None, visibility=None ):
        user_post = UserPost()
        user_post.id_user = user_id
        user_post.date_post = date_post
        user_post.status = status

        post = Post()
        post.post = posting
        post.type = type
        post.visibility = visibility

        user_post.post = post

        self.session.add( user_post )
        self.session.commit()

        return user_post

    def update_post( self, post_id=None, posting=None, type=None, visibility=None ):
        post = search_post_by_id( post_id )

        post.post = posting
        post.type = type
        post.visibility = visibility

        self.session.add( post )
        self.session.commit()

    def remove_post( self, post_id ):
        self.session.delete( self.search_user_post_by_id_post( post_id ) )
        self.session.delete( self.search_post_by_id( post_id ) )
        self.session.commit()

    def search_post_by_id( self, post_id=None ):
        return self.session.query( Post ).filter_by( id=post_id ).first()

    def search_user_post_by_id_post( self, post_id=None ):
        return self.session.query( UserPost ).filter_by( id_post=post_id ).first()