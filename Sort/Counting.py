def counting_sort(arr):
    size = len(arr)
    output = [0] * size
    count = [0] * 10 # count array initialization

    for m in range(0, size): # storing the count of each element 
        count[arr[m]] += 1

    for m in range(1, 10): # storing the cumulative count
        count[m] += count[m - 1]

    # place the elements in output array after finding the index of each element of original array in count array
    m = size - 1
    while m >= 0:
        output[count[arr[m]] - 1] = arr[m]
        count[arr[m]] -= 1
        m -= 1

    for m in range(0, size):
        arr[m] = output[m]
        
        
##### MAIN #####

myList = input("Enter your list : ")
myList = myList.split()
myList = [int(x) for x in myList]

counting_sort(myList)

print(myList)