import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def numberOfWays(arr, k):
    subarrays = []

    for idx0, value0 in enumerate(arr):
        for idx1, value1 in enumerate(arr):
            if idx0 != idx1 and ((value0 + value1) == k) and ((idx1, idx0) not in subarrays):
                subarrays.append((idx0, idx1))

    return subarrays


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
    k_1 = 6
    arr_1 = [1, 2, 3, 4, 3]
    expected_1 = 2
    output_1 = numberOfWays(arr_1, k_1)
    check(expected_1, output_1)

    k_2 = 6
    arr_2 = [1, 5, 3, 3, 3]
    expected_2 = 4
    output_2 = numberOfWays(arr_2, k_2)
    check(expected_2, output_2)

    # Add your own test cases here
