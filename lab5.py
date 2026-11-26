import heapq
#Спасская, Пушкинская
#Ладожская, Невский проспект
#Технологический институт, Новочеркасская
metro_graph = {
    "Адмиралтейская": {"Садовая": 3},
    "Садовая": {"Адмиралтейская": 3, "Сенная площадь": 3, "Спасская": 3, "Звенигородская": 1},
    "Спасская": {"Садовая": 3, "Сенная площадь": 3, "Достоевская": 1},
    "Сенная площадь": {"Садовая": 3, "Спасская": 3, "Невский проспект": 1, "Технологический институт": 3},
    "Технологический институт": {"Сенная площадь": 3, "Пушкинская": 1},
    "Пушкинская": {"Технологический институт": 1, "Владимирская": 3, "Звенигородская": 3},
    "Владимирская": {"Пушкинская": 3, "Достоевская": 3, "Площадь Восстания": 1},
    "Площадь Восстания": {"Владимирская": 1, "Маяковская": 3},
    "Маяковская": {"Площадь Восстания": 3, "Гостиный двор": 1, "Площадь Александра Невского": 3},
    "Гостиный двор": {"Маяковская": 1, "Невский проспект": 1},
    "Невский проспект": {"Гостиный двор": 1, "Сенная площадь": 1},
    "Достоевская": {"Спасская": 1, "Владимирская": 3, "Лиговский проспект": 5},
    "Лиговский проспект": {"Достоевская": 5, "Площадь Александра Невского": 5},
    "Площадь Александра Невского": {"Маяковская": 3, "Лиговский проспект": 5, "Новочеркасская": 5},
    "Новочеркасская": {"Площадь Александра Невского": 5, "Ладожская": 5},
    "Ладожская": {"Новочеркасская": 5, "Проспект Большевиков": 5},
    "Проспект Большевиков": {"Ладожская": 5},
    "Звенигородская": {"Садовая": 1, "Пушкинская": 3, "Обводный канал": 4},
    "Обводный канал": {"Звенигородская": 4},
}


def dijkstra_path(graph, start, goal):
    if start not in graph or goal not in graph:
        return None, None

    queue = [(0, start)]
    distances = {station: float('inf') for station in graph}
    distances[start] = 0
    previous = {start: None}
    visited = set()

    while queue:
        current_time, current_station = heapq.heappop(queue)

        if current_station in visited:
            continue
        visited.add(current_station)

        if current_station == goal:
            path = []
            node = goal
            while node is not None:
                path.append(node)
                node = previous[node]
            path.reverse()
            return path, current_time

        for neighbor, weight in graph[current_station].items():
            if neighbor in visited:
                continue
            new_time = current_time + weight
            if new_time < distances[neighbor]:
                distances[neighbor] = new_time
                previous[neighbor] = current_station
                heapq.heappush(queue, (new_time, neighbor))

    return None, None


def format_path(path, total_time):
    if not path:
        return "Путь не найден"
    return f"{' -> '.join(path)}  (время в пути: {total_time} мин.)"


def find_station(name, graph):
    name_lower = name.strip().lower()
    for station in graph:
        if station.lower() == name_lower:
            return station
    return None


user_input = input("Введите начальную и конечную станции через запятую: ").strip()
parts = [s.strip() for s in user_input.split(",")]
start_input, end_input = parts
start_station = find_station(start_input, metro_graph)
end_station = find_station(end_input, metro_graph)
print(f"\nИщем кратчайший путь от '{start_station}' до '{end_station}':\n")
path, total_time = dijkstra_path(metro_graph, start_station, end_station)
print(f"Алгоритм Дейкстры: {format_path(path, total_time)}")
