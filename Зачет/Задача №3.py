from typing import Union


def check_time(data: Union[list[tuple], tuple[tuple]]) -> bool:
    """
    Функция на основе полученных заявок формата (время начала, время окончания), проверяет, возможность удовлетворить
    все заявки одной ракетой за один день.
    :param data: Массив данных, содержащий кортежи из двух целых числительных
    :return: возвращает true/false в зависимости от результата проверки
    """
    if not data:
        raise ValueError
    for time in data:
        if len(time) > 2:
            raise IndexError('Ошибка, кортеж с временем должен включать лишь 2 элемента!')
        if type(time[0]) is not int or type(time[1]) is not int:
            raise TypeError('Ошибка, время должно быть типа int!')
        if time[0] > time[1]:
            raise ValueError('Ошибка, время начала должно быть меньше времени окончания!')
        if time[0] == time[1]:
            raise ValueError('Ошибка, время начала не может совпадать с временем окончания!')
        if not (1 <= time[0] <= 24) or not (1 <= time[1] <= 24):
            raise ValueError('Ошибка, время должно быть в диапазоне от 1 до 24!')

    if len(data) == 1:
        return True

    data_sorted = sorted(data, key=lambda x: x[0])  # Или тоже необходимо было вручную реализовать?

    ending_time = None
    for time in data_sorted:
        if ending_time is None:
            ending_time = time[1]
            pass
        else:
            if ending_time > time[0]:
                return False
            else:
                ending_time = time[1]
    return True


if __name__ == '__main__':
    data_list1 = [(1, 5), (6, 7), (7, 13), (15, 20)]
    data_list2 = [(13, 15), (15, 20), (18, 23)]
    print(check_time(data_list1))
    print(check_time(data_list2))
    