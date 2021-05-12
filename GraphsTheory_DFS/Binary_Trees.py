class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)

            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
            else:
                self.value = value

    def dfs_binary_root(root):
        if root is None:
            return
        else:
            print(root.value, end=" ")
            Node.dfs_binary_root(root.left)
            Node.dfs_binary_root(root.right)

if __name__ == '__main__':
    root = Node(7)
    root.insert(2)
    root.insert(25)
    root.insert(9)
    root.insert(80)
    root.insert(0)
    root.insert(5)
    root.insert(15)
    root.insert(8)

    # Preorder Traversal
    Node.dfs_binary_root(root)

