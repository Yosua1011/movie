import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on an alien planet", "http://www.fandomfollowing.com/wp-content/uploads/2016/02/avatar-wallp-1920x1080.jpeg", "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
print(avatar.storyline)
avatar.show_trailer()

the_founder = media.Movie("The Founder", "A man who build McDonald Empire", "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Founder_poster.jpg", "https://www.youtube.com/watch?v=AX2uz2XYkbo")
the_founder.show_poster()