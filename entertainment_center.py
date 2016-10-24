import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A marine on an alien planet", "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

the_founder = media.Movie("The Founder", "A man who build McDonald Empire", "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Founder_poster.jpg", "https://www.youtube.com/watch?v=AX2uz2XYkbo")

ratatouille = media.Movie("Ratatouille", "A mouse who dreamed to be a chef", "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", "https://www.youtube.com/watch?v=c3sBBRxDAqk")

movies = [toy_story, avatar, the_founder, ratatouille]
#fresh_tomatoes.open_movies_page(movies)
print (media.Movie.VALID_RATINGS)

