def bucket_sort(input_list): # sort from max to min
    max_value = max(input_list) # Find maximum value in the list and use length of the list to determine which value in the list goes into which bucket 
    size = max_value/len(input_list)

    buckets_list= []  # Create n empty buckets where n is equal to the length of the input list
    for x in range(len(input_list)):
        buckets_list.append([]) 

    for i in range(len(input_list)): # Put list elements into different buckets based on the size
        j = int (input_list[i] / size)
        if j != len (input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

    for z in range(len(input_list)): # Sort elements within the buckets using Insertion Sort
        inseration_sort(buckets_list[z])
            
    final_output = [] # Concatenate buckets with sorted elements into a single list
    for x in range(len (input_list)):
        final_output = final_output + buckets_list[x]
    return final_output

def inseration_sort(bucket):
    for i in range(1, len(bucket)):
        var = bucket[i]
        j = i - 1
        while j >= 0 and var < bucket[j]:
            bucket[j+1] = bucket[j]
            j = j - 1
        bucket[j+1] = var

##### MAIN #####

myList = input("Enter your list : ")
myList = myList.split()
myList = [float(x) for x in myList]

bucket_sort(myList)

print(myList)