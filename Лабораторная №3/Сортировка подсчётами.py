from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    ...  # TODO реализовать алгоритм сортировки подсчетами

    if len(container) == 1:
        return container

    # Проходим по массиву элементов, запоминаем уникальные элементы и их количество
    counter = {}
    for element in container:
        if element not in counter:
            counter[element] = 1
        else:
            counter[element] += 1

    massive = list(counter.keys())

    # Отсортируем ключи словаря сортировкой пузырьком
    n = len(massive)
    for run in range(n - 1):
        for i in range(n - 1 - run):
            if massive[i] > massive[i + 1]:
                massive[i], massive[i + 1] = massive[i + 1], massive[i]

    # Соберем воедино массив
    result_list = []
    for element in massive:
        for run in range(counter[element]):
            result_list.append(element)

    return result_list
