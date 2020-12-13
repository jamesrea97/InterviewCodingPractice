# InterviewCodingPractice

This project contains coding interview practice taken from various sources,
written in Python.

The project is the following topics:

- Arrays (of integers) under file `array.py`
- Strings under `string.py`
- Data Structures under `structures.py`
- Sorting Algorithms under `sorting.py`
- Miscellaneous code under `misc.py`

## Running Project

Each question/algorithm can be run from `main.py`.

## Consideratinos for Reader

Additional comments about _time_ and _space_ complexity were added to
each question/algorithm.

Python Library usage was reduced to minimal in order to make solutions as
language agnostic as possible.

## Data Structures Discussion

In this section, diagrams explaining the idea behind each data structure is
presented.

### Linked List

<p align="center">
  <img src="https://user-images.githubusercontent.com/59763234/102012419-71bcb980-3d4a-11eb-93be-12503bda9c81.png"  width="500"/>
</p>

### Binary Search Tree
<p align="center">
  <img src="https://user-images.githubusercontent.com/59763234/102012422-75e8d700-3d4a-11eb-85bd-f3867ac95b62.png"  width="500"/>
</p>

### Binary (Max) Heap
<p align="center">
  <img src="https://user-images.githubusercontent.com/59763234/102012420-73867d00-3d4a-11eb-88c5-0068fafd8e80.png" width="500"/>
</p>

## Sorting Algorithm Discussion

In this section, diagrams explaining the idea behind each sorting algorithm
is presented. Additionl comments on the worst _time_ and _space_ complexity are
also provided.

### Selection Sort

Idea: Select element for current location. Repeat for all n locations.

Time Complexity: O(n^2) for all cases since we need to find the element for
each location.

Auxillary Space Complexity: O(1) since no extra array is necessary

### Insertion Sort

Idea: Move down (inserting) element into sorted array, swapping on element-wise
comparisons.

Time Complexity:
Worst - O(n^2) whenever the list is reversed sorted as we need
to swao with each element in sorted sub-arrray.
Best - O(n) whenever the list is already sorted since no swaps needed.

Auxillary Space Complexity: O(1) since no extra array is necessary

### Merge Sort

Idea: Divide array into subarrays, sort them, merge them together

Time Complexity: O(nlog(n))for all cases since we have log(N) division levels,
each of which have to merge the array in a sorted way before considering longer
sub-arrays.

Auxillary Space Complexity: O(N) since we need to store subarrays, whose total
length is N.

### Quick Sort

Idea: Create a pivot. Move everything less/more pivot on left/right pivot.
Repeat process and combine the results together to form sorted array.

Time Complexity:
Best: O(nlog(n)) - when the array is evenly divided - no need
to move any elements either side of the pivot at a given layer
Worst: O(n^2) - when already sorted as need to move maximum of elements either
side of pivot at a given layer.

Auxillary Space Complexity: O(N) since we need to store subarrays, whose total
length is N.
