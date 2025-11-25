# algo
> Bunch of algorithms and data structures.

Understanding time complexity helps optimize algorithms by analyzing how runtime grows with input size.  
The growth of runtime in relation to input size is represented with Big O notation.  
Here's an example: O(1), runtime will take the same amount of time (1) no matter the input size!

## ToC
- [Algorithms](README#Algorithms)
- [Data Structures](<README#Data structures>)
- [Encoding](README#Encoding)
- [Real World](<README#Real world>)
- [Takeaways](README#Takeaways)

## Algorithms
In [algorithms.py](./algorithms.py).

### Search
| Algorithm | Time Complexity | Notes |
|-----------|-----------------|-------|
| Simple Search | O(n) | Linear search through each element, works on unsorted data |
| Binary Search | O(log n) | Way faster then Simple Search, but requires sorted data |
| Depth-First Search (DFS) | O(V + E) where <br> V = "vertices" <br> and E = "edges" | Uses a stack to find a path in unweighted graphs by exploring nodes as deep as possible before backtracking, good for cycle detection |
| Breadth-First Search (BFS) | O(V + E) where <br> V = "vertices" <br> and E = "edges" | Uses a queue to find the shortest path in unweighted graphs by exploring each branch by a certain depth before going deeper |
| A* Search | O(b^d) <br> where b = "branching factor" <br> and d = "depth" | Uses admissible heuristics (domain's problem specific) to find the optimal path in weighted graphs |

### Sort
| Algorithm | Time Complexity | Notes |
|-----------|-----------------|-------|
| Selection Sort | O(n^2) | In-place comparison sort, finds minimum element each iteration |
| Quick Sort | O(n * log n) average case <br> and O(n^2) worst case | Divide and conquer |
<!-- | Bubble Sort | O(n^2) | In-place, repeatedly swaps adjacent elements, stable | -->
<!-- | Merge Sort | O(n * log n) | Divide and conquer, stable, good for external sorting | -->
<!-- | Heap Sort | O(n * log n) | In-place, uses binary heap data structure, not stable | -->
<!-- | Radix Sort | O(n * k) where k = "number of digits " | Non-comparative digit-by-digit sorting | -->

> [!NOTE]
> Quick Sort worst case is bad and can happen as most implementation are entirely deterministic.  
> Luckily, we can force it to run in quadratic time to avoid this and always get avarage case!  
> Refer to [Killing Quicksort](https://research.swtch.com/qsort) by Russ Cox.

### Additional
| Algorithm | Time Complexity | Notes |
|-----------|-----------------|-------|
| Factorial | O(n) | Recursive computation |
| Ackermann | Non-elementary (super-exponential) | Grows faster then any other primitive recursive function |
<!-- | Traveling Salesman | O(n! * n^2) | A classic computing difficult problem | -->
<!-- | Fibonacci | O(2^n) naive, O(n) DP | Exponential naive recursion | -->
<!-- | Prime Check | O(√n) | Check divisibility up to square root of n | -->
<!-- | Hashing | O(1) average | Constant time lookup with a simple hash function | -->
<!-- | Byzantine Fault Tolerance | O(n²) | Message complexity for distributed consensus | -->

Find more on [Rosetta Code](https://rosettacode.org/wiki/Rosetta_Code)!

## Data structures
In [structures.py](./structures.py)

### Arrays

| Operation | Time Complexity | Notes |
|-----------|-----------------|-------|
| Access | O(1) | Direct indexing |
| Search | O(n) | Linear search |
| Insertion | O(n) | Requires shifting elements |
| Deletion | O(n) | Requires shifting elements |

### Linked Lists

| Operation | Time Complexity | Notes |
|-----------|-----------------|-------|
| Access | O(n) | Must traverse from head |
| Search | O(n) | Linear search |
| Insertion | O(1) | If you have the reference |
| Deletion | O(1) | If you have the reference |

### Queues
A FIFO (first in, first out) structure.

| Structure | Operation | Time Complexity |
|-----------|-----------|-----------------|
| Queue | Enqueue | O(1) |
| Queue | Dequeue | O(1) |

### Stacks
A LIFO (last in, last out) structure.

| Structure | Operation | Time Complexity |
|-----------|-----------|-----------------|
| Stack | Push | O(1) | LIFO structure |
| Stack | Pop | O(1) | LIFO structure |

### Hash Tables
Often used to implement graphs!

| Operation | Average | Worst Case | Notes |
|-----------|---------|------------|-------|
| Access | O(1) | O(n) | With a good hash function |
| Search | O(1) | O(n) | Collisions affect performance |
| Insertion | O(1) | O(n) | Load factor important |
| Deletion | O(1) | O(n) | Depends on collision resolution |

#### Directed Graph
A type graph where nodes have directions.  

#### Weighted Graphs
A type graph where nodes have weight assiged to them.

### Trees
A type of graph without cycles.

#### Binary Trees
Trees with no more than 2 children per node!

> [!NOTE]
> Data structures like SQLite's B+ trees make searches faster by organizing data efficiently.

## Encoding
```
As this example will show you, there are many different ways to encode characters.
That is, the letter a could be written in binary in many different ways.
It started with ASCII. In the 1960s, ASCII was created. ASCII is a 7-bit encoding.
Unfortunately, ASCII did not include a lot of characters.
ASCII does not include any characters with umlauts (ü or ö, for example) or common currencies like the British Pound or Japanese Yen.
ISO-8859-1 was created because of this. ISO-8859-1 is an 8-bit encoding meaning it doubles in total characters number!
We went from 128 characters to 256 characters, but this was still not enough and countries began making their own encodings.
Japan has several encodings for Japanese since ISO-8859-1 and ASCII were focused on European languages.

The whole situation was a mess until Unicode was introduced.
Unicode is another encoding standard. It aims to provide characters for any language.
Unicode has 149,186 characters as of version 15, quite a jump from 256 (more than 1,000 of these are emojis).
Unicode is the standard, but you need to use an encoding that follows the standard. The most popular encoding today is UTF-8.
UTF-8 is variable-length character encoding, which means characters can be anywhere from 1 to 4 bytes (8–32 bits).

Compression algorithms like (Huffman coding) try to reduce the number of bits needed to store each character.
```

## Real world
Example, optimizing the time complexity for an important production API endpoint.  
Passing from the handler to the store and the database!

<!-- Damn, it would have been nice a computer calculated time complexity for us, can it? -->  
<!-- Kind of with complexity analysis, benchmarking and profiling! -->

## Takeaways
1. Think about time complexity while refactoring.
2. If you can't optimize for time, optimize for size!
3. Your default encoding should be UTF-8.

Most of this knowledge comes from [Grokking Algorithms](https://www.manning.com/books/grokking-algorithms).

