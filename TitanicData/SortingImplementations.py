#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 19:02:11 2024

@author: dennisf
"""

import csv
import time  

Ages = []
with open('train.csv', 'r') as file:
    reader = csv.reader(file)
    column_index = 5
    next(reader)  
    for row in reader:
        Age = row[column_index]
        if Age != '' and Age != 'Age':
            Ages.append(float(Age)) 

# Extract the first 20 age values
Ages = Ages[:20]
print("First 20 Ages Given:", Ages)

#---------------MERGE SORT------------------
def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        lhalf = arr[:middle]
        rhalf = arr[middle:]
        merge_sort(lhalf)
        merge_sort(rhalf)
        i = j = k = 0
        while i < len(lhalf) and j < len(rhalf):
            if lhalf[i] < rhalf[j]:
                arr[k] = lhalf[i]
                i += 1
            else:
                arr[k] = rhalf[j]
                j += 1
            k += 1
        while i < len(lhalf):
            arr[k] = lhalf[i]
            i += 1
            k += 1
        while j < len(rhalf):
            arr[k] = rhalf[j]
            j += 1
            k += 1
    return arr

#---------------BUBBLE SORT------------------
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#---------------INSERTION SORT------------------
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

#---------------SELECTION SORT------------------
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

#---------------QUICK SORT------------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left) + [pivot] + quick_sort(right)


results = {}

# Merge Sort
start_time = time.time()
sorted_merge = merge_sort(Ages.copy())
results['Merge Sort'] = time.time() - start_time

# Bubble Sort
start_time = time.time()
sorted_bubble = bubble_sort(Ages.copy())
results['Bubble Sort'] = time.time() - start_time

# Insertion Sort
start_time = time.time()
sorted_insertion = insertion_sort(Ages.copy())
results['Insertion Sort'] = time.time() - start_time

# Selection Sort
start_time = time.time()
sorted_selection = selection_sort(Ages.copy())
results['Selection Sort'] = time.time() - start_time

# Quick Sort
start_time = time.time()
sorted_quick = quick_sort(Ages.copy())
results['Quick Sort'] = time.time() - start_time

# Print sorted arrays
print("Sorted Results:")
print("Merge Sort:", sorted_merge)
print("Bubble Sort:", sorted_bubble)
print("Insertion Sort:", sorted_insertion)
print("Selection Sort:", sorted_selection)
print("Quick Sort:", sorted_quick)

print("\nTime Taken for Each Sorting Algorithm:")
for sort_type, duration in results.items():
    print(f"{sort_type}: {duration:.6f} seconds")
