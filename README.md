# Sorting-Algorithm
This folder will contains my implementations of some sorting algorithm from scratch.  

## QuickSort
<<<<<<< HEAD
Quicksort is a divide and conquer algorithm which relies on a partition operation: to partition an array, an element called a pivot is selected. All elements smaller than the pivot are moved before it and all greater elements are moved after it. 

### Efficiency 
This can be done efficiently in linear time and in-place. The lesser and greater sublists are then recursively sorted. This yields average time complexity of O(n log n), with low overhead, and thus this is a popular algorithm. Efficient implementations of quicksort (with in-place partitioning) are typically unstable sorts and somewhat complex, but are among the fastest sorting algorithms in practice. Together with its modest O(log n) space usage, quicksort is one of the most popular sorting algorithms and is available in many standard programming libraries.
=======

### Algorithm
Quicksort is a divide and conquer algorithm which relies on a partition operation: to partition an array, an element called a pivot is selected. All elements smaller than the pivot are moved before it and all greater elements are moved after it. 

Read more here : https://en.wikipedia.org/wiki/Sorting_algorithm#Quicksort

## Binary Search

### Algorithm
Binary search works on sorted arrays. Binary search begins by comparing an element in the middle of the array with the target value. If the target value matches the element, its position in the array is returned. If the target value is less than the element, the search continues in the lower half of the array. If the target value is greater than the element, the search continues in the upper half of the array. By doing this, the algorithm eliminates the half in which the target value cannot lie in each iteration. 

Read more here : https://en.wikipedia.org/wiki/Binary_search_algorithm
>>>>>>> 6dcf0f34bf9ab34d75640c16a191fa6e1663acb5

The important caveat about quicksort is that its worst-case performance is $O(n^2)$. The most complex issue in quicksort is thus choosing a good pivot element, as consistently poor choices of pivots can result in drastically slower performance, but good choice of pivots yields $O(n*log(n))$ performance, which is asymptotically optimal.

# Contribution 
Feel free to add any other algorithm and suggest a better implementation of the above coded algorithm.
