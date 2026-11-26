from collections import deque

metro_graph = {
    "Адмиралтейская": {"Садовая"},
    "Садовая": {"Адмиралтейская", "Сенная площадь", "Спасская", "Звенигородская"},
    "Спасская": {"Садовая", "Сенная площадь", "Достоевская"},
    "Сенная площадь": {"Садовая", "Спасская", "Невский проспект", "Технологический институт"},
    "Технологический институт": {"Сенная площадь", "Пушкинская"},
    "Пушкинская": {"Технологический институт", "Владимирская", "Звенигородская"},
    "Владимирская": {"Пушкинская", "Достоевская", "Площадь Восстания"},
    "Площадь Восстания": {"Владимирская", "Маяковская"},
    "Маяковская": {"Площадь Восстания", "Гостиный двор", "Площадь Александра Невского"},
    "Гостиный двор": {"Маяковская", "Невский проспект"},
    "Невский проспект": {"Гостиный двор", "Сенная площадь"},
    "Достоевская": {"Спасская", "Владимирская", "Лиговский проспект"},
    "Лиговский проспект": {"Достоевская", "Площадь Александра Невского"},
    "Площадь Александра Невского": {"Маяковская", "Лиговский проспект", "Новочеркасская"},
    "Новочеркасская": {"Площадь Александра Невского", "Ладожская"},
    "Ладожская": {"Новочеркасская", "Проспект Большевиков"},
    "Проспект Большевиков": {"Ладожская"},
    "Звенигородская": {"Садовая", "Пушкинская", "Обводный канал"},
    "Обводный канал": {"Звенигородская"},
}


def bfs(graph, start, end):
    if start == end:
        return [start]

    visited = {start}
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                if neighbor == end:
                    return new_path
                queue.append(new_path)
    return None


def dfs(graph, start, end, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path = path + [start]

    if start == end:
        return path

    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, end, visited, path)
            if result:
                return result
    return None


def main():
    print("Доступные станции:")
    for s in sorted(metro_graph):
        print(" •", s)

    start = input("\nВведите начальную станцию: ").strip()
    end = input("Введите конечную станцию: ").strip()

    if start not in metro_graph or end not in metro_graph:
        print("Ошибка: станция не найдена в графе.")
        return

    print("\n--- Поиск в ширину (BFS) ---")
    path_bfs = bfs(metro_graph, start, end)
    if path_bfs:
        print("Путь:", " -> ".join(path_bfs))
    else:
        print("Путь не найден")

    print("\n--- Поиск в глубину (DFS) ---")
    path_dfs = dfs(metro_graph, start, end)
    if path_dfs:
        print("Путь:", " -> ".join(path_dfs))
    else:
        print("Путь не найден")


if __name__ == "__main__":
    main()
