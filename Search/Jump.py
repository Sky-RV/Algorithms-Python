import math

def jump(arr, index, n):
    step = math.sqrt(n)
    prev = 0
    while arr[int(min(step, n)-1)] < index:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1
    while arr[int(prev)] < index:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[int(prev)] == index:
        return prev
    return -1

##### MAIN #####

myList = input("Enter your list : ")
myList = myList.split()
myList = [int(x) for x in myList]

key = int(input("Enter the Key : "))

answer = jump(myList, key, len(myList))

print(int(answer))