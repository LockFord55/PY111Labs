from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    ...  # TODO решить задачу с помощью динамического программирования

    # Создаем поле
    field = []
    for row in range(n):
        field.append([0] * m)

    # Первоначальное известное состояние
    for i in range(1, n):
        field[i][0] = 1
    for j in range(1, m):
        field[0][j] = 1

    # Заполняем первую строку
    for element in range(1, m):
        field[1][element] = field[1][element - 1] + 2

    # Само построение
    for row in range(2, n):
        for col in range(1, m):
            field[row][col] = field[row - 1][col] + 2

    for row in range(n):
        print(field[row])

    return field


if __name__ == '__main__':
    paths = car_paths(4, 2)
    #print(paths[-1][-1])  # 7
