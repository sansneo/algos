# Test
# Run the algorithms!

import algorithms
import structures

# Search
print('Simple Search O(n) (target, pos) --> ', algorithms.simple_search(structures.unsorted_array, 1))
print('Binary Search O(log n) (target, pos) --> ', algorithms.binary_search(structures.sorted_array, 3))
print('Breadth First Search O(V+E) (path, distance) --> ', algorithms.breadth_first_search(structures.directed_graph, 'Albi', 'God', None))
print('Depth First Search O(V+E) (path, distance) --> ', algorithms.depth_first_search(structures.directed_graph, 'Albi', 'Elisa', 2))

def straight_line_heuristic(city, target):
    """
    Straight-line distance heuristic for European cities (in km)
    """
    straight_line_distances = {
        'Paris': {'Paris': 0, 'London': 343, 'Berlin': 878},
        'London': {'Paris': 343, 'London': 0, 'Berlin': 933},
        'Berlin': {'Paris': 878, 'London': 933, 'Berlin': 0}
    }
    return straight_line_distances[city][target]
print('A-Star Search O(b^v) (path, cost) --> ', algorithms.a_star_search(structures.weighted_graph, "Paris", "Berlin", straight_line_heuristic))

# Sort
print('Selection Sort O(n) (sorted) --> ', algorithms.selection_sort(structures.unsorted_list))

algorithms.quick_sort(structures.unsorted_list, 0, None)
print('Quick Sort O(n * log n) avarage and O(n^2) worst case (none) --> ', structures.unsorted_list)

# Additional
print('Factorial O(n * log n) (factorial) --> ', algorithms.factorial(5))
print('Ackermann (managable) O(A(M, N) (value) --> ', algorithms.ackermann(4, 2))
print('Ackermann (double recursioon) O(A(M, N) (value) --> ', algorithms.ackermann(2, algorithms.ackermann(4, 2)))
