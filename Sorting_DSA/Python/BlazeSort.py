'''
Write a Python program to implement Bubble Sort to sort a list of tuples 
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
def bubble_sort(ele):
    n = len(ele)
    for k in range(n - 1):
        swap = False
        for i in range(n - 1 - k):
            if ele[i][1] > ele[i + 1][1]:
                ele[k], ele[k + 1] = ele[k + 1], ele[k]
                swap = True
        if not swap:
            break
    return ele
starttime = time.time()
ele = [(5, 10), (2, 3), (8, 15), (1, 2), (7, 8)]
result = bubble_sort(ele)
endtime = time.time()
time = starttime - endtime
print("The Sorted List of Tuples {}, time taken {:.3f}".format(result, time))