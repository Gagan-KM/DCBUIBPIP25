'''
Write a Python program to implement Merge Sort to sort a list of tuples  
based on the second element of each tuple in ascending order.  

Input:  
    A list of n tuples, where each tuple consists of two integers (x, y).  
    The sorting should be based on the second element (y) of each tuple.  

Constraints:  
    1 ≤ n ≤ 10^5  
    -10^9 ≤ x, y ≤ 10^9  

Example:  
    Input:  
        ele = [(9, 12), (4, 7), (3, 15), (6, 1), (10, 5)]  

    Expected Output:  
        [(6, 1), (10, 5), (4, 7), (9, 12), (3, 15)]  

Explanation:  
    The input list [(9, 12), (4, 7), (3, 15), (6, 1), (10, 5)] is sorted based on the second element.  
    (6, 1) comes first because 1 is the smallest.  
    (10, 5) comes next, as 5 is the second smallest.  
    The final sorted order is [(6, 1), (10, 5), (4, 7), (9, 12), (3, 15)].  
'''

import random
from datetime import datetime

def merge_sort(ele):
    if len(ele) <= 1:
        return 
    mid = len(ele) // 2
    left = ele[mid:]
    right = ele[:mid]
    merge_sort(left)
    merge_sort(right)
    merge_sort_list(left, right, ele)

def merge_sort_list(l1, l2, ele):
    i = j = k = 0
    n1 = len(l1)
    n2 = len(l2)
    while i < n1 and j < n2:
        if l1[i][1] <= l2[j][1]:
            ele[k] = l1[i]
            i += 1
        else:
            ele[k] = l2[j]
            j += 1
        k += 1
    while i < n1:
        ele[k] = l1[i]
        i += 1
        k += 1
    while j < n2:
        ele[k] = l2[j]
        j += 1
        k += 1
start_time = datetime.now()
current_date = datetime.today().strftime("%d-%m-%Y")
ele = [(9, 12), (4, 7), (3, 15), (6, 1), (10, 5)]  
print(f"Before {ele}")
merge_sort(ele)
end_time = datetime.now()
print("The Sorted list {}, time taken {:.3f} as of {}".format(ele, (end_time - start_time).total_seconds(), current_date))