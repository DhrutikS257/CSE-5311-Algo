from dfs import Graph, read_edges

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    def __str__(self):
        return self.val + (" -> " + str(self.next) if self.next else "")


def topological_sort(nodes, edges):
    g = Graph(edges, nodes)
    _, f, _ = g.dfs()
    return sorted(nodes, key=lambda u: f[u], reverse=True)


def parse_file(filename):
    return read_edges(filename)


def build_linked_list(order):
    head = None
    prev = None
    for label in order:
        node = ListNode(label)
        if prev:
            prev.next = node
        else:
            head = node
        prev = node
    return head

# Node order now fixed to the diagram's visit sequence:
CLOTHING_NODES = [
    'shirt',
    'watch',
    'undershorts',
    'pants',
    'shoes',
    'socks',
    'belt',
    'tie',
    'jacket'
]


def main():
    import sys
    if len(sys.argv) < 2:
        filename = 'topological.txt'
        print(f"No input file specified. Using default: {filename}")
    else:
        filename = sys.argv[1]

    print(f"Reading edges from '{filename}'...\n")
    edges = parse_file(filename)

    # Print DFS metadata
    graph = Graph(edges, CLOTHING_NODES)
    d, f, _ = graph.dfs()
    print("Node        | Discovery | Finish | Adjacent")
    print("---------------------------------------------------")
    for u in CLOTHING_NODES:
        adj = ','.join(graph.adj.get(u, [])) or 'None'
        print(f"{u:<11} | {d[u]:>9} | {f[u]:>6} | {adj}")

    # Linked list
    order = topological_sort(CLOTHING_NODES, edges)
    ll_head = build_linked_list(order)
    print("\nTopological sort represented as a linked list:")
    print(ll_head)

if __name__ == '__main__':
    main()
