def binary_search(input_array, value):
    """this function take an input array, and return the index of value 
    if present in the input array or -1 if not"""
    min_index = 0
    max_index = len(input_array)-1
        
    while (min_index<=max_index):
        midle = (min_index+max_index)//2
        if input_array[midle]==value:
            return midle
        elif value > input_array[midle]:
            min_index = midle+1
        else :
            max_index = max_index-1
    return -1
              

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 29
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))

print(binary_search(test_list, -7))
