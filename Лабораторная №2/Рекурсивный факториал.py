def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    ...  # TODO реализовать рекурсивный алгоритм нахождения факториала
    if n < 0:
        raise ValueError
    if n == 1:
        return 1
    return factorial_recursive(n - 1) * n

print(factorial_recursive(5))