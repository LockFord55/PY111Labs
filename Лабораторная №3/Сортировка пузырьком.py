from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    ...  # TODO реализовать алгоритм сортировки пузырьком
    if not container:
        return []
    if len(container) == 1:
        return container

    last_element_index = len(container) - 1
    for run in range(last_element_index, 0, -1):
        for index in range(run):
            if container[index] > container[index + 1]:
                container[index], container[index + 1] = container[index + 1], container[index]
    return container
