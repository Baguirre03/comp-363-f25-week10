def khan(graph: list[list[int]]) -> list[int]:
    """Comprehensive implementation of Kahn's algorithm for topological sorting."""

    # Data integrity check - a bit much but I was having fun with it.
    if (
        graph is None
        or not isinstance(graph, list)
        or len(graph) == 0
        or not all(isinstance(row, list) for row in graph)
        or not all(len(row) == len(graph) for row in graph)
    ):
        raise ValueError("Input must be a non-empty square adjacency matrix.")

    # Ease of reference
    N = len(graph)
    NO_EDGE = graph[0][0]

    # Calculate in-degrees of all vertices.
    in_degrees = [0] * N
    for u in range(N):
        for v in range(N):
            if graph[u][v] != NO_EDGE:
                # In edge u --> v we compute the in-degree of v
                in_degrees[v] += 1

    # Initialize list of source vertices
    sources = []
    for i in range(N):
        if in_degrees[i] == 0:
            sources.append(i)

    # List to store the topological order
    topological_order = []

    # Progressively remove sources and update in-degrees
    while len(sources) > 0:
        # Remove a source vertex
        vertex = sources.pop(0)
        # Add it to the topological order
        topological_order.append(vertex)
        # Decrease in-degrees of its neighbors
        for neighbor in range(N):
            if graph[vertex][neighbor] != NO_EDGE:
                in_degrees[neighbor] -= 1
                # If in-degree becomes zero, add it to sources
                if in_degrees[neighbor] == 0:
                    sources.append(neighbor)

    # Done
    return topological_order


def DFS(G, v, marked, res):
    # Mark the current vertex as visited
    marked.add(v)
    # Consider all the neighbors of v
    for w in range(len(G)):
        # For any edge v --> w, if w is unmarked,
        # plan to visit it.
        if G[v][w] != G[0][0] and w not in marked:
            # Plan to visit w
            DFS(G, w, marked, res)

    res.append(v)  # add it after visiting all descendants
    return res


def DFS_helper(G):
    """Helper method to launch a DFS from vertex v."""
    marked = set()
    res = []

    for u in range(len(G)):
        if u not in marked:
            DFS(G, u, marked, res)

    res.reverse()
    return res


G1 = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
]

G2 = [
    [0, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 1, 2, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
]

print(khan(G1))  # [3, 0, 1, 2, 4, 5]
print(khan(G2))  # [0, 3, 1, 2, 4, 5]
print(DFS_helper(G1))  # [3, 0, 1, 2, 4, 5]
print(DFS_helper(G2))  # [3, 1, 0, 2, 4, 5]
