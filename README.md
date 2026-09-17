# graphs_faye

A Python library for working with weighted graphs and shortest-path problems.

## Overview

`graphs_faye` is a Python library that provides graph algorithms for finding paths through graphs. The library currently includes two algorithms:

* **Dijkstra's shortest path algorithm** for finding minimum-cost paths in weighted graphs with nonnegative edge weights.
* **Breadth-First Search (BFS)** for finding shortest paths in terms of the number of edges in an unweighted graph.

The project is organized as a standard Python package and can be installed with `pip`.

The main package is named `graphs_faye`.

## Features

### Dijkstra's Shortest Path Algorithm

Dijkstra's algorithm finds the shortest paths from a specified source vertex to other vertices in a weighted graph.

The implementation:

* maintains the shortest known distance to each vertex;
* uses a min-heap to efficiently select the next vertex to process;
* updates distances when a shorter path is discovered;
* records the path used to reach each vertex.

The algorithm returns both the shortest distances and the corresponding paths.

### Breadth-First Search

The library also includes a Breadth-First Search implementation.

BFS explores a graph level by level. For an unweighted graph, this means that the first time a vertex is reached, the number of edges used to reach it is minimal.

The BFS implementation returns both the number of edges from the source to each reachable vertex and the corresponding paths.

## Requirements

The package requires:

* Python 3.8 or newer
* `pip`

The package itself does not require any third-party Python dependencies.

## Installation

Clone the repository:

```bash
git clone https://github.com/fayegor/graphs_faye.git
```

Change into the project directory:

```bash
cd graphs_faye
```

Install the package:

```bash
python -m pip install .
```

After installation, the package can be imported with:

```python
from graphs_faye import sp
from graphs_faye import bfs
```

## Package Structure

```text
graphs_faye/
├── src/
│   └── graphs_faye/
│       ├── __init__.py
│       ├── heapq.py
│       ├── sp.py
│       └── bfs.py
├── data/
│   ├── example1.txt
│   ├── example2.txt
│   ├── example3.txt
│   └── example4.txt
├── pics/
├── test.py
├── README.md
└── pyproject.toml
```

### Source Files

#### `src/graphs_faye/__init__.py`

Defines `graphs_faye` as a Python package.

#### `src/graphs_faye/sp.py`

Contains the implementation of Dijkstra's shortest path algorithm.

#### `src/graphs_faye/heapq.py`

Provides the heap operations used by the Dijkstra implementation, including operations such as `heappush()` and `heappop()`.

#### `src/graphs_faye/bfs.py`

Contains the Breadth-First Search implementation.

#### `test.py`

Provides a command-line example that reads a graph from a text file and runs Dijkstra's algorithm from source vertex `0`.

#### `data/`

Contains example graph files that can be used for testing.

#### `pyproject.toml`

Contains the Python package configuration used to build and install `graphs_faye`.

## Graph Representation

Graphs in this library are represented using Python dictionaries.

Each vertex is a key in the outer dictionary. Its value is another dictionary containing neighboring vertices and the weights of their edges.

For example:

```python
graph = {
    0: {1: 4, 7: 8},
    1: {0: 4, 2: 8, 7: 11},
    2: {1: 8, 3: 7}
}
```

In this example:

* vertex `0` has an edge to vertex `1` with weight `4`;
* vertex `0` has an edge to vertex `7` with weight `8`;
* vertex `1` has edges to vertices `0`, `2`, and `7`;
* vertex `2` has edges to vertices `1` and `3`.

A graph file uses three values per line:

```text
source destination weight
```

For example:

```text
0 1 4
0 7 8
1 2 8
```

The `test.py` program reads these values and converts them into the dictionary representation used by the library.

## Using Dijkstra's Algorithm

Dijkstra's algorithm is available through the `sp` module.

Import it with:

```python
from graphs_faye import sp
```

Call the algorithm with:

```python
dist, path = sp.dijkstra(graph, source)
```

The two arguments are:

* `graph`: the graph represented as a dictionary;
* `source`: the vertex where the search begins.

The function returns:

* `dist`: a dictionary containing the shortest known distance from the source to each vertex;
* `path`: a dictionary containing the vertices used to reach each destination.

### Dijkstra Example

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

print("Shortest distances from 0:")
print(dist)

for vertex in path:
    print(f"shortest path to {vertex}: {path[vertex]}")
```

The resulting distance dictionary for this example is:

```text
{0: 0, 1: 4, 2: 12, 3: 19, 4: 21, 5: 11, 6: 9, 7: 8, 8: 14}
```

For example:

* the shortest distance from `0` to `1` is `4`;
* the shortest distance from `0` to `7` is `8`;
* the shortest distance from `0` to `2` is `12`;
* the shortest distance from `0` to `4` is `21`.

### How Dijkstra's Algorithm Works

The algorithm begins at the source vertex with distance `0`. Every other vertex is initially assigned a very large distance.

The algorithm then uses a min-heap to select the vertex with the smallest currently known distance.

For each selected vertex, the algorithm examines its neighboring vertices. If traveling through the selected vertex produces a shorter distance, the distance is updated and the new value is added to the heap.

This process continues until there are no more vertices that need to be processed.

Dijkstra's algorithm relies on nonnegative edge weights. For graphs containing negative edge weights, a different shortest-path algorithm should be used.

## Using Breadth-First Search

Breadth-First Search is available through the `bfs` module.

Import it with:

```python
from graphs_faye import bfs
```

Call the algorithm with:

```python
dist, path = bfs.bfs(graph, source)
```

The arguments are:

* `graph`: the graph represented as a dictionary;
* `source`: the starting vertex.

The function returns:

* `dist`: the number of edges from the source to each reachable vertex;
* `path`: the vertices used to reach each destination.

BFS is intended for unweighted graphs, where each edge represents the same traversal cost.

### BFS Example

```python
from graphs_faye import bfs

graph = {
    0: {1: 1, 2: 1},
    1: {0: 1, 3: 1},
    2: {0: 1, 3: 1},
    3: {1: 1, 2: 1}
}

dist, path = bfs.bfs(graph, 0)

print("BFS distances:")
print(dist)

print("BFS paths:")
print(path)
```

The result is:

```text
{0: 0, 1: 1, 2: 1, 3: 2}
```

This means:

* vertex `0` is `0` edges from the source;
* vertices `1` and `2` are `1` edge from the source;
* vertex `3` is `2` edges from the source.

The corresponding paths include:

```text
0 -> 1
0 -> 2
0 -> 1 -> 3
```

## Command-Line Testing

The repository includes several example graph files in the `data` directory:

```text
data/
├── example1.txt
├── example2.txt
├── example3.txt
└── example4.txt
```

The provided `test.py` program can be used to run Dijkstra's algorithm on one of these files.

For example:

```bash
python test.py data/example1.txt
```

The program reads the graph file, starts Dijkstra's algorithm at vertex `0`, and prints the shortest distances and paths.

For `example1.txt`, the shortest-distance result is:

```text
Shortest distances from 0:
{0: 0, 1: 4, 2: 12, 3: 19, 4: 21, 5: 11, 6: 9, 7: 8, 8: 14}
```

### Testing BFS

BFS can also be tested directly after installing the package:

```bash
python -c "from graphs_faye import bfs; graph={0:{1:1,2:1},1:{0:1,3:1},2:{0:1,3:1},3:{1:1,2:1}}; print(bfs.bfs(graph,0))"
```

The test produces:

```text
({0: 0, 1: 1, 2: 1, 3: 2}, {0: [], 1: [0], 2: [0], 3: [0, 1]})
```

## API Summary

### `sp.dijkstra(graph, source)`

Finds shortest paths in a weighted graph.

**Parameters**

* `graph`: dictionary representing the graph
* `source`: starting vertex

**Returns**

* `dist`: shortest distances
* `path`: shortest paths

### `bfs.bfs(graph, source)`

Finds shortest paths by number of edges in an unweighted graph.

**Parameters**

* `graph`: dictionary representing the graph
* `source`: starting vertex

**Returns**

* `dist`: number of edges from the source
* `path`: shortest paths by number of edges

## Development

The repository uses separate Git branches for development and the main version.

* `main` contains the main version of the project.
* `dev` is used for development work and new changes.

The `main` branch is protected.

Changes can be developed on `dev`, tested locally, and then merged into `main`.
## Project Information

Package name:

```text
graphs_faye
```

Current package version:

```text
0.1.0
```

## GitHub Repository

Public repository:

https://github.com/fayegor/graphs_faye


