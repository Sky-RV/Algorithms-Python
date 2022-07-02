def gnome_sort(arr, n):
    index = 0
    while index < n:
        if index == 0:
            index += 1
        if arr[index] >= arr[index-1]:
            index += 1
        else:
            arr[index], arr[index-1] = arr[index-1], arr[index]
            index -= 1
    return arr

##### MAIN #####

myList = input("Enter your list : ")
myList = myList.split()
myList = [int(x) for x in myList]

gnome_sort(myList, len(myList))

print(myList)