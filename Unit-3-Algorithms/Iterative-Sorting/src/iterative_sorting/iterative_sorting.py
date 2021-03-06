# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # select smallest, bring to the front
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # series of swaps between adjacent elements, gradually
    # moving larger elements towards end of array

    # loop through array
        # compare each element to its neighbor
        # if element is in the wrong position, swap them
    # if no swaps needed, stop
    # else return to the element at index 0 and repeat step 1
    swap_count = 0
    is_unsorted = True

    if len(arr):
        while is_unsorted:
            for i, num in enumerate(arr):
                if num == arr[-1]:
                    if swap_count == 0:
                        is_unsorted = False
                    else:
                        swap_count = 0
                else:
                    if num > arr[i+1]:
                        arr[i], arr[i+1] = arr[i+1], arr[i]
                        swap_count += 1

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
# def counting_sort(arr, maximum=None):
#     # time: O(n+k)
#     # space: O(k)
#     if len(arr):

#     return arr
