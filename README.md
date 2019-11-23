# Sorting-Algorithm
This folder will contains my implementation of some sorting algorithm from scratch.  

## QuickSort
Quicksort is a divide and conquer algorithm which relies on a partition operation: to partition an array, an element called a pivot is selected. All elements smaller than the pivot are moved before it and all greater elements are moved after it. 

### Efficiency 
This can be done efficiently in linear time and in-place. The lesser and greater sublists are then recursively sorted. This yields average time complexity of O(n log n), with low overhead, and thus this is a popular algorithm. Efficient implementations of quicksort (with in-place partitioning) are typically unstable sorts and somewhat complex, but are among the fastest sorting algorithms in practice. Together with its modest O(log n) space usage, quicksort is one of the most popular sorting algorithms and is available in many standard programming libraries.

The important caveat about quicksort is that its worst-case performance is $O(n^2)$. The most complex issue in quicksort is thus choosing a good pivot element, as consistently poor choices of pivots can result in drastically slower performance, but good choice of pivots yields $O(n*log(n))$ performance, which is asymptotically optimal.

# Contribution 
Feel free to add any other algorithm and suggest a better implementation of the above coded algorithm.
