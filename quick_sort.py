"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    pivot_indx = len(array)
    still = True
    low_idx = 0
    high_idx = pivot_indx
    while still :
        for i in range(low_idx, high_idx):
            if array[i] > array[pivot_indx] :
                temp = array[i]
                array[i]=array[pivot_indx-1] 
                array[pivot_indx-1] = array[pivot_indx]
                array[pivot_indx] = temp
                break
        


    return []

# test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
test = [8, 3, 1, 7, 0, 10, 2]

print quicksort(test)