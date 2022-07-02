def heap_ify(arr, n, i): # n => heap size and heapify subtree rooted at index i
    largest = i # initialize largest as root
    l = 2 * i + 1 # left
    r = 2 * i + 2 # right
    if l < n and arr[i] < arr[l]: # if left child of the root is greater than root
        largest = l
    if r < n and arr[largest] < arr[r]: # if right child of root is greater that the root
        largest = r
    if largest != i: # change root
        arr[i], arr[largest] = arr[largest], arr[i]
    
def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2-1, -1, -1): # build max heap since the last parent will be at ((n..2)-1) we can start at that location
        heap_ify(arr, n, i)
    for i in range(n-1, 0, -1): # extract elements one by one
        arr[i], arr[0] = arr[0], arr[i]
        heap_ify(arr, i, 0)
        
##### MAIN #####

myList = input("Enter your list : ")
myList = myList.split()
myList = [int(x) for x in myList]

heap_sort(myList)

print(myList)