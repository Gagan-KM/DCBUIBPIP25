'''
Write a Python program to implement Insertion Sort to sort a list of tuples 
based on the second element of each tuple in ascending order.

Input:
    A list of n tuples, where each tuple consists of two integers (x, y).
    The sorting should be based on the second element (y) of each tuple.
    
Constraints:
    1 ≤ n ≤ 10^5
    -10^9 ≤ x, y ≤ 10^9

Example:
    Input:
        ele = [(5, 10), (2, 3), (8, 15), (1, 2), (7, 8)]

    Expected Output:
        [(1, 2), (2, 3), (7, 8), (5, 10), (8, 15)]

Explanation:
    The input list [(5, 10), (2, 3), (8, 15), (1, 2), (7, 8)] is sorted based on the second element.
    (1, 2) comes first because 2 is the smallest.
    (2, 3) comes next, as 3 is the second smallest.
    The final sorted order is [(1, 2), (2, 3), (7, 8), (5, 10), (8, 15)].
'''

import time
def insertion_sort(ele):
    n = len(ele)
    for i in range(1, n):
        anchor = ele[i]
        j = i - 1
        while anchor[1] < ele[j][1] and j >= 0:
            ele[j + 1] = ele[j]
            j -= 1
        ele[j + 1] = anchor
    return ele
starttime = time.time()
ele = [(5, 10), (2, 3), (8, 15), (1, 2), (7, 8)]
result = insertion_sort(ele)
endtime = time.time()
time = starttime - endtime
print("The Sorted List of Tuples {}, time taken {:.3f}".format(result, time))