import random
import time
import sys

sys.setrecursionlimit(2000000)

def generate_products(count):
    nazvania = ["Кабель", "Мышь", "Монитор", "Ноутбук", "Принтер", "Наушники", 
                "Клавиатура", "Флешка", "Видеокарта", "Жесткий диск", "Камера", 
                "Фотоаппарат", "Видеокамера", "Смартфон", "Аэрогриль", 
                "Соковыжималка", "Пылесос", "Тостер", "Микроволновка"]

    product_list = []
    ids = random.sample(range(1, 2000000), count)

    for i in range(count):
        product = {
            "id": ids[i],
            "name": random.choice(nazvania)
        }
        product_list.append(product)
    return product_list



def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j]['id'] > arr[j + 1]['id']:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j]['id'] > key_item['id']:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)]['id']
    left = [x for x in arr if x['id'] < pivot]
    middle = [x for x in arr if x['id'] == pivot]
    right = [x for x in arr if x['id'] > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def run_test():
    TOTAL_ITEMS = 1000000
    TEST_SMALL = 5000 

    print(f"--- Генерация {TOTAL_ITEMS} товаров ---")
    full_list = generate_products(TOTAL_ITEMS)
    print("Генерация завершена.\n")


    print(f"--- Тест Quick Sort ({TOTAL_ITEMS} элементов) ---")
    start = time.time()
    sorted_quick = quick_sort(full_list.copy())
    print(f"Время выполнения: {time.time() - start:.4f} сек.\n")


    small_list = full_list[:TEST_SMALL]
    print(f"--- Тест простых сортировок ({TEST_SMALL} элементов) ---")

    start = time.time()
    bubble_sort(small_list.copy())
    print(f"Bubble Sort: {time.time() - start:.4f} сек.")

    start = time.time()
    insertion_sort(small_list.copy())
    print(f"Insertion Sort: {time.time() - start:.4f} сек.")

if __name__ == "__main__":
    run_test()
