import sys
from collections import defaultdict
from typing import Optional, Dict, Tuple

class Node:
    def __init__(self, name: str = ""):
        self.name: str = name
        self.adjacent_nodes: Dict[str,int] = defaultdict(int)

    def add_edge(self, neighbor: 'Node', weight: int):
        self.adjacent_nodes[neighbor.name] = weight

    def __repr__(self):
        return f"Node({self.name!r})"

def read_graph(path: str) -> Tuple[defaultdict, Node]:
    nodes: defaultdict[str,Node] = defaultdict(Node)
    start_node: Optional[Node] = None

    with open(path) as f:
        for line in f:
            parts = line.strip().split()
            if not parts:
                continue

            if parts[0] == 'init':
                name = parts[1]
                node = nodes[name]
                node.name = name
                start_node = node
            else:
                u_name, v_name, w_str = parts
                w = int(w_str)

                u = nodes[u_name];  v = nodes[v_name]
                if u.name == "": u.name = u_name
                if v.name == "": v.name = v_name

                u.add_edge(v, w)

    if start_node is None:
        raise ValueError("Missing ‘init <node>’ line")
    return nodes, start_node

def reconstruct_path(prev: Dict[str,Optional[str]],
                     target: str) -> list[str]:
    path = []
    while target is not None:
        path.append(target)
        target = prev[target]
    return path[::-1]
