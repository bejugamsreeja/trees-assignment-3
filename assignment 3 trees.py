#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Implement Binary tree

class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):
# Compare the new value with the parent node
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
               if self.right is None:
                  self.right = Node(data)
               else:
                  self.right.insert(data)
      else:
         self.data = data

# Print the tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()


# In[2]:


# Find height of a given tree

class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
# Recursive function to calculate the height of a given binary tree
def height(root):
 
    # base case: empty tree has a height of 0
    if root is None:
        return 0
 
    # recur for the left and right subtree and consider maximum depth
    return 1 + max(height(root.left), height(root.right))
 
 
if __name__ == '__main__':
 
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)
 
    print('The height of the binary tree is', height(root))


# In[3]:


# Perform Pre-order, Post-order, In-order traversal

class node:
    def __init__(self,c):
        self.data=c
        self.left=self.right=None
 
# Function to recursively build the expression tree
def add(a):
 
    # If its the end of the expression
    if (a == ''):
        return ''
 
    # If the character is an operand
    if a[0]>='a' and a[0]<='z':
        return node(a[0]),a[1:]
    else:
        # Create a node with a[0] as the data and
        # both the children set to null
        p=node(a[0])
        # Build the left sub-tree
        p.left,q=add(a[1:])
        # Build the right sub-tree
        p.right,q=add(q)
        return p,q
         
 
# Function to print the infix expression for the tree
def inr(p): #recursion
 
    if (p == None):
        return
    else:
        inr(p.left)
        print(p.data,end=' ')
        inr(p.right)
 
# Function to print the postfix expression for the tree
def postr(p):
 
    if (p == None):
        return
    else:
        postr(p.left)
        postr(p.right)
        print(p.data,end=' ')
 
# Driver code
if __name__ == '__main__':
     
    a = "*+ab-cd"
    s,a=add(a)
    print("The Infix expression is:")
    inr(s)
    print()
    print("The Postfix expression is:")
    postr(s)


# In[4]:


#BFS
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')


# In[5]:


#DFS
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')


# In[6]:


class Node:
    # Constructor to create a new Node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
# A utility function to check if a given node is leaf or not
def isLeaf(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return False
 
# This function return sum of all left leaves in a
# given binary tree
def leftLeavesSum(root):
 
    # Initialize result
    res = 0
     
    # Update result if root is not None
    if root is not None:
 
        # If left of root is None, then add key of
        # left child
        if isLeaf(root.left):
            res += root.left.key
        else:
            # Else recur for left child of root
            res += leftLeavesSum(root.left)
 
        # Recur for right child of root and update res
        res += leftLeavesSum(root.right)
    return res
 
# Driver program to test above function
 
# Let us construct the Binary Tree shown in the above function
root = Node(20)
root.left = Node(9)
root.right = Node(49)
root.right.left = Node(23)       
root.right.right = Node(52)
root.right.right.left = Node(50)
root.left.left = Node(5)
root.left.right = Node(12)
root.left.right.right = Node(12)
print ("Sum of left leaves is", leftLeavesSum(root))
 
     


# In[7]:


def SumNodes(l):
     
    leafNodeCount = pow(2, l - 1)
    vec = [[] for i in range(l)]
 
    for i in range(1, leafNodeCount + 1):
        vec[l - 1].append(i)
    for i in range(l - 2, -1, -1):
        k = 0
        while (k < len(vec[i + 1]) - 1):
            vec[i].append(vec[i + 1][k] +
                          vec[i + 1][k + 1])
            k += 2
 
    Sum = 0
    for i in range(l):
        for j in range(len(vec[i])):
            Sum += vec[i][j]
 
    return Sum
 

if __name__ == '__main__':
    l = 3
 
    print(SumNodes(l))


# In[8]:


class getNode:
    def __init__(self, data):
 
        # put in the data
        self.data = data
        self.left = self.right = None
 
# function to count subtrees that
# Sum up to a given value x
 
 
def countSubtreesWithSumX(root, count, x):
 
    # if tree is empty
    if (not root):
        return 0
 
    # Sum of nodes in the left subtree
    ls = countSubtreesWithSumX(root.left,
                               count, x)
 
    # Sum of nodes in the right subtree
    rs = countSubtreesWithSumX(root.right,
                               count, x)
 
    # Sum of nodes in the subtree
    # rooted with 'root.data'
    Sum = ls + rs + root.data
 
    # if true
    if (Sum == x):
        count[0] += 1
 
    # return subtree's nodes Sum
    return Sum
 
# utility function to count subtrees
# that Sum up to a given value x
 
 
def countSubtreesWithSumXUtil(root, x):
 
    # if tree is empty
    if (not root):
        return 0
 
    count = [0]
 
    # Sum of nodes in the left subtree
    ls = countSubtreesWithSumX(root.left,
                               count, x)
 
    # Sum of nodes in the right subtree
    rs = countSubtreesWithSumX(root.right,
                               count, x)
 
    # if tree's nodes Sum == x
    if ((ls + rs + root.data) == x):
        count[0] += 1
 
    # required count of subtrees
    return count[0]
 
 
# Driver Code
if __name__ == '__main__':
 
    # binary tree creation
    #         5
    #         / \
    #     -10     3
    #     / \ / \
    #     9 8 -4 7
    root = getNode(5)
    root.left = getNode(-10)
    root.right = getNode(3)
    root.left.left = getNode(9)
    root.left.right = getNode(8)
    root.right.left = getNode(-4)
    root.right.right = getNode(7)
 
    x = 7
 
    print("Count =",
          countSubtreesWithSumXUtil(root, x))
 


# In[9]:


from collections import deque
 
# A binary tree node has data, pointer
# to left child and a pointer to right
# child
class Node:
     
    def __init__(self, key):
         
        self.data = key
        self.left = None
        self.right = None
 
# Function to find the maximum sum
# of a level in tree
# using level order traversal
def maxLevelSum(root):
     
    # Base case
    if (root == None):
        return 0
 
    # Initialize result
    result = root.data
     
    # Do Level order traversal keeping
    # track of number
    # of nodes at every level.
    q = deque()
    q.append(root)
     
    while (len(q) > 0):
         
        # Get the size of queue when the
        # level order traversal for one
        # level finishes
        count = len(q)
 
        # Iterate for all the nodes in
        # the queue currently
        sum = 0
        while (count > 0):
             
            # Dequeue an node from queue
            temp = q.popleft()
 
            # Add this node's value to current sum.
            sum = sum + temp.data
 
            # Enqueue left and right children of
            # dequeued node
            if (temp.left != None):
                q.append(temp.left)
            if (temp.right != None):
                q.append(temp.right)
                 
            count -= 1   
 
        # Update the maximum node count value
        result = max(sum, result)
 
    return result
     
# Driver code
if __name__ == '__main__':
     
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(8)
    root.right.right.left = Node(6)
    root.right.right.right = Node(7)
 
    # Constructed Binary tree is:
    #              1
    #            /   \
    #          2      3
    #        /  \      \
    #       4    5      8
    #                 /   \
    #                6     7   
    print("Maximum level sum is", maxLevelSum(root))


# In[10]:


class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
def printOddNodes(root, isOdd = True):
     
    # If empty tree
    if (root == None):
        return
 
    # If current node is of odd level
    if (isOdd):
        print(root.data, end = " ")
 
    # Recur for children with isOdd
    # switched.
    printOddNodes(root.left, not isOdd)
    printOddNodes(root.right, not isOdd)
 
# Driver code
if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    printOddNodes(root)
     


# In[ ]:




