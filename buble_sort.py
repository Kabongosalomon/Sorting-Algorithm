import ipdb
import time

def buble_sort_naive(l):
    """
    We start with this naive approach that just check if element close by
    and update the boolean variable and swap accondingly 

    The complexity of this algorithm is O(n^2)
    """
    swap = True
    while swap:
        swap = False
        for i in range(len(l)-1):
            if l[i]>l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                swap = True
    return l

def buble_sort_imp_1(l):
    """
    Te idea here is that by doing the first run, the biggest element will
    be the last element in the list, and that is definitly is 
    best position, so no need to try to swap him again. 

    The complexity of this algorithm is O(?)
    """
    swap = True
    n = len(l)
    while swap:
        swap = False
        for i in range(n-1):
            if l[i]>l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                swap = True
        n-=1
    return l

def buble_sort_imp_2(l):
    """
    More generally, it can happen that more than one element 
    is placed in their final position on a single pass. 
    In particular, after every pass, all elements after the last swap 
    are sorted, and do not need to be checked again. 
    
    This allows to skip over many elements, resulting 
    in about a worst case 50% improvement in comparison 
    count (though no improvement in swap counts), 
    and adds very little complexity because the new code 
    subsumes the "swapped" variable 

    The complexity of this algorithm is O(?)
    """
    n = len(l)
    number = None
    while number!=0:
        number = 0
        for i in range(n-1):
            if l[i]>l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                number = i+1
        n=number
    return l

example_1 = [5, 1, 4, 2, 8]
# print(buble_sort_naive(example_1))
# print(buble_sort_imp_1(example_1))
print(buble_sort_imp_2(example_1))

    