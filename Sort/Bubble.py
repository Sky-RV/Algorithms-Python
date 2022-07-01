# Implementation
from math import fabs


def bubble_sort_I(myList):
    for i in range(len(myList)):
        for j in range(len(myList) - 1):
            if myList[j] > myList[j+1]:
                myList[j], myList[j+1] = myList[j+1], myList[j]
                
# Optimization 1
def bubble_sort_O1(myList):
    swap = True
    while (swap):
        swap = False
        for i in range(len(myList) - 1):
            if myList[i] > myList[i+1]:
                myList[i], myList[i+1] = myList[i+1], myList[i]
                swap = True
                
                
# Optimization 2
def bubble_sort_O2(myList):
    swap = True
    interactions = 0
    while (swap):
        swap = False
        for i in range(len(myList) - interactions - 1):
            if myList[i] > myList[i+1]:
                myList[i], myList[i+1] = myList[i+1], myList[i]
                swap = True
        interactions += 1

##### MAIN #####

myList = input("Enter your list : ")
myList = myList.split()
myList = [int(x) for x in myList]


bubble_sort_I(myList)
# bubble_sort_O1(myList)
# bubble_sort_O2(myList)

print(myList)