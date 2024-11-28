"""
Сортування злиттям
Time Complexity: O(n log(n))
Auxiliary Space: O(n)
"""

import cProfile
import random

def mergeSort(arr):
    if len(arr) > 1:
 
        # Знаходження середини масиву
        mid = len(arr) // 2
 
        # Поділ елементів масиву
        L = arr[:mid]
 
        # на 2 половини
        R = arr[mid:]
 
        # Сортування першої половинки
        mergeSort(L)
 
        # Сортування другої половинки
        mergeSort(R)
 
        i = j = k = 0
 
        # Копіювати дані до тимчасових масивів L[] і R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        #Перевірка, чи залишився якийсь елемент
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr


# Запуск на виконання
if __name__ == '__main__':


    # --------------- Демонстрація роботи ------------------
    # arr = [12, 11, 13, 5, 6]
    # print('Вхід: ', arr)
    # size = len(arr)
    # arr_out = mergeSort(arr)
    # print('Вихід: ', arr_out)

    # ----------------- Аналітика складності ---------------

    cp = cProfile.Profile()
    items_number = 1000000
    arr = [random.uniform(0, 99) for _ in range(items_number + 1)]
    size = len(arr)
    cp.enable()
    mergeSort(arr)
    cp.disable()
    cp.print_stats()

