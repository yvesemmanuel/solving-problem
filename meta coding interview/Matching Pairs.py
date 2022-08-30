import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
def matching_pairs(s, t):
    # string boundaries
    l = 0
    r = len(s) - 1

    # strings are not mutable, so let's use a list to make a swap
    lst_s = [j for j in s]
    lst_t = [i for i in t]

    while lst_s[l] == lst_t[l] and l < len(lst_s) - 1:
            l += 1
        
    while lst_s[r] == lst_t[r] and r > 0:
        r -= 1

    if r > l:
        lst_s[l], lst_s[r] = lst_s[r], lst_s[l]         

        count = 0
        for i, char in enumerate(lst_s):
            if lst_t[i] == char:
                count += 1
    else:
        count = len(lst_s) - 2
    
    return count
    

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

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
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  s_1, t_1 = "abcde", "adcbe"
  expected_1 = 5
  output_1 = matching_pairs(s_1, t_1)
  check(expected_1, output_1)

  s_2, t_2 = "abcd", "abcd"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)

  # Add your own test cases here
  