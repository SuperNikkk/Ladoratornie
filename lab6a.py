from collections import deque


class TreeNode:
    __slots__ = ('val', 'left', 'right')

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def is_symmetric(self):
        def is_mirror(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return (left.val == right.val
                    and is_mirror(left.left, right.right)
                    and is_mirror(left.right, right.left))
        if self.root is None:
            return True
        return is_mirror(self.root.left, self.root.right)


def build_tree(nodes):
    if not nodes or nodes[0] is None:
        return BinaryTree(None)
    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1
    while queue and i < len(nodes):
        node = queue.popleft()
        if i < len(nodes):
            if nodes[i] is not None:
                node.left = TreeNode(nodes[i])
                queue.append(node.left)
            i += 1
        if i < len(nodes):
            if nodes[i] is not None:
                node.right = TreeNode(nodes[i])
                queue.append(node.right)
            i += 1
    return BinaryTree(root)


if __name__ == "__main__":
    root1 = build_tree([1, 2, 2, 3, 4, 4, 3])
    print(f"Пример 1: {root1.is_symmetric()}")

    root2 = build_tree([1, 2, 2, None, 3, None, 3])
    print(f"Пример 2: {root2.is_symmetric()}")
