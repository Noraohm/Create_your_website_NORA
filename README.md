# Create_your_website_NORA
Project of intro to programming (Udacity). Creating a movie website.


**project overview**

The Movie Trailer Website project consists of server-side code to store a list of movies titles, along with its respective box art imagery and movie trailer website. 
The data should be served as a web page allowing visitors to review the movies and watch the trailers:


## Prerequisites
To run a Python you need below:
1) Python 2 or 3 version from [click here](https://www.python.org/downloads/).
2) Google & github to search if you stuck in any steps [click here](https://github.com/).

## Installing:

follow the instruction in the download page for installing the programs.

### Steps:


In this project you will create 3 python file:
1)	in media file you will import the webbrowser function to open the browser. Also you will create the Movie class and inhert 2 def function 
-	(__init__) to create a space in the memory to add and to remember the new values.
-	show_trailer is giving the instruction to the program to open a youtube window inside the web page for the clicked movie


```
lass Movie ():
    '''this for adding the movie'''

    def __init__(self, Movie_title , Movie_storyline, Movie_poster_image_url, Movie_trailer_youtube_url ):
        self.title = Movie_title
        self.storyline = Movie_storyline
        self.poster_image_url = Movie_poster_image_url
        self.trailer_youtube_url = Movie_trailer_youtube_url
    def show_trailer (self):
        webbrowser.open(self.trailer_youtube_url)        
        
```

2)	 Movie_Website you will use some HTML , CSS & JS code to set up the page also you will need to use front-end framework like 
Bootstrap or flask with some Python codes to open the page and the required content to be appear.


3)	Movies_center to add all displayed movie information’s. In this you need to import the 2 rest files to shape the information as its.



## Authors
Nora Almotairy
