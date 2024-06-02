def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    ...  # TODO реализовать проверку скобочной группы
    queue = []
    for element in brackets_row:
        if element == ')' or element == '(':
            queue.append(element)
            if queue[0] == '(' and queue[-1] == ')':
                queue.pop()
                queue.pop(0)

    if not queue:
        return True
    else:
        return False


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
