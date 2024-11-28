"""
Алгоритм сортування вставкою
Time Complexity: O(n^2)
Auxiliary Space: O(1)
"""

import cProfile
import random
  
# Функція алгоритму сортування вставкою
def insertion_sort(arr):
  
    # Перехід черех 1 до len(arr)
    # Підрахунок ітерацій: метод enumerate() додає лічильник до ітерованого arr і повертає його у формі об’єкта перерахування.
    for i, key in enumerate(arr):

        # Перемістити елементи arr[0..i-1], тобто
        # більше ключа key, на одну позицію вперед їхньої поточної позиції
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

    return arr


# Запуск на виконання
if __name__ == "__main__":


    # --------------- Демонстрація роботи ------------------
    # arr = [12, 11, 13, 5, 6]
    # print('Вхід: ', arr)
    # arr_out = insertion_sort(arr)
    # print('Вихід: ', arr_out)


    # ----------------- Аналітика складності ---------------
    items_number = 10000
    arr = [random.uniform(0, 99) for _ in range(items_number + 1)]
    cp = cProfile.Profile()
    cp.enable()
    insertion_sort(arr)
    cp.disable()
    cp.print_stats()
