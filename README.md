# Grokking Algorithms Study

A comprehensive study repository implementing algorithms and data structures from the book "Grokking Algorithms" by Aditya Bhargava.

## Overview

This repository contains implementations of fundamental algorithms and data structures with practical exercises, organized by chapters. The goal is to understand algorithmic thinking and computational complexity through hands-on coding practice.

## Repository Structure

```text
├── chapter-1/              # Introduction to Algorithms
│   └── exercises/
│       ├── javascript/     # JavaScript implementations
│       │   └── binarySearch.js
│       └── python/         # Python implementations
│           ├── binarySearch.py
│           └── exercise1.py
├── chapter-2/              # Selection Sort
│   ├── arrays_lists.md     # Theory notes on arrays vs linked lists
│   └── exercises/
│       └── selectedSorted.py
└── README.md
```

## Implemented Algorithms

### Chapter 1: Introduction to Algorithms

#### Binary Search

- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)
- **Languages**: Python, JavaScript

**Description**: Efficient search algorithm for sorted arrays that repeatedly divides the search interval in half.

**Files**:

- `chapter-1/exercises/python/binarySearch.py` - Basic implementation
- `chapter-1/exercises/python/exercise1.py` - Enhanced version with operation counter
- `chapter-1/exercises/javascript/binarySearch.js` - JavaScript implementation

### Chapter 2: Selection Sort

#### Selection Sort

- **Time Complexity**: O(n²)
- **Space Complexity**: O(n) - due to creating new array
- **Language**: Python

**Description**: Simple sorting algorithm that finds the minimum element and places it at the beginning.

**Files**:

- `chapter-2/exercises/selectedSorted.py` - Implementation with helper function

## Key Concepts Covered

### Data Structures

- **Arrays**: Contiguous memory allocation, O(1) random access
- **Linked Lists**: Non-contiguous memory, O(1) insertion/deletion

### Algorithm Analysis

- **Big O Notation**: Understanding algorithmic efficiency
- **Time vs Space Tradeoffs**: Analyzing computational complexity

### Comparison: Arrays vs Linked Lists

| Operation | Arrays | Linked Lists |
|-----------|--------|--------------|
| Reading   | O(1)   | O(n)         |
| Insertion | O(n)   | O(1)         |
| Deletion  | O(n)   | O(1)         |

## Getting Started

### Prerequisites

- Python 3.7+
- Node.js (for JavaScript implementations)

### Running the Code

#### Python Examples

```bash
# Binary Search
python chapter-1/exercises/python/binarySearch.py

# Binary Search with counter
python chapter-1/exercises/python/exercise1.py

# Selection Sort
python chapter-2/exercises/selectedSorted.py
```

#### JavaScript Examples

```bash
# Binary Search
node chapter-1/exercises/javascript/binarySearch.js
```

## Learning Objectives

- [ ] Understand algorithmic complexity analysis
- [ ] Master fundamental search algorithms
- [ ] Implement basic sorting algorithms
- [ ] Compare data structure performance characteristics
- [ ] Apply Big O notation for algorithm evaluation

## Notes and Theory

Theoretical concepts and explanations are documented in markdown files:

- `chapter-2/arrays_lists.md` - Comprehensive comparison of arrays and linked lists

## Future Chapters

This repository will be expanded to include:

- Recursion and Divide & Conquer
- Hash Tables
- Breadth-First Search
- Dijkstra's Algorithm
- Greedy Algorithms
- Dynamic Programming
- K-nearest neighbors

## Contributing

This is a personal study repository. However, if you find any bugs or have suggestions for improvements, feel free to open an issue.

## References

- **Book**: "Grokking Algorithms" by Aditya Bhargava
- **Publisher**: Manning Publications
- **Focus**: Visual and intuitive approach to algorithms

## License

This project is for educational purposes only.
