class Graph:
    def __init__(self):
        self.g = {}
        self.g_reverse = {}

    def node(self, u: str) -> None:
        self.g[u] = self.g.get(u, [])
        self.g_reverse[u] = self.g_reverse.get(u, [])

    def edge(self, u: str, v: str, weight: float = 0) -> None:
        self.node(u)
        self.node(v)
        self.g[u] = self.g.get(u, []) + [(v, weight)]
        self.g_reverse[v] = self.g_reverse.get(v, []) + [(u, weight)]

    @property
    def nodes(self) -> [str]:
        return self.g.keys()

    @property
    def edges(self) -> [[(str, float)]]:
        edges = []
        for node in self.g:
            edges.append(self.g[node])
        return edges

    def get_node_edges(self, node: str) -> [(str, float)]:
        return self.g.get(node, [])

    def get_node_reverse_edges(self, node: str) -> [(str, float)]:
        return self.g_reverse.get(node, [])

    def get_raw_data(self) -> {str: [(str, float)]}:
        return self.g

    def __iter__(self):
        return self.g.__iter__()

    def __repr__(self):
        return self.g.__repr__()

    def __len__(self):
        return len(self.g)
