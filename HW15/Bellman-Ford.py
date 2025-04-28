import sys
from collections import defaultdict
import heapq
from typing import Optional, Dict, Tuple
from parser import read_graph, Node, reconstruct_path

def bellman_ford(nodes: defaultdict, start: Node
                 ) -> Tuple[Dict[str, float], Dict[str, Optional[str]]]:

    dist = {name: float('inf') for name in nodes}
    prev = {name: None for name in nodes}
    dist[start.name] = 0

    # Gather all edges
    edges: List[Tuple[str, str, int]] = []
    for u_name, u_node in nodes.items():
        for v_name, w in u_node.adjacent_nodes.items():
            edges.append((u_name, v_name, w))

    # Relax edges repeatedly
    for _ in range(len(nodes) - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u

    # Check for negative-weight cycles
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            raise ValueError("Graph contains a negative-weight cycle")

    return dist, prev

def main():
    fname = sys.argv[1] if len(sys.argv)>1 else 'graph.txt'
    if len(sys.argv)<2:
        print(f"Using default input file: {fname}")

    nodes, start = read_graph(fname)
    dist, prev = bellman_ford(nodes, start)

    for name in nodes:
        path = reconstruct_path(prev, name)
        print(f"{start.name} → {name}: dist={dist[name]}, path={' → '.join(path)}")

if __name__ == '__main__':
    main()
