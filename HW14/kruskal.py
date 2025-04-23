#!/usr/bin/env python3
import sys

class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, x):
        self.parent[x] = x
        self.rank[x] = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        # union by rank
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

def read_edges(filename):
    edges = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            u, v, w = line.split()
            edges.append((u, v, int(w)))
    return edges

def kruskal(vertices, edges):
    # 1) make-set for each vertex
    ds = DisjointSet()
    for v in vertices:
        ds.make_set(v)

    # 2) sort edges by weight
    edges = sorted(edges, key=lambda e: e[2])

    mst = []
    total_weight = 0
    # 3) for each edge in non-decreasing order
    for u, v, w in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, w))
            total_weight += w
    return mst, total_weight

def main():
    # handle command-line argument
    if len(sys.argv) < 2:
        filename = 'kruskal.txt'
        print(f"No input file specified. Using default: {filename}")
    else:
        filename = sys.argv[1]
    print(f"Reading edges from '{filename}'...\n")

    edges = read_edges(filename)
    # collect all unique vertices
    verts = set()
    for u, v, _ in edges:
        verts.add(u)
        verts.add(v)

    mst, total = kruskal(verts, edges)

    # print table header
    print("Selected MST edges:")
    print(f"{'Edge':<12}| {'Weight':>6}")
    print('-' * 20)
    for u, v, w in mst:
        print(f"{u+'-'+v:<12}| {w:>6}")
    print()
    print(f"Total weight: {total}")

if __name__ == '__main__':
    main()
