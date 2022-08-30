import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

def findSignatureCounts(arr):
    n = len(arr)

    # initially each student sign its own book
    signatures = [1] * n

    # for each student
    for i in range(1, n + 1):

        # sign all books he receives until he holds his own book
        idx = i - 1
        while arr[idx] != i:
            signatures[idx] += 1
            idx = arr[idx] - 1

    return signatures


def printInteger(n):
    print('[', n, ']', sep='', end='')


def printIntegerList(array):
    size = len(array)
    print('[', end='')
    for i in range(size):
        if i != 0:
            print(', ', end='')
        print(array[i], end='')
    print(']', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    expected_size = len(expected)
    output_size = len(output)
    result = True
    if expected_size != output_size:
        result = False
    for i in range(min(expected_size, output_size)):
        result &= (output[i] == expected[i])
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number,
              ': Expected ', sep='', end='')
        printIntegerList(expected)
        print(' Your output: ', end='')
        printIntegerList(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    arr_1 = [2, 1]
    expected_1 = [2, 2]
    output_1 = findSignatureCounts(arr_1)
    check(expected_1, output_1)

    arr_2 = [1, 2]
    expected_2 = [1, 1]
    output_2 = findSignatureCounts(arr_2)
    check(expected_2, output_2)

    arr_3 = [3, 2, 4, 1]
    expected_3 = [3, 1, 3, 3]
    output_3 = findSignatureCounts(arr_3)
    check(expected_3, output_3)
