import enum
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


class Color(enum.Enum):
    RED = "R"
    BLACK = "B"


class Node:
    def __init__(self, key, color=Color.RED, parent=None, left=None, right=None):
        self.key = key
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.key}({self.color.value})"


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(key=None, color=Color.BLACK)
        self.NIL.left = None
        self.NIL.right = None
        self.root = self.NIL
        
    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x is x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        z = Node(key, color=Color.RED, parent=None,
                 left=self.NIL, right=self.NIL)
        y = None
        x = self.root
        while x is not self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            elif z.key > x.key:
                x = x.right
            else:
                return
        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        self._insert_fixup(z)

    def _insert_fixup(self, z):
        while z.parent is not None and z.parent.color == Color.RED:
            if z.parent is z.parent.parent.left:
                uncle = z.parent.parent.right
                if uncle.color == Color.RED:
                    z.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                else:
                    if z is z.parent.right:
                        z = z.parent
                        self._left_rotate(z)
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self._right_rotate(z.parent.parent)
            else:
                uncle = z.parent.parent.left
                if uncle.color == Color.RED:
                    z.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                else:
                    if z is z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self._left_rotate(z.parent.parent)
        self.root.color = Color.BLACK

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _minimum(self, node):
        while node.left is not self.NIL:
            node = node.left
        return node

    def delete(self, key):
        z = self._find(key)
        if z is None:
            return
        y = z
        y_original_color = y.color
        if z.left is self.NIL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right is self.NIL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent is z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == Color.BLACK:
            self._delete_fixup(x)

    def _delete_fixup(self, x):
        while x is not self.root and x.color == Color.BLACK:
            if x is x.parent.left:
                w = x.parent.right
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.right.color == Color.BLACK:
                        w.left.color = Color.BLACK
                        w.color = Color.RED
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.right.color = Color.BLACK
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.left.color == Color.BLACK:
                        w.right.color = Color.BLACK
                        w.color = Color.RED
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.left.color = Color.BLACK
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = Color.BLACK

    def _find(self, key):
        x = self.root
        while x is not self.NIL and x.key is not None:
            if key == x.key:
                return x
            elif key < x.key:
                x = x.left
            else:
                x = x.right
        return None

    def contains(self, key):
        return self._find(key) is not None

    def check_properties(self):
        if self.root is self.NIL:
            return True
        if self.root.color != Color.BLACK:
            return False

        def bh(node):
            if node is self.NIL:
                return 1
            if node.color == Color.RED:
                for c in (node.left, node.right):
                    if c is not self.NIL and c.color == Color.RED:
                        raise ValueError("Красный узел с красным ребёнком")
            lh = bh(node.left)
            rh = bh(node.right)
            if lh != rh:
                raise ValueError("Неравная чёрная высота")
            return lh + (1 if node.color == Color.BLACK else 0)

        try:
            bh(self.root)
            return True
        except ValueError as e:
            print("ОШИБКА:", e)
            return False

def compute_positions(tree):
    """Присваиваем x-координаты (in-order), y = глубина."""
    positions = {}
    order = [0]
    def walk(node, depth=0):
        if node is tree.NIL or node is None:
            return
        walk(node.left, depth + 1)
        positions[id(node)] = (order[0], -depth)
        order[0] += 1
        walk(node.right, depth + 1)
    walk(tree.root)
    return positions


def draw_tree(tree, ax, title=""):
    ax.clear()
    ax.set_title(title, fontsize=11)
    ax.axis("off")

    if tree.root is tree.NIL:
        ax.text(0.5, 0.5, "<пустое дерево>", ha="center", va="center")
        return

    pos = compute_positions(tree)
    xs = [p[0] for p in pos.values()]
    ys = [p[1] for p in pos.values()]
    ax.set_xlim(min(xs) - 1, max(xs) + 1)
    ax.set_ylim(min(ys) - 1, max(ys) + 1.5)

    # Рёбра
    def draw_edges(node):
        if node is tree.NIL or node is None:
            return
        for child in (node.left, node.right):
            if child is not tree.NIL and child is not None:
                x1, y1 = pos[id(node)]
                x2, y2 = pos[id(child)]
                ax.plot([x1, x2], [y1, y2], color="gray", lw=1.2, zorder=1)
                draw_edges(child)
    draw_edges(tree.root)

    for node_id, (x, y) in pos.items():
        node = node_by_id(tree, node_id)
        color = "#d62728" if node.color == Color.RED else "#1a1a1a"
        edge = "#8b0000" if node.color == Color.RED else "black"
        circle = mpatches.Circle((x, y), radius=0.32, facecolor=color,
                                 edgecolor=edge, lw=1.5, zorder=2)
        ax.add_patch(circle)
        ax.text(x, y, str(node.key), ha="center", va="center",
                color="white", fontsize=10, fontweight="bold", zorder=3)

    legend = [
        mpatches.Patch(color="#d62728", label="Красный"),
        mpatches.Patch(color="#1a1a1a", label="Чёрный"),
    ]
    ax.legend(handles=legend, loc="upper right", fontsize=8, framealpha=0.7)


def node_by_id(tree, node_id):
    stack = [tree.root]
    while stack:
        n = stack.pop()
        if n is tree.NIL or n is None:
            continue
        if id(n) == node_id:
            return n
        stack.append(n.left)
        stack.append(n.right)
    return None


def run_with_visualization(inserts, deletes, save_prefix="rbt_step"):
    tree = RedBlackTree()
    total = 1 + len(inserts) + len(deletes)
    cols = 3
    rows = (total + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 3.2 * rows))
    axes = axes.flatten()
    step = 0

    draw_tree(tree, axes[step], "Начальное состояние")
    step += 1

    for k in inserts:
        tree.insert(k)
        assert tree.check_properties()
        draw_tree(tree, axes[step], f"insert({k})")
        step += 1

    for k in deletes:
        tree.delete(k)
        assert tree.check_properties()
        draw_tree(tree, axes[step], f"delete({k})")
        step += 1

    for i in range(step, len(axes)):
        axes[i].axis("off")

    plt.tight_layout()
    plt.savefig(f"{save_prefix}.png", dpi=120, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    inserts = [10, 20, 30, 15, 25, 5, 1, 40, 35, 50, 45]
    deletes = [30, 10, 20, 50]
    run_with_visualization(inserts, deletes, "rbt_visualization")
    print("Сохранено: rbt_visualization.png")
