
"""
Найкрутіше сортування
Time Complexity: ?
Auxiliary Space: ?

Що таке функція sort() Python?
https://www.geeksforgeeks.org/sort-in-python/
У Python sort()функція — це метод, який належить до списку.
Він використовується для сортування в python або елементів списку в порядку зростання за замовчуванням.
Метод sort()змінює оригінальний список на місці, тобто він змінює порядок елементів безпосередньо в існуючому об’єкті списку,
а не створює новий відсортований список.

"""

import cProfile
from rand_example import show_result_image, random_uniform


# Запуск на виконання
if __name__ == "__main__":

    # ------------------------------- найкрутіше сортування ----------------------------------
    arr = [1, 3, 5, 2, 4]
    print(sorted(arr), arr)

    # ---------------------- вихідні параметри об'єкта сортування ----------------------------
    a = 0
    b = 10
    iter = 10000
    failename_start = 'start_value.txt'
    failename_stop = 'stop_value.txt'

    # ---------------------- сортування випадкового масиву float ---------------------------

    random = random_uniform(a, b, iter)
    show_result_image(random, 'random.uniform')                         # графік візуалізації вхідних не сортованих даних
    random_sort = sorted(random)                                        # сортування методами numpy
    show_result_image(random_sort, 'random.uniform.sort')               # графік візуалізації сортованих даних


    # # ---------------------- Аналітика складності алгоритму  --------------------------------
    #
    # cp = cProfile.Profile()                                             # аналітика складності
    # cp.enable()
    # random_sort = sorted(random)                                        # круте сортування
    # cp.disable()
    # cp.print_stats()                                                    # аналітика складності






