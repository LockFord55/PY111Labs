def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    ...  # TODO реализовать итеративный алгоритм нахождения факториала
    if n < 0:
        raise ValueError('Факториал считается от неотрицательных целых чисел.')

    factorial = 1
    for num in range(1, n+1):
        factorial *= num

    return factorial
