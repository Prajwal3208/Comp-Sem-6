class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def build_tree():
    root_value = int(input("Enter the root value: "))
    root = TreeNode(root_value)

    queue = [root]
    while queue:
        current_node = queue.pop(0)

        num_children = int(input(f"Enter the number of children for node {current_node.value}: "))
        for _ in range(num_children):
            child_value = int(input(f"Enter the value of child {len(current_node.children) + 1} for node {current_node.value}: "))
            child = TreeNode(child_value)
            current_node.add_child(child)
            queue.append(child)

    return root


def dfs_recursive(node):
    print(node.value, end=' ')
    for child in node.children:
        dfs_recursive(child)


def dfs_stack(root):
    stack = [root]
    while stack:
        current_node = stack.pop()
        print(current_node.value, end=' ')
        stack.extend(reversed(current_node.children))


def bfs(root):
    queue = [root]
    while queue:
        current_node = queue.pop(0)
        print(current_node.value, end=' ')
        queue.extend(current_node.children)


# Example usage:
if __name__ == "__main__":
    root_node = build_tree()

    print("\nDFS (Recursive):")
    dfs_recursive(root_node)

    print("\nDFS (Stack):")
    dfs_stack(root_node)

    print("\nBFS:")
    bfs(root_node)

