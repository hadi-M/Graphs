class GraphNode():
    def __init__(self, identifier):
        self.id = identifier
        self.parents = []
        self.children = []

    def add_parent(self, parent_node: "GraphNode") -> None:
        self.parents.append(parent_node)

    def add_child(self, child_node: "GraphNode") -> None:
        self.children.append(child_node)


class Graph():
    def __init__(self):
        self.members = dict()
    
    def add_member(self, member_id: int) -> None:
        new_node = GraphNode(member_id)
        self.members[member_id] = new_node

    def get_longest_ancestor(self, starting_node_id: int) -> int:
        visited = []
        memory = Queue()
        paths = []
        memory.enqueue([starting_vertex])
        while memory.size() > 0:
            next_path = memory.dequeue()
            paths.append(paths)
            next_elem = next_path[-1]
            if next_elem not in visited:
                visited.append(next_elem)
                # print(next_elem)
                for i in self.vertices[next_elem]:
                    memory.enqueue(next_path + [i])


def earliest_ancestor(ancestors, starting_node):
    G1 = Graph()
    for relationship in ancestors:  # ancestors: [(1, 3), (2, 3), (3, 6),
        try:
            node_id_1 = relationship[0]
            G1.members[node_id_1].chil
