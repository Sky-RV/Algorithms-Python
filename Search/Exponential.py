def binary(arr, left, right, index):
    if right >= left:
        mid = left + (right - left) // 2
        if arr[mid] == index:
            return mid
        if arr[mid] > index:
            return binary(arr, left, mid-1, index)
        return binary(arr, mid+1, right, index)
    return -1

def exponential(arr, index, n):
    if arr[0] == index:
        return 0
    i = 1
    while i < n and arr[i] <= index:
        i = i * 2
    return binary(arr, i//2, min(i, n-1), index)

##### MAIN #####

myList = input("Enter your list : ")
myList = myList.split()
myList = [int(x) for x in myList]

key = int(input("Enter the Key : "))

answer = exponential(myList, key, len(myList))

print(answer)