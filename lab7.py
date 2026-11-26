import matplotlib.pyplot as plt
import matplotlib.patches as patches


class AVLNode:
    def __init__(self, key, left=None, right=None, height=1):
        self.key = key
        self.left = left
        self.right = right
        self.height = height


def height(node):
    return node.height if node else 0


def update_height(node):
    node.height = 1 + max(height(node.left), height(node.right))


def balance_factor(node):
    return height(node.left) - height(node.right) if node else 0


def rotate_right(y):
    x = y.left
    t2 = x.right
    x.right = y
    y.left = t2
    update_height(y)
    update_height(x)
    return x


def rotate_left(x):
    y = x.right
    t2 = y.left
    y.left = x
    x.right = t2
    update_height(x)
    update_height(y)
    return y


def rebalance(node, key):
    update_height(node)
    bf = balance_factor(node)

    if bf > 1:
        if key < node.left.key:
            return rotate_right(node)               
        else:
            node.left = rotate_left(node.left)
            return rotate_right(node)                 

    if bf < -1:
        if key > node.right.key:
            return rotate_left(node)                
        else:
            node.right = rotate_right(node.right)
            return rotate_left(node)               

    return node


def insert(node, key):
    if node is None:
        return AVLNode(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        return node
    return rebalance(node, key)


def min_value_node(node):
    while node.left:
        node = node.left
    return node


def delete(node, key):
    if node is None:
        return None
    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    else:
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        temp = min_value_node(node.right)
        node.key = temp.key
        node.right = delete(node.right, temp.key)

    if node is None:
        return None
    return rebalance(node, node.key)


def visualize(root, title="AVL Tree", save_path=None):
    if root is None:
        print("Дерево пустое")
        return

    positions = {}
    counter = [0]

    def assign(node, depth=0):
        if node is None:
            return
        assign(node.left, depth + 1)
        positions[id(node)] = (counter[0], -depth)
        counter[0] += 1
        assign(node.right, depth + 1)

    assign(root)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title(title, fontsize=14)
    ax.axis("off")

    def draw_edges(node):
        if node is None:
            return
        x1, y1 = positions[id(node)]
        for child in (node.left, node.right):
            if child:
                x2, y2 = positions[id(child)]
                ax.plot([x1, x2], [y1, y2], color="gray", linewidth=1.5, zorder=1)
                draw_edges(child)

    draw_edges(root)

    def draw_nodes(node):
        if node is None:
            return
        x, y = positions[id(node)]
        bf = balance_factor(node)
        color = "lightgreen" if bf == 0 else "lightyellow"
        ax.add_patch(patches.Circle((x, y), radius=0.35,
                                    facecolor=color, edgecolor="black", zorder=2))
        ax.text(x, y, f"{node.key}\nh={node.height}",
                ha="center", va="center", fontsize=9, zorder=3)
        draw_nodes(node.left)
        draw_nodes(node.right)

    draw_nodes(root)

    xs = [p[0] for p in positions.values()]
    ys = [p[1] for p in positions.values()]
    ax.set_xlim(min(xs) - 1, max(xs) + 1)
    ax.set_ylim(min(ys) - 1, max(ys) + 1)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=120, bbox_inches="tight")
        print(f"Сохранено: {save_path}")
    plt.show()


if __name__ == "__main__":
    root = None

    print("Вставка: 30, 20, 10")
    for k in (30, 20, 10):
        root = insert(root, k)
    visualize(root, "Шаг 1: вставка 30, 20, 10 (LL-поворот)", "step1.png")

    print("Вставка: 40, 1, 2, 100, 50, 25")
    for k in (40, 1, 2, 100, 50, 25):
        root = insert(root, k)
    visualize(root, "Шаг 2: вставка 40, 50, 25 (RR-поворот)", "step2.png")

    print("Удаление: 40")
    root = delete(root, 40)
    visualize(root, "Шаг 3: удаление 40", "step3.png")
