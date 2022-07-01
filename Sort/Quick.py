def partition(l, r, num):
    pivot, ptr = num[r], l #last element is pivot and first element is pointer
    for i in range(l, r):
        if num[i] <= pivot:
            num[i], num[ptr] = num[ptr], num[i]
            ptr += 1
    num[ptr], num[r] = num[r], num[ptr]
    return ptr

def quick_sort(l, r, num):
    if len(num) == 1:
        return num
    if l < r:
        pi = partition(l, r, num)
        quick_sort(l, pi-1, num) # recursively sorting the left values
        quick_sort(pi+1, r, num) # rescursively sorting the right values
    return num

##### MAIN #####

myList = input("Enter your list : ")
myList = myList.split()
myList = [int(x) for x in myList]

quick_sort(0, len(myList)-1, myList)

print(myList)  