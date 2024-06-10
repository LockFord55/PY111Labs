"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    ...  # TODO реализовать итеративный линейный поиск
    if not arr:
        raise ValueError

    minimum_index = 0
    minimum = arr[minimum_index]

    for index, element in enumerate(arr):
        if element < minimum:
            minimum = element
            if element == minimum and index != minimum_index:
                minimum_index = index

    return minimum_index
