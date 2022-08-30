import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def are_they_equal(array_a, array_b):
  # Write your code here
  if array_a == array_b:
      return True
  elif set(array_a) != set(array_b):
    return False

  lst = []
  for i in range(len(array_a)):
      if array_a[i] != array_b[i]:
          lst.append(i)

  array_to_match = array_a[lst[0]:lst[-1] + 1]
  subarray = array_b[lst[0]:lst[-1] + 1]
  subarray.reverse()
  
  return subarray == array_to_match


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.
def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1 = 4
  a_1 = [1, 2, 3, 4, 5]
  b_1 = [1, 5, 4, 3, 2]
  expected_1 = True
  output_1 = are_they_equal(a_1, b_1)
  check(expected_1, output_1)

  n_2 = 4
  a_2 = [1, 4, 2, 3]
  b_2 = [1, 2, 3, 4]
  expected_2 = False
  output_2 = are_they_equal(a_2, b_2)
  check(expected_2, output_2)

  # Add your own test cases here
  