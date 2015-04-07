import movie_scene

class Movie():

    def __init__(self, title, image_url, trailer_youtube_url ) :
        self.title = title
        self.poster_image_url = image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.actors = []
        
    def add_actor( self, ac ) :
        self.actors.append( ac )
    
