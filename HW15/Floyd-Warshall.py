import sys
from collections import defaultdict
import heapq
from typing import Optional, Dict, Tuple, List
from parser import read_graph, Node

def floyd_warshall(nodes: defaultdict
                   ) -> Tuple[Dict[str, Dict[str, float]], Dict[str, Dict[str, Optional[str]]]]:

    names = list(nodes.keys())

    dist: Dict[str, Dict[str, float]] = {
        u: {v: float('inf') for v in names} for u in names
    }
    next_hop: Dict[str, Dict[str, Optional[str]]] = {
        u: {v: None for v in names} for u in names
    }

    for u in names:
        dist[u][u] = 0
        next_hop[u][u] = u
    for u_name, u_node in nodes.items():
        for v_name, w in u_node.adjacent_nodes.items():
            dist[u_name][v_name] = w
            next_hop[u_name][v_name] = v_name

    # Main triple loop
    for k in names:
        for i in names:
            for j in names:
                alt = dist[i][k] + dist[k][j]
                if alt < dist[i][j]:
                    dist[i][j] = alt
                    next_hop[i][j] = next_hop[i][k]

    return dist, next_hop

def reconstruct_fw_path(next_hop: Dict[str, Dict[str, Optional[str]]],
                        u: str, v: str) -> List[str]:
    if next_hop[u][v] is None:
        return []
    path: List[str] = [u]
    while u != v:
        u = next_hop[u][v]
        path.append(u)
    return path

def main():
    fname = sys.argv[1] if len(sys.argv)>1 else 'graph.txt'
    if len(sys.argv)<2:
        print(f"Using default input file: {fname}")

    nodes, start = read_graph(fname)
    dist, next = floyd_warshall(nodes)

    for u in nodes:
            for v in nodes:
                if dist[u][v] < float('inf'):
                    path = reconstruct_fw_path(next, u, v)
                    print(f"{u} -> {v}: dist={dist[u][v]}, path={'->'.join(path)}")

if __name__ == '__main__':
    main()
