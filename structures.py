from array import array
from collections import deque

# Array
unsorted_array = array('i', [3, 1, 2, 5, 1, 4, 7])
sorted_array = array('i', [1, 2, 3, 4, 5, 7])

# List
unsorted_list = [3, 1, 2, 5, 1, 4, 7]
sorted_list = ['Apple', 'Banana', 'Coconut']

# Directed Graph
directed_graph = {
    "Albi": ["Elisa", "Bob", "Claire"],
    "Claire": ["Bob", "God", "Albi"],  # Cycle created here
    "Elisa": [],
    "Bob": [], 
    "God": []
}

# Weighted Graph (European cities distance)
weighted_graph = {
    'Paris': {
        'London': 344,
        'Berlin': 1054
    },
    'London': {
        'Paris': 344,
        'Berlin': 1097
    },
    'Berlin': {
        'Paris': 1054,
        'London': 1097
    }
}

# Queues are FIFO (First In First Out)
queue = deque([1, 2, 3])
queue.append(4)   # enqueue
queue.popleft()   # dequeue

# Stacks are LIFO (Last In Last Out)
stack = [1, 2, 3]
stack.append(4)   # push
stack.pop()       # pop

# Hash Table (Python's implementation of Hash Tables are Dictionaries)
capitals = {"France": "Paris", "UK": "London", "Germany": "Berlin"}

# Trees do not have cycles
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(5)
root.right = Node(15)

# Binary Tree
# A special type of tree where nodes can have at most two children
