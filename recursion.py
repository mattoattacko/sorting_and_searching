def sum(numbers):
  if not numbers:
    return 0
  remaining_sum = sum(numbers[1:])
  return numbers[0] + remaining_sum

print(sum([1, 2, 7, 9]))

# The function takes a list of the numbers we want to add.
def sumOne(numbers):
  # The total starts at zero.
  total = 0
  # We loop over every number contained in the list.
  for number in numbers:
    # And we add the current number to the total.
    total += number
  # Once we're done looping, we return the accumulated total.
  return total

# If we call the sum function with a list of numbers, it will return the total.
# When we run this program it will print out that returned value, "19".
print(sumOne([1, 2, 7, 9]))

"""
- If we run this with python recursion.py,  It will output the sum of the numbers in the list
- If we added print statements to help us debug the code, the series of recursive calls would look like this:

$ python recursion.py
Calling sum([2, 7, 9])
Calling sum([7, 9])
Calling sum([9])
Calling sum([])
Call to sum([9]) returning 9 + 0
Call to sum([7, 9]) returning 7 + 9
Call to sum([2, 7, 9]) returning 2 + 16
Call to sum([1, 2, 7, 9]) returning 1 + 18
19
"""