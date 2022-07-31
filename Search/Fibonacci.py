from bisect import bisect_left
  
def fibonacci(arr, x, n):
  
    fibMMm2 = 0  # (m-2)'th Fibonacci No.
    fibMMm1 = 1  # (m-1)'th Fibonacci No.
    fibM = fibMMm2 + fibMMm1  # m'th Fibonacci
  
    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1
  
    offset = -1
  
    while (fibM > 1):
  
        i = min(offset+fibMMm2, n-1)
  
        if (arr[i] < x):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
  
        elif (arr[i] > x):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
  
        else:
            return i
  
    if(fibMMm1 and arr[n-1] == x):
        return n-1
  
    return -1
  
  
##### MAIN #####

myList = input("Enter your list : ")
myList = myList.split()
myList = [int(x) for x in myList]

key = int(input("Enter the Key : "))

answer = fibonacci(myList, key, len(myList))

print(int(answer))
  