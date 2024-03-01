from main4 import add_edges, Node


def dfs_visit(node, graph, pos, visited, colors, layer=1):
    if node is not None and node.id not in visited:
        visited.add(node.id)
        # Визначення кольору для поточного вузла
        color = "#{:06x}".format(0x100000 + (0x0FFFFF // (len(visited) + 1)))
        node.color = color
        colors[node.id] = color

        if node.left:
            dfs_visit(node.left, graph, pos, visited, colors, layer + 1)
        if node.right:
            dfs_visit(node.right, graph, pos, visited, colors, layer + 1)

def bfs_visit(root, graph, pos, colors):
    queue = [root]
    visited = set()
    i = 1

    while queue:
        node = queue.pop(0)
        if node.id not in visited:
            visited.add(node.id)
            # Визначення кольору для поточного вузла
            color = "#{:06x}".format(0x100000 + (0x0FFFFF // i))
            node.color = color
            colors[node.id] = color
            i += 1

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

def visualize_tree_traversal(tree_root, traversal_type="dfs"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    colors = {}

    if traversal_type == "dfs":
        dfs_visit(tree_root, tree, pos, set(), colors)
    elif traversal_type == "bfs":
        bfs_visit(tree_root, tree, pos, colors)

    # Перебудова графа з новими кольорами
    add_edges(tree, tree_root, pos)
    draw_custom_tree(tree, pos, colors)

def draw_custom_tree(tree, pos, colors):
    # Отримання кольорів та міток для відображення
    node_colors = [colors.get(node[0], node[1]['color']) for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

# Використання коду для створення дерева та візуалізації обходів
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Візуалізація DFS
print("DFS Traversal Visualization:")
visualize_tree_traversal(root, "dfs")

# Візуалізація BFS
print("BFS Traversal Visualization:")
visualize_tree_traversal(root, "bfs")
