import math
# Add any extra import statements you may need here


def hoare_partition(arr, l, r):
    pivot = arr[l]

    # lower and upper bounds
    i = l
    j = r + 1

    while True:
        while True:
            i += 1
            if arr[i] >= pivot or i >= r: break 
        
        while True:
            j -= 1
            if arr[j] <= pivot: break

        arr[i], arr[j] = arr[j], arr[i]
        if i >= j: break
    
    arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    
    return j

def quicksort(arr, l, r):
    if l < r:
        pivot = hoare_partition(arr, l, r)
        quicksort(arr, l, pivot - 1)
        quicksort(arr, pivot + 1, r)

def countDistinctTriangles(arr):
    listedArrays = list(map(list, arr))
    ordernedArrays = []
    
    count = 0
    for a in listedArrays:
        quicksort(a, 0, len(a) - 1)

        if a not in ordernedArrays:
            ordernedArrays.append(a)
            count += 1
    
    return count


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
    arr_1 = [(7, 6, 5), (5, 7, 6), (8, 2, 9), (2, 3, 4), (2, 4, 3)]
    expected_1 = 3
    output_1 = countDistinctTriangles(arr_1)
    check(expected_1, output_1)

    arr_2 = [(3, 4, 5), (8, 8, 9), (7, 7, 7)]
    expected_2 = 3
    output_2 = countDistinctTriangles(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here