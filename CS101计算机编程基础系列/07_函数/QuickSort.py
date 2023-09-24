# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 11:13:03 2020
@author: Sam

Implementation of quick sort, with the last index chosen, and a randomized 
chosen partition. 

Future work: Improve this with chosen median algorithm to make sure its
time complexity is O(nlgn).

For a classic demo, see: https://www.youtube.com/watch?v=ywWBy6J5gz8
"""

import random

def partition(lst, p, r):
    """
    Chosen the last element as "piviot", if the array is nearly sorted, namely
    always last is the biggest, time complexity low to O(n ** 2), 
    otherwise it is  Theta(nlgn)
    """
    x = lst[r]
    i = p - 1
    for j in range(p, r):
        if lst[j] <= x:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
            
    lst[i + 1], lst[r] = lst[r], lst[i + 1]
    return i + 1

def randomizedPartition(lst, p, r):
    """
    Randomly choosing a piviot to prevent the above O(n ** 2) as less as 
    possible. Mathematically can prove if the randomization algorithm works
    its complexity is Theta(nlgn), and will in very low probability be O(n ** 2)
    
    随机选一个数换到末尾，防止数组接近排序时对快排效率的拖累，此时数学上可证明，
    若随机算法正常，该算法复杂度为Theta(nlgn)，出现O(n ** 2)的概率极低
    """
    chosenIdx = random.randint(p, r)
    x = lst[chosenIdx]
    lst[r], lst[chosenIdx] = lst[chosenIdx], lst[r]
    i = p - 1
    for j in range(p, r):
        if lst[j] < x:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
   
    lst[i + 1], lst[r] = lst[r], lst[i + 1]
    return i + 1

def qSort(lst, *args):
    if not args:
        qSort(lst, 0, len(lst)-1)
        return
    
    p, r=args
    if p < r:
        q = randomizedPartition(lst, p, r)
        qSort(lst, p, q - 1)
        qSort(lst, q + 1, r)

if __name__ == '__main__':
    """
    A = [2, 8, 7, 1, 3, 5, 6, 4]
    indice = partition(A, 0, 7)
    print(indice)
    print(A)
    print(A[indice])
    """
    items = [6, 20, 5, 8, 19, 56, 23, 87, 41, 49, 53]
    print("Before sort:", items)
    qSort(items)
    print("After sort:", items)
    items = [3, 8, 2, 5, 1, 4, 7, 6]
    print("Before sort:", items)
    qSort(items)
    print("After sort:", items)    