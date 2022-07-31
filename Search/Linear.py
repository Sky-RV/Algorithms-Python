# Iterative
def linear(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Recursive 
def linear2(arr, index, key):
    if index == -1:
        return -1
    if arr[index] == key:
        return index
    return linear2(arr, index-1, key)

##### MAIN #####

myList = input("Enter your list : ")
myList = myList.split()
myList = [int(x) for x in myList]

key = int(input("Enter the Key : "))

answer = linear(myList, key)

print(answer)