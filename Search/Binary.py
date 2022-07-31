# Recursive
from re import search


def binary(arr, left, right, index):
    if right >= left:
        mid = left + (right - left) // 2
        if arr[mid] == index:
            return mid
        elif arr[mid] > index:
            return binary(arr, left, mid-1, index)
        else:
            return binary(arr, mid+1, right, index)

    else:
        return -1

# Iterative
def binary2(arr, left, right, index):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == index:
            return mid
        elif arr[mid] < index:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def Binary_Search(alist, key):

    low = 0
    high = len(alist) - 1
    mid = 0

    while low<= high:

        mid = (low + high) // 2

        if alist[mid] < key:
            low = mid + 1

        elif alist[mid] > key:
            high = mid - 1

        else:
            return mid

    return -1

##### MAIN #####

myList = input("Enter your list : ")
myList = myList.split()
myList = [int(x) for x in myList]

key = int(input("Enter the Key : "))

# answer = Binary_Search(myList, key)
answer = binary(myList, 0, len(myList)-1, key)

print(answer)