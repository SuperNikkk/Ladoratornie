from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def from_list(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def is_cousins(root, x, y):
    info = {}

    def dfs(node, depth, parent):
        if node is None:
            return
        if node.val == x or node.val == y:
            info[node.val] = (depth, parent)
        dfs(node.left, depth + 1, node.val)
        dfs(node.right, depth + 1, node.val)

    dfs(root, 0, None)

    if x in info and y in info:
        dx, px = info[x]
        dy, py = info[y]
        return dx == dy and px != py
    return False


if __name__ == "__main__":
    tree1 = from_list([1, 2, 3, 4])
    print("Пример 1:", is_cousins(tree1, 4, 3)) 

    tree2 = from_list([1, 2, 3, None, 4, None, 5])
    print("Пример 2:", is_cousins(tree2, 5, 4))  
