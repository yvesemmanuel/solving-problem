import math
# Add any extra import statements you may need here


def Convert(string):
    list1 = []
    list1[:0] = string
    return list1


def get_substrings(string, K):
    n = len(string)
    substrings = []

    for i in range(0, n):
        for j in range(i, n):
            if (j + 1 - i) >= K:
                substrings.append(Convert(string[i:j + 1]))

    return substrings


def min_length_substring(s, t):
    K = len(t)
    S_substrings = get_substrings(s, K)

    minimum = float('inf')
    for sub in S_substrings:
        equal = 0
        S_sub = Convert(sub)
        for c in t:
            if c in S_sub:
                equal += 1
                S_sub.remove(c)

        if equal == K and minimum > len(sub):
            minimum = len(sub)

    if minimum == float('inf'):
        return -1
    else:
        return minimum


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
        print(wrongTick, 'Test #', test_case_number,
              ': Expected ', sep='', end='')
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    s1 = "dcbefebce"
    t1 = "fd"
    expected_1 = 5
    output_1 = min_length_substring(s1, t1)
    check(expected_1, output_1)

    s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
    t2 = "cbccfafebccdccebdd"
    expected_2 = -1
    output_2 = min_length_substring(s2, t2)
    check(expected_2, output_2)
