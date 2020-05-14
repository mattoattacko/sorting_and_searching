import random
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

def is_sorted(values):
  """
  - Checks to see if our list is already sorted
  - Returns True if sorted, False if not
  - Loops through numeric index of each value in the list, from zero to one less than the length of the list
  - If the list is sorted, then every value in it will be less than the one that comes after it
  """
  for index in range(len(values) - 1):
    if values[index] > values[index + 1]:
      return False
  return True

def bogo_sort(values):
  """
  - Does our actual sorting
  - We call is_sorted to see if the list is sorted, and we will keep looping until is_sorted returns True
  - 'attempts' tracks the number of loops it takes
  - With each pass through, we print the current number of attempts
  """
  attempts = 0
  while not is_sorted(values):
    print(attempts)
    random.shuffle(values)
    attempts += 1
  return values

print(bogo_sort(numbers))
