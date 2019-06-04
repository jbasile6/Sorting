# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a_index = 0
    b_index = 0
    for x in range(0, elements):
        # make sure the a_index and b_index stay within the range
        if a_index >= len(arrA):
            # all of arrA is added to merged_arr, add the next arrB item to merged_arr and increase b_index by 1
            merged_arr[x] = arrB[b_index]
            b_index += 1
        elif b_index >= len(arrB):
            # all of arrB is added to merged_arr, add the next arrA item to merged_arr and increase a_index by 1
            merged_arr[x] = arrA[a_index]
            a_index += 1


            # compare the item at a_index in arrA to the item at b_index in arrB: check for A is smaller 
        elif arrA[a_index] < arrB[b_index]:
            #if 0 item in arrA is smaller, it is the first item in the merged_arr, move a_index to next spot
            merged_arr[x] = arrA[a_index]
            a_index += 1
        else: # check for B is smaller
            #if 0 item in arrB is smaller, it is first in merged_arr, move b_index to next spot
            merged_arr[x] = arrB[b_index]
            b_index += 1
        
    return merged_arr

print(merge([1,2,5], [4,8,9]))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # if the array length is larger than 1 split in half
    if len(arr) <= 1:
        return arr
    else:
        return merge_sort([x for x in arr[1:] if x <= arr[0]]) + [arr[0]] + merge_sort([y for y in arr[1:] if y > arr[0]])

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
