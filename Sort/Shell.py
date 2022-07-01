from re import I


def shell_sort(myList, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = myList[i]
            j = i
            while j >= interval and myList[j-interval] > temp:
                myList[j] = myList[j-interval]
                j -= interval
            myList[j] = temp
        interval //= 2
        
##### MAIN #####

myList = input("Enter your list : ")
myList = myList.split()
myList = [int(x) for x in myList]

shell_sort(myList, len(myList))

print(myList) 