# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # check for smaller num between cur_index and length of the arra
        for y in range(cur_index, len(arr)):
            #if a number is smaller than cur_index make that the new smallest_index
            if arr[y] < arr[smallest_index]:
                smallest_index = y

        # TO-DO: swap
        #declare smallest number(arr[smallest_index]) as a variable
        smallest_num = arr[smallest_index]
        # swap smallest num with the num in the current index position
            #assign number in the cur_index position to the smallest_index postion
        arr[smallest_index] = arr[cur_index]
            #assign smallest num to the cur_index position
        arr[cur_index] = smallest_num
        




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr