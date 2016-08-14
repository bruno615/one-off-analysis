
# 4 - Merging Meeting Times
import pdb

times = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]


def condense_meeting_times(tup):
  # Sort the tuple
  tup.sort(key = lambda tup: tup[0])
  # Output Blocks, start with first tuple of times
  blocks = [tup[0]]

  i = 1
  j = 0

  while i < len(tup):
    # If the start time is between the start and end times
    if tup[i][0] >= blocks[j][0] and tup[i][0] <= blocks[j][1]:
      # Take the max of the new meeting and the existing meeting end times
      blocks[j] = [blocks[j][0], max(blocks[j][1], tup[i][1])]
      i = i + 1
    else:
      # Else, add the meeting block
      blocks.append(tup[i])
      i = i + 1
      j = j + 1
  return(blocks)

print(condense_meeting_times(times))

example2 = [(1, 2), (2, 3)]
print(condense_meeting_times(example2))

example3 = [(1, 5), (2, 3)]
print(condense_meeting_times(example3))

example4 = [(1, 10), (2, 6), (3, 5), (7, 9)]
print(condense_meeting_times(example4))
