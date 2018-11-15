
import webbrowser

class Movie ():
    '''this for adding the movie'''

    def __init__(self, Movie_title , Movie_storyline, Movie_poster_image_url, Movie_trailer_youtube_url ):
        self.title = Movie_title
        self.storyline = Movie_storyline
        self.poster_image_url = Movie_poster_image_url
        self.trailer_youtube_url = Movie_trailer_youtube_url
        """the (__init__) function creates a space in the memory to add and to remember the new values.
        #self is a constructor which been called when I use the instance .. it's like calling the object I use.
        #Input ( Movie_title = movie names ,
                 Movie_storyline = the story of the movies,
                 Movie_poster_image_url = the URL for the poster (img) in the internet,
                 Movie_trailer_youtube_url = The movie trailer link in the youtube )        
        #(self.title, self.storyline,self.poster_image_url ,self.trailer_youtube_url) defining the self with object to use it in the movie website file & movie center.
        #Output will be the movie (Movie_title,Movie_storyline,Movie_poster_image_url , self.title = Movie_title) for each movie."""


    def show_trailer (self):
        webbrowser.open(self.trailer_youtube_url)
    
        """ show_trailer is giving the instruction to the program to open a youtube window inside the web page for the clicked movie """



