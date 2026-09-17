from collections import deque


def bfs(graph, source):
    """Find shortest paths from source in an unweighted graph.

    Args:
        graph: A dictionary whose keys are vertices and whose values
            contain neighboring vertices.
        source: The starting vertex.

    Returns:
        A tuple containing:
        - dist: shortest number of edges from source to each reachable vertex
        - path: the vertices used to reach each vertex from source
    """
    dist = {source: 0}
    path = {source: []}
    queue = deque([source])

    while queue:
        u = queue.popleft()

        for v in graph.get(u, {}):
            if v not in dist:
                dist[v] = dist[u] + 1
                path[v] = path[u] + [u]
                queue.append(v)

    return dist, path