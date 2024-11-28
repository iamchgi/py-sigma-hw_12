

'''

МОДЕЛЬ: рівномірного закону розподілу випадкових величин (ВВ) для сортування.
Довідковий матеріал:
https://numpy.org/doc/stable/reference/random/generator.html
https://www.w3schools.com/python/numpy/numpy_random_exponential.asp
https://numpy.org/doc/stable/reference/random/generated/numpy.random.exponential.html
https://www.geeksforgeeks.org/numpy-random-exponential-in-python/
https://numpy.org/doc/stable/reference/random/generated/numpy.random.chisquare.html

Package                      Version
---------------------------- -----------
pip                          23.1
numpy                        1.23.5
matplotlib                   3.6.2

'''

import numpy as np
import matplotlib.pyplot as plt
import random


# ----------------------- рівномірний закон розводілу - десяткове числення -----------------------
def random_uniform(a, b, iter):
    '''
    Функція генерування випадкових величин за рівномірним законом - float
    :param a: ліва межа зміни значень / довірчого інтервала
    :param b: права межа зміни значень / довірчого інтервала
    :param iter: кількість елементів, що генерується
    :param failename: імя файлу куди записується результат
    :return: вибірка значень рівномірно розподілених в межах a, b, з кількістю iter - десяткова система числення
    '''

    S = np.zeros((iter))
    for i in range(iter):
        S[i] = np.random.uniform(a, b)  # параметри закону задаются межами аргументу

    return S


# ----------------------- рівномірний закон розводілу - цілі числа -----------------------
def random_uniform_int(a, b, iter):
    '''
    Функція генерування випадкових величин за рівномірним законом з параметрами - int
    :param a: ліва межа зміни значень / довірчого інтервала
    :param b: права межа зміни значень / довірчого інтервала
    :param iter: кількість елементів, що генерується
    :param failename: імя файлу куди записується результат
    :return: вибірка значень рівномірно розподілених в межах a, b, з кількістю iter - десяткова система числення
    '''

    S = np.zeros(iter, dtype=int)
    for i in range(iter):
        S[i] = random.randint(a, b)  # параметри закону задаются межами аргументу

    return S

def data_str(filename):
    with open(filename, "r", encoding='utf-8'):
        nums = []
        for i in open(filename):
            nums.append(i)  # читання файлу по рядках і заповнення списку результатом
    print(nums)
    return nums


def save_txt_file(S, filename):
    '''
    Функція запису випадкової вибірки у файл
    :param S: масив випадкових значень - вибірка
    :param failename: і'мя файла
    :return: нічого
    '''
    np.savetxt(filename, S)

    return


def show_result_image(S, text):
    '''
    Функція візуалізації дискретного ряду
    :param S: вхідний масив дискретних даних
    :param text: повідомлення
    :return: нічого
    '''

    plt.plot(S)
    plt.ylabel(text)
    plt.show()
    return


def np_sort(S):
    '''
    Функція сортування
    :param S: об'єкт сортування
    :return: результат сортування
    https://numpy.org/doc/stable/reference/generated/numpy.sort.html
    '''
    S_sort = np.sort(S)
    return S_sort


if __name__ == '__main__':

    a = 0
    b = 10
    iter = 1000
    ailename_start = 'start_value.txt'
    ailename_stop = 'stop_value.txt'
    filename_str = 'text_file.txt'

    # random = random_uniform_int(a, b, iter)
    # data_str(filename_str)

    random = random_uniform(a, b, iter)
    save_txt_file(random, ailename_start)
    show_result_image(random, 'random.uniform')
    random_sort = np_sort(random)
    show_result_image(random_sort, 'random.uniform.sort')
    save_txt_file(random_sort, ailename_stop)


