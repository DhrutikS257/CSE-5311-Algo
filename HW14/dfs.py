# dfs.py
import collections

class Graph:
    def __init__(self, edges, nodes=None):
        self.adj = collections.defaultdict(list)
        self.nodes = set(nodes) if nodes else set()
        for u, v in edges:
            self.adj[u].append(v)
            self.nodes.add(u)
            self.nodes.add(v)
        if nodes:
            for n in nodes:
                self.nodes.add(n)
                self.adj.setdefault(n, [])
        self.nodes = list(self.nodes)
        self.color = {}
        self.parent = {}
        self.d = {}
        self.f = {}
        self.time = 0

    def dfs(self):
        """Perform DFS and return discovery/finish times and parents."""
        self.color = {u: 'WHITE' for u in self.nodes}
        self.parent = {u: None for u in self.nodes}
        self.d = {}
        self.f = {}
        self.time = 0
        for u in self.nodes:
            if self.color[u] == 'WHITE':
                self._dfs_visit(u)
        return self.d, self.f, self.parent

    def _dfs_visit(self, u):
        self.time += 1
        self.d[u] = self.time
        self.color[u] = 'GRAY'
        for v in self.adj[u]:
            if self.color[v] == 'WHITE':
                self.parent[v] = u
                self._dfs_visit(v)
        self.color[u] = 'BLACK'
        self.time += 1
        self.f[u] = self.time


def read_edges(filename):
    """Read edge list from a text file."""
    edges = []
    with open(filename) as f:
        for line in f:
            parts = line.split()
            if len(parts) == 2:
                edges.append((parts[0], parts[1]))
    return edges


def main():
    import sys
    # Use 'data.txt' by default if no file specified
    if len(sys.argv) < 2:
        edge_file = 'dfs.txt'
        print("No input file specified. Using default: dfs.txt")
    else:
        edge_file = sys.argv[1]

    print(f"Starting DFS on graph from '{edge_file}'...\n")

    edges = read_edges(edge_file)
    g = Graph(edges)
    d, f, parent = g.dfs()

    print("Node metadata after DFS:")
    print("Value | Discovery | Finish | Parent | Adjacent")
    print("------------------------------------------------------")
    for u in sorted(g.nodes):
        adj = ','.join(g.adj[u])
        par = parent[u] if parent[u] is not None else 'None'
        print(f"{u:<5} | {d[u]:>9} | {f[u]:>6} | {par:<6} | {adj}")

if __name__ == '__main__':
    main()
