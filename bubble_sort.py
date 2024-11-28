

"""

Бульбашковий алгоритм сортування

Time Complexity: O(n^2)
Auxiliary Space: O(1)
"""

import time
import random
import cProfile
from rand_example import show_result_image, random_uniform, np_sort, save_txt_file, data_str, random_uniform_int

# Функція бульбашкового сортування
def bubble_sort(arr):
    n = len(arr)
 
    # Пройти по всіх елементах масиву
    for i in range(n):
 
        # Останній та  i-й елементи вже на місці
        for j in range(0, n-i-1):

            # Обхід масиву від 0 до n-i-1
            # Поміняти місцями, якщо знайдений елемент більший ніж наступний елемент
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
 
 
# Запуск на виконання
if __name__ == "__main__":

    # ---------------------- вихідні параметри об'єкта сортування ----------------------------
    a = 0
    b = 10
    iter = 10000
    failename_start = 'start_value.txt'
    failename_stop = 'stop_value.txt'

    # ---------------------- сортування випадкового масиву float ---------------------------
    random = random_uniform(a, b, iter)

    # ---------------------- сортування випадкового масиву int ---------------------------
    # random = random_uniform_int(a, b, iter)

    save_txt_file(random, failename_start)                              # запис випадкового масиву у файл
    show_result_image(random, 'random.uniform')                         # графік візуалізації вхідних не сортованих даних
    random_sort = np_sort(random)                                       # сортування методами numpy
    show_result_image(random_sort, 'random.uniform.sort')               # графік візуалізації сортованих даних
    save_txt_file(random_sort, failename_stop)                          # запис сортованого масиву методами numpy у файл



    # ---------------------- Аналітика складності алгоритму  ---------------------------
    # Фіксація часу --------------------------
    #
    # StartTime = time.time()
    # bubble_sort_arr = bubble_sort(random)                              # сортування бульбашкою
    # totalTime = (time.time() - StartTime)
    # print('totalTime =', totalTime, 's')

    # Використання сервісів -------------------
    cp = cProfile.Profile()                                             # аналітика складності
    cp.enable()

    bubble_sort_arr = bubble_sort(random)                               # сортування бульбашкою
    cp.disable()
    cp.print_stats()                                                    # аналітика складності

    failename_stop = 'stop_value_bubble.txt'                            # запис сортованого масиву методом бульбашки у файл
    save_txt_file(bubble_sort_arr, failename_stop)
    show_result_image(bubble_sort_arr, 'random.uniform.sort.bubble')    # графік візуалізації сортованих за бульбашкою даних



    # # ----------------- Аналітика складності - рівномірні дані ---------------
    # items_number = 10000
    # arr = [random.uniform(0, 99) for _ in range(items_number + 1)]
    # cp = cProfile.Profile()
    # cp.enable()
    # bubble_sort(arr)
    # cp.disable()
    # cp.print_stats()

