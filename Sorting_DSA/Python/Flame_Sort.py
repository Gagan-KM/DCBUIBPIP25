'''
Write a Python program to implement Quick Sort to sort a list of tuples 
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
import random
from datetime import datetime

def partition(ele, low, high):
    i, j = low, high
    p = ele[low][1]

    while True:
        while i <= j and ele[i][1] <= p:
            i += 1
        while i <= j and ele[j][1] >= p:
            j -= 1
        if i <= j:
            ele[i], ele[j] = ele[j], ele[i]
        else:
            break
    ele[low], ele[j] = ele[j], ele[low]
    return j

def quick_sort(ele, low, high):
    if low < high:
        pivot = partition(ele, low, high)
        quick_sort(ele, low, pivot - 1)
        quick_sort(ele, pivot + 1, high)
        
start_time = datetime.now()
current_date = datetime.today().strftime("%d-%m-%Y")
ele = [(5, 10), (2, 3), (8, 15), (1, 2), (7, 8)]
print(f"Before: {ele}")
quick_sort(ele, 0, len(ele) - 1)
end_time = datetime.now()
print("The Sorted list {}, time taken {:.3f} as of {}".format(ele, (end_time - start_time).total_seconds(), current_date))