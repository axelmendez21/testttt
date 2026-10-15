# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Midterm Exam 3

def make_movie(movie_title, movie_director, movie_star, movie_runtime=90):
    movie_dict = {'Title': movie_title,
                  'Director': movie_director,
                  'Star': movie_star,
                  'Length': movie_runtime}
    return movie_dict

print(make_movie('Star Wars', 'George Lucas', 'Mark Hamill', 105))
print(make_movie('Revenge of the Nerds', 'Jeff Kanew', 'Donald Gibb'))