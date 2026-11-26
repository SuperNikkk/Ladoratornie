def place_towers(cities, radius):
    cities = sorted(cities)
    towers = []
    i = 0
    n = len(cities)

    while i < n:
        tower_pos = cities[i] + radius
        towers.append(tower_pos)
        while i < n and cities[i] <= tower_pos + radius:
            i += 1

    return towers


cities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
radius = 2

towers = place_towers(cities, radius)
print("Минимальное количество вышек:", len(towers))
print("Позиции вышек:", towers)
