#30 - Permutation Palendrome.py

# Write an efficient function that checks whether any permutation of an input string is a palindrome.
# Examples:

# "civic" should return True
# "ivicc" should return True
# "civil" should return False
# "livci" should return False
# "But 'ivicc' isn't a palindrome!"
# If you had this thought, read the question again carefully. We're asking if any permutation of the string is a palindrome. Spend some extra time ensuring you fully understand the question before starting. Jumping in with a flawed understanding of the problem doesn't look good in an interview.

import pdb

def is_palindrome(string):
  if not string.isalpha():
    raise NameError('Input contains non-alphabet character(s)')
  string = string.lower()

  odd_letters = []

  for letter in list(string):
    if letter in odd_letters:
      odd_letters.remove(letter)
    else:
      odd_letters.append(letter)

  return(len(odd_letters) <= 1)

print(is_palindrome('cIvvv1ic'))
