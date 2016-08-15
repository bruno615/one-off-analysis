#14 - Inflight Entertainment.py
# https://www.interviewcake.com/question/python/inflight-entertainment

#Users on longer flights like to start a second movie right when their first one ends,
#but they complain that the plane usually lands before they can see the ending.
#So you're building a feature for choosing two movies whose total runtimes will equal the exact flight length.

#Write a function that takes an integer flight_length (in minutes)
# and a list of integers movie_lengths (in minutes)
# and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.

flight_length = 360

movie_lengths = [121, 181, 239]

def exists_movie_combo(flight_length, movie_lengths):

  # Order the movies shortest to longest
  movie_lengths.sort(key = lambda movie_lengths:movie_lengths)

  # Find the required movie length for movie to for a perfect fit
  ideal_second_movie_length = [flight_length - x for x in movie_lengths]

  # This is a less efficient method, but it ensures the same movie isn't watched twice
  i = 0
  while i < len(movie_lengths):
    if ideal_second_movie_length[i] in movie_lengths[:i]+movie_lengths[(i+1):]:
      return(True)
    i = i + 1
  return(False)

# Returns true because two movies fit the flight
print(exists_movie_combo(flight_length = 360, movie_lengths = [109,251]))

# Returns false because there must be 2 movies
print(exists_movie_combo(flight_length = 360, movie_lengths = [1,2,360]))

# Returns false because the same movie should not be watched twice, even if correct length
print(exists_movie_combo(flight_length = 360, movie_lengths = [1,2,180]))
