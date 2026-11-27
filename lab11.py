import heapq

class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, value)

    def find_min(self):
        return self.heap[0]

    def extract_min(self):
        return heapq.heappop(self.heap)

    def merge(self, other):
        result = BinaryHeap()
        result.heap = self.heap + other.heap
        heapq.heapify(result.heap)  
        return result

    def __len__(self):
        return len(self.heap)

    def __bool__(self):
        return bool(self.heap)

    def __str__(self):
        return str(self.heap)


if __name__ == "__main__":
    print("=== Двоичная куча (heapq) ===")
    bh = BinaryHeap()
    for x in [5, 3, 8, 1, 1, 1, 1, 9, 2, 7]:
        bh.insert(x)
    print("Куча после вставок:", bh)
    print("Минимум:", bh.find_min())
    print("Извлекаем минимум:", bh.extract_min())
    print("Куча после извлечения:", bh)
    bh2 = BinaryHeap()
    for x in [4, 6, 0, 10]:
        bh2.insert(x)
    print("Вторая куча:", bh2)

    merged = bh.merge(bh2)
    print("Результат слияния:", merged)
    print("Минимум объединённой кучи:", merged.find_min())

    extracted = []
    while merged:
        extracted.append(merged.extract_min())
    print("Извлечение по порядку:", extracted)
