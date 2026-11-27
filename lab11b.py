class LeftistNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.dist = 1


def _dist(node):
    return node.dist if node is not None else 0


def _merge_nodes(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if a.key > b.key:
        a, b = b, a
    a.right = _merge_nodes(a.right, b)
    if _dist(a.left) < _dist(a.right):
        a.left, a.right = a.right, a.left
    a.dist = _dist(a.right) + 1
    return a


class LeftistHeap:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = _merge_nodes(self.root, LeftistNode(value))

    def find_min(self):
        return self.root.key

    def extract_min(self):
        min_key = self.root.key
        self.root = _merge_nodes(self.root.left, self.root.right)
        return min_key

    def merge(self, other):
        result = LeftistHeap()
        result.root = _merge_nodes(self.root, other.root)
        return result

    def __bool__(self):
        return self.root is not None


if __name__ == "__main__":
    print("=== Левосторонняя куча ===")
    lh = LeftistHeap()
    for x in [5, 3, 8, 1, 9, 2, 7]:
        lh.insert(x)
    print("Минимум:", lh.find_min())
    print("Извлекаем минимум:", lh.extract_min())
    print("Новый минимум:", lh.find_min())

    lh2 = LeftistHeap()
    for x in [4, 6, 0, 10]:
        lh2.insert(x)

    print("\n--- Вторая куча ---")
    print("Минимум второй кучи:", lh2.find_min())
    print("Извлекаем минимум из второй кучи:", lh2.extract_min())
    print("Новый минимум второй кучи:", lh2.find_min())

    merged = lh.merge(lh2)
    print("\n--- После слияния ---")
    print("Минимум после слияния:", merged.find_min())

    extracted = []
    while merged:
        extracted.append(merged.extract_min())
    print("Извлечение по порядку:", extracted)
