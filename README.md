# graphs_faye

## Overview

`graphs_faye` is a Python library for working with weighted graphs. The library provides an implementation of Dijkstra's shortest path algorithm.

Dijkstra's algorithm finds the shortest paths from a specified source vertex to other vertices in a weighted graph. The implementation uses a min-heap to efficiently determine the next vertex with the smallest known distance.

## Installation

Clone this repository and install the package using `pip`:

```bash
python -m pip install .
```

After installation, the package can be imported with:

```python
from graphs_faye import sp
```

## Using Dijkstra's Algorithm

The `dijkstra()` function is located in the `sp` module.

It takes two arguments:

* `graph`: a dictionary representing a weighted graph
* `source`: the starting vertex

It returns two dictionaries:

* `dist`: the shortest distance from the source to each vertex
* `path`: the shortest-path information for each reachable vertex

### Example

```python
from graphs_faye import sp

graph = {
    0: {1: 4, 7: 8},
    1: {0: 4, 2: 8, 7: 11},
    2: {1: 8, 3: 7, 5: 4, 8: 2},
    3: {2: 7, 4: 9},
    4: {3: 9, 5: 10},
    5: {2: 4, 4: 10, 6: 2},
    6: {5: 2, 7: 1, 8: 6},
    7: {0: 8, 1: 11, 6: 1, 8: 7},
    8: {2: 2, 6: 6, 7: 7}
}

dist, path = sp.dijkstra(graph, 0)

print("Shortest distances:", dist)
print("Shortest paths:", path)
```

## Graph Representation

Graphs are represented using Python dictionaries. Each vertex maps to another dictionary containing its neighboring vertices and the weights of the connecting edges.

For example:

```python
graph = {
    0: {1: 4, 7: 8},
    1: {0: 4, 2: 8}
}
```

This represents a weighted graph in which vertex `0` has an edge to vertex `1` with weight `4` and an edge to vertex `7` with weight `8`. Vertex `1` has edges to vertices `0` and `2`.

## Project Structure

```text
graphs_faye/
├── src/
│   └── graphs_faye/
│       ├── __init__.py
│       ├── heapq.py
│       └── sp.py
├── data/
│   ├── example1.txt
│   ├── example2.txt
│   ├── example3.txt
│   └── example4.txt
├── test.py
├── README.md
└── pyproject.toml
```

### Files

* `sp.py` contains the Dijkstra shortest path implementation.
* `heapq.py` provides the heap operations used by the algorithm.
* `__init__.py` defines `graphs_faye` as a Python package.
* `test.py` demonstrates how to use the library with graph data files.
* `pyproject.toml` contains the package configuration used by `pip`.

## Testing

The repository includes several example graph files in the `data` directory.

For example:

```bash
python test.py data/example1.txt
```

This command reads the graph from the specified file, runs Dijkstra's algorithm starting at vertex `0`, and prints the shortest distances and paths.

Example output:

```text
Shortest distances from 0:
{0: 0, 1: 4, 2: 12, 3: 19, 4: 21, 5: 11, 6: 9, 7: 8, 8: 14}
```

## Repository

GitHub repository:

https://github.com/fayegor/graphs_faye
