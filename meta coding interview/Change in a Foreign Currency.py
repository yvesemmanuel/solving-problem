import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def canGetExactChange(targetMoney, denominations):
    if targetMoney == 0:
        return True
    elif targetMoney < 0:
        return False

    for coin in denominations:
        if (canGetExactChange(targetMoney - coin, denominations)):
            return True

    return False


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
        print(wrongTick, 'Test #', test_case_number,
              ': Expected ', sep='', end='')
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    target_1 = 94
    arr_1 = [5, 10, 25, 100, 200]
    expected_1 = False
    output_1 = canGetExactChange(target_1, arr_1)
    check(expected_1, output_1)

    target_2 = 75
    arr_2 = [4, 17, 29]
    expected_2 = True
    output_2 = canGetExactChange(target_2, arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
