# Calling the and creating objects using the Movie Class in the Media

import movie

# pass(movie_title, movie_storyline, poster_image, trailer_youtube)
toy_story = movie.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and jealous .",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtu.be/wmiIUN-7qhE")

toy_story = movie.Movie("Avatar",
                        "A marine on an alien planet.",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://youtu.be/6ziBFh3V1aM")

print(toy_story.storyline)