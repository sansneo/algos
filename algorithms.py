from collections import deque
import heapq

# ###### #
# Search #
# ###### #

# Simple Search O(n)
# Requires an unsorted array.
def simple_search(arr, target):
    """
    Simple Search on an array
    Time complexity: O(n)
    
    Args:
        arr: List of elements to search through
        target: Element to find
        
    Returns:
        The target and it's position if found, None otherwise
    """
    for pos, v in enumerate(arr):
        if v == target:
            return v, pos
    return None

# Binary Search O(log n)
# Requires a sorted array.
def binary_search(arr, target):
    """
    Binary Search on a sorted array
    Time complexity: O(log n)
    
    Args:
        arr: Sorted list of elements
        target: Element to find
        
    Returns:
        The target and it's position if found, None otherwise
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return guess, mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return (None, -1)

# Breadth First Search O(V+E) where V is "number of nodes" and E is "number of edges" (out-neighbours connections)
# Requires a Graph. Uses a Queue.
def breadth_first_search(graph, start, target, max_depth=None):
    """
    Breadth First Search (BFS) on a Directed Graph.
    Goes through all the node's neighbours recursively until max depth if set.
   
    Args:
        graph: Dictionary Directed Graph representation {node: [neighbors]}
        start: Starting node
        target: Node to find
        max_depth: Maximum depth (None = limitless)
        
    Returns:
        The path and the distance, None otherwise
    """
    if start not in graph:
        return [], -1
    queue = deque([(start, [start], 0)])
    visited = {start} # Tracking visited nodes to avoid cycles
    while queue:
        position, path, distance = queue.popleft()
        # Max depth check
        if max_depth is not None and distance > max_depth:
            continue
        # Target node found
        if position == target:
            return path, distance
        # Exploring all neighbors at the current depth level
        for neighbor in graph.get(position, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor], distance + 1))
    return [], -1

# Depth First Search O(V+E) where V is "number of nodes" and E is "number of edges"
# Requires a Graph. Uses a Stack.
def depth_first_search(graph, start, target, max_depth=None):
    """
    Depth First Search (DFS) on a Directed Graph.
    Goes as deep as possible along each branch before backtracking.
   
    Args:
        graph: Dictionary Directed Graph representation {node: [neighbors]}
        start: Starting node
        target: Node to find
        max_depth: Maximum depth (None = limitless)
        
    Returns:
        The path and the distance, None otherwise
    """
    if start not in graph:
        return [], -1
    stack = [(start, [start], 0)]
    visited = {start}
    while stack:
        position, path, distance = stack.pop()
        # Target node found
        if position == target:
            return path, distance
        # Max depth check
        if max_depth is not None and distance >= max_depth:
            continue
        # Exploring neighbors left to right
        for neighbor in reversed(graph.get(position, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor], distance + 1))
    return [], -1

# A-Star Search (A*) O(b^d)
def a_star_search(graph, start, target, heuristic):
    """
    A-Star Search on a Weighted Graph.
    Finds the shortest path using heuristic-guided search.

    Args:
        graph: Dictionary Weighted Graph representation {node: {neighbor: cost}}
        start: Starting node
        target: Node to find
        heuristic: Function that estimates cost from node to target as heuristic(node, target) -> float (domain's problem specific)
                   
    Returns:
        The optimal path and its cost
    """
    if start not in graph:
        return [], float('inf')  # Return infinite cost if not found
    open_set = [(heuristic(start, target), 0, start, [start])]
    heapq.heapify(open_set)
    g_scores = {start: 0}
    closed_set = set()  # Explored nodes
    while open_set:
        # Get the node with the best score
        current_f, current_g, current_node, path = heapq.heappop(open_set)
        if current_node in closed_set: # Skip nodes if explored
            continue
        # Target node found
        if current_node == target:
            return path, current_g  # Return optimal path and its cost
        closed_set.add(current_node) # Mark node as explored
        # Explore all neighbors of the current node
        for neighbor, cost in graph.get(current_node, {}).items():
            if neighbor in closed_set:
                continue
            # Calculate tentative score
            tentative_g = current_g + cost
            # Is this path to the neighbour better than the ones previously found?
            if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, target)
                new_path = path + [neighbor]
                heapq.heappush(open_set, (f_score, tentative_g, neighbor, new_path))
    # No path found
    return [], float('inf')

# #### #
# Sort #
# #### #

# Selection Sort O(n^2)
def selection_sort(unsorted):
    copy = list(unsorted)
    for i in range(len(copy)):
        lowest = i
        for j in range(i + 1, len(copy)):
            if copy[j] < copy[lowest]:
                lowest = j
        copy[i], copy[lowest] = copy[lowest], copy[i]
    return copy

# Quick Sort (in-place, better memory efficency)
def quick_sort(unsorted, low=0, high=None):
    """
    Quick Sort (in-place)
    Time complexity: O(n log n) average, O(n²) worst case
    
    Args:
        arr: List to sort (will be modified in-place)
        low: Starting index (default 0)
        high: Ending index (default len(arr) - 1)
        
    Returns:
        None
    """
    if high is None:
        high = len(unsorted) - 1
    if low < high:
        # Partition
        pivot_index = partition(unsorted, low, high)
        # Recursively sort elements
        quick_sort(unsorted, low, pivot_index - 1)
        quick_sort(unsorted, pivot_index + 1, high)

def partition(arr, low, high):
    """
    Helper function for in-place Quick Sort
    """
    pivot = arr[high]  # Choose last element as pivot
    i = low - 1  # Index of the smaller element
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # Swapping
            arr[i], arr[j] = arr[j], arr[i]
    # Placing pivot
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# ########## #
# Additional #
# ########## #

# Factorial O(n)
# 5! is 5 * 4 * 3 * 2 * 1
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

# Ackermann O(A(M, N))
def ackermann(m, n):
   return (n + 1) if m == 0 else (
      ackermann(m-1, 1) if n == 0 else ackermann(m-1, ackermann(m, n-1)))
