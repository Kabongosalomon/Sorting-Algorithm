"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
<<<<<<< HEAD
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
=======
    if len(array)==1:
        return array[0:]

    pivot_indx = len(array)-1
    still = True
    low_idx = 0
    high_idx = pivot_indx
    i = 0
    # while still :
    while(low_idx < pivot_indx):
        if array[i] > array[pivot_indx] :
            temp = array[i]
            array[i]=array[pivot_indx-1] 
            array[pivot_indx-1] = array[pivot_indx]
            array[pivot_indx] = temp
            pivot_indx-=1
        else:
            i+=1
            low_idx+=1
            
    return quicksort(array[:pivot_indx])+ quicksort(array[pivot_indx:])
>>>>>>> 6dcf0f34bf9ab34d75640c16a191fa6e1663acb5

# test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
test = [8, 3, 1, 7, 0, 10, 2]

<<<<<<< HEAD
print quicksort(test)
=======
print(quicksort(test))
>>>>>>> 6dcf0f34bf9ab34d75640c16a191fa6e1663acb5
