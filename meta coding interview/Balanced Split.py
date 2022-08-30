import math
import numpy as np

def hoare_partition(arr, l, r):
    pivot = arr[l]

    # A and B bounds
    bound = l
    j = r + 1

    while True:
        while True:
            bound += 1
            if arr[bound] >= pivot or bound >= r: break 
        
        while True:
            j -= 1
            if arr[j] <= pivot: break

        arr[bound], arr[j] = arr[j], arr[bound]
        if bound >= j: break
    
    arr[bound], arr[j] = arr[j], arr[bound]
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


def smaller(a, b):
    if a < b: return True
    
    return False

def check_strictly(arr0, arr1):
    arrB = np.array(arr1)
    for n in arr0:
        if not all(arrB > n):
            return False

    return True

def balancedSplitExists(arr):
    bound = 0
    quicksort(arr, 0, len(arr) - 1)

    while bound != len(arr) - 1:
        A = arr[:bound + 1]
        B = arr[bound + 1:]
        
        if sum(A) == sum(B):
            if check_strictly(A, B):
                return True            
        
        bound += 1

    return False


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
    arr_1 = [2, 1, 2, 5]
    expected_1 = True
    output_1 = balancedSplitExists(arr_1)
    check(expected_1, output_1)

    arr_2 = [3, 6, 3, 4, 4]
    3, 3, 4, 4, 6
    expected_2 = False
    output_2 = balancedSplitExists(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
