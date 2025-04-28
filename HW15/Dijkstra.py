import sys
from collections import defaultdict
import heapq
from typing import Optional, Dict, Tuple
from parser import read_graph, Node, reconstruct_path

def dijkstra(nodes: defaultdict, start: Node
            ) -> Tuple[Dict[str,float], Dict[str,Optional[str]]]:

    dist = {name: float('inf') for name in nodes}
    prev = {name: None           for name in nodes}
    dist[start.name] = 0

    visited = set()
    heap = [(0, start.name)]

    while heap:
        d_u, u_name = heapq.heappop(heap)
        if u_name in visited:
            continue
        visited.add(u_name)

        u = nodes[u_name]
        for v_name, w in u.adjacent_nodes.items():
            alt = d_u + w
            if alt < dist[v_name]:
                dist[v_name] = alt
                prev[v_name] = u_name
                heapq.heappush(heap, (alt, v_name))

    return dist, prev



def main():
    fname = sys.argv[1] if len(sys.argv)>1 else 'graph.txt'
    if len(sys.argv)<2:
        print(f"Using default input file: {fname}")

    nodes, start = read_graph(fname)
    dist, prev = dijkstra(nodes, start)

    for name in nodes:
        path = reconstruct_path(prev, name)
        print(f"{start.name} → {name}: dist={dist[name]}, path={' → '.join(path)}")

if __name__ == '__main__':
    main()
