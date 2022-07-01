def merge_sort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2 # the mid of list
        L = myList[:mid] # dividing the list elements
        R = myList[mid:] # intp 2 halves
        merge_sort(L) # sort the first hald
        merge_sort(R) # sort the second half
        i = j = k = 0
        while i < len(L) and j < len(R): # copy data to temp list L[] and R[]
            if L[i] < R[j]:
                myList[k] = L[i]
                i += 1
            else:
                myList[k] = R[j]
                j += 1
            k += 1
        while i < len(L): # checking if any elements was left
            myList[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            myList[k] = R[j]
            j += 1
            k += 1
            
            
##### MaIN #####
   
myList = input("Enter your list : ")
myList = myList.split()
myList = [int(x) for x in myList]

merge_sort(myList)

print(myList)        