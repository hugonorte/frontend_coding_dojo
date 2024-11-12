# QuickSort Algorithm Documentation

## Overview
This module implements the QuickSort algorithm, an efficient sorting algorithm that uses the divide-and-conquer approach to sort elements in a list. The sorting is done in place, meaning that the original list is modified to produce the sorted order.

## Functions

### partition(array, low, high)
This function finds the partition position in the array. It chooses the rightmost element as the pivot and rearranges the elements in the array such that all elements less than or equal to the pivot are on its left, and all elements greater than the pivot are on its right.

#### Parameters:
- `array` (list): The list of elements to be partitioned.
- `low` (int): The starting index of the portion of the list to be partitioned.
- `high` (int): The ending index of the portion of the list to be partitioned.

#### Returns:
- `int`: The index position where the partition is done.

### quickSort(array, low, high)
This function performs the QuickSort algorithm on the array. It recursively sorts the elements by partitioning the array and then sorting the sub-arrays on the left and right of the pivot.

#### Parameters:
- `array` (list): The list of elements to be sorted.
- `low` (int): The starting index of the portion of the list to be sorted.
- `high` (int): The ending index of the portion of the list to be sorted.

### initQuick(data)
This function initializes the QuickSort algorithm by determining the size of the list and calling the `quickSort` function with the appropriate parameters.

#### Parameters:
- `data` (list): The list of elements to be sorted.

## Usage
To use the QuickSort algorithm, call the `initQuick` function with the list of elements you want to sort. The list will be sorted in place.

Example:

in: [1, 8, 6, 2, 2]

out: [1, 2, 2, 6, 8]