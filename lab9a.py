def activity_selection(activities):
    sorted_acts = sorted(activities, key=lambda x: x[1])
    
    selected = [sorted_acts[0]]
    last_end = sorted_acts[0][1]
    
    for start, end in sorted_acts[1:]:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    
    return selected

activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9),
              (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]

result = activity_selection(activities)
print(result)
print("Количество:", len(result))
