from random import choice, sample
import random
import time
import math



product_list = []
nazvania=["Кабель", "Мышь", "Монитор", "Ноутбук", "Принтер", "Наушники", "Клавиатура", "Флешка", "Видеокарта", "Жесткий диск", "Камера", "Фотоаппарат", "Видеокамера", "Смартфон", "Аэрогриль", "Соковыжималка", "Пылесос", "Тостер", "Микроволновка"]
numers_product = sample(range(1, 1500000), 1000000)
numers_product.sort()
for i in range(0, len(numers_product)):
    if numers_product[i]>len(nazvania):
        q=numers_product[i]//19
        name1 =nazvania[i% len(nazvania)]
        product = dict(id = numers_product[i], name = name1)
        product_list.append(product)
    else:
        name1=nazvania[i]
        product = dict(id = numers_product[i], name = name1)
        product_list.append(product)
        

poisk_id = [
    numers_product[3], 
    numers_product[len(numers_product) // 2], 
    numers_product[-5], 
    random.choice(numers_product), 
    10000015
]




time_list=[]
for i in poisk_id:
    start=time.perf_counter()
    for j in product_list:
        if j['id']==i:
            break
    en=time.perf_counter()
    time_list.append((en-start))




exp_time_list=[]
for i in poisk_id:
    start=time.perf_counter()
    n=len(product_list)
    if i>product_list[0]['id']:
        bound=1
        while bound < n and product_list[bound]['id'] < i:
            bound*=2
        left=bound // 2
        right=min(bound, n - 1)
        while left<=right:
            mid=(left + right) // 2
            if product_list[mid]['id'] == i:
                break
            elif product_list[mid]['id'] < i:
                left = mid + 1
            else:
                right = mid - 1

    en = time.perf_counter()
    exp_time_list.append((en - start))



binary_times=[]
for i in poisk_id:
    start = time.perf_counter()
    found_bin = -1
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if product_list[mid]['id'] == i:
            found_bin = mid
            break
        elif product_list[mid]['id'] < i:
            left = mid + 1
        else:
            right = mid - 1
    en = time.perf_counter()
    binary_times.append(en - start)




jump_times=[]
for i in poisk_id:
    start = time.perf_counter()
    found_jump = -1
    prev = 0
    curr = 0
    prev = 0
    step = int(math.sqrt(n))
    while curr < n and product_list[min(curr + step, n) - 1]['id'] < i:
        prev = curr
        curr += step
        if prev >= n: break
    for i in range(prev, min(curr + step, n)):
        if product_list[i]['id'] ==i:
            break
    jump_times.append(time.perf_counter() - start)





print("-" * 162)
print("--", end=" ")
print("Тип поиска     \   ID".ljust(21), end=' -- ')
for j in range(5):
    print(f"{poisk_id[j]:<23}", end=' -- ')
print()
print("-" * 162)
print("--", end=" ")
print("Линейный поиск".ljust(21), end=' -- ')
for j in range(5):
    print(f"{time_list[j]:<23}", end=' -- ')
print()
print("-" * 162)
print("--", end=" ")
print("Экспонециальный поиск".ljust(21), end=' -- ')
for j in range(5):
    print(f"{exp_time_list[j]:<23}", end=' -- ')
print()
print("-" * 162)
print("--", end=" ")
print("Бинарный поиск".ljust(21), end=' -- ')
for j in range(5):
    print(f"{binary_times[j]:<23}", end=' -- ')
print()
print("-" * 162)
print("--", end=" ")
print("Прыжковый поиск".ljust(21), end=' -- ')
for j in range(5):
    print(f"{jump_times[j]:<23}", end=' -- ')
print()
print("-" * 162)


