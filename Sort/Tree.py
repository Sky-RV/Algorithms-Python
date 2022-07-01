class Node: # contain left and right child of the current node and key value
    def __init__(self, item = 0):
        self.key = item
        self.left, self.right = None, None
        
root = Node() # root of binary search tree (bst)
root = None

def insert(key):
    global root
    root = insertRec(root, key)
    
def insertRec(root, key): # a riculsive function to insert a new key in bst
    if root == None: # if tree is empty return a new node
        root = Node(key)
        return root
    if key < root.key:
        root.left = insertRec(root.left, key)
    elif key > root.key: # if tree is not empty recursive down the tree
        root.right = insertRec(root.right, key)
    return root

def inorderRec(root): # to traversal of bst
    if root != None:
        inorderRec(root.left)
        print(root.key, end=" ")
        inorderRec(root.right)
        
def tree_sort(myList):
    for i in range(len(myList)):
        insert(myList[i])
        
##### MAIN #####

myList = input("Enter your list : ")
myList = myList.split()
myList = [int(x) for x in myList]

tree_sort(myList)
inorderRec(root)