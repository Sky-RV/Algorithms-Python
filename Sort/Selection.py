def selecftion_sort(myList):
    for i in range(len(myList)): # transfer through all list elements
        min_index = i # find the min element in remaining
        for j in range(i+1, len(myList)):
            if myList[min_index] > myList[j]:
                min_index = j
        myList[i], myList[min_index] = myList[min_index], myList[i]
        
##### MAIN #####

myList = input("Enter your list : ")
myList = myList.split()
myList = [int(x) for x in myList]

selecftion_sort(myList)

print(myList) 