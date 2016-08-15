#32 - Top Scores.py

# You rank players in the game from highest to lowest score. So far you're using an algorithm that sorts in O(n\lg{n})O(nlgn) time, but players are complaining that their rankings aren't updated fast enough. You need a faster sorting algorithm.

# Write a function that takes:

# a list of unsorted_scores
# the highest_possible_score in the game
# and returns a sorted list of scores in less than O(nlog(n)) time.

unsorted_scores = [5,20, 3, 89, 89, 99, 98]
highest_possible_score = 100

def get_highest_scores(unsorted_scores, highest_possible_score):

  # define a dictionary
  scores_to_counts = {}

  for score in unsorted_scores:
    if score in scores_to_counts:
      scores_to_counts[score] += 1
    else:
      scores_to_counts[score] = 1

  sorted_scores = sorted(scores_to_counts, reverse = True)

  full_sorted_list = []
  for score in sorted_scores:
    j = scores_to_counts[score]
    while j > 0:
      full_sorted_list.append(score)
      j = j - 1
  return(full_sorted_list)



print get_highest_scores(unsorted_scores, highest_possible_score)
