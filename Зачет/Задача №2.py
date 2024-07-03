def consensus(data: list[str]) -> str:
    """
    Функция получает на вход список 4-х символьных строк,
    и находит в них итеративно наиболее повторяющийся паттерн побуквенно
    :param data: список строк
    :return: консенсус-строку
    """
    if not data:
        raise ValueError('Ошибка! Введите список 4-х символьных строк!')
    for element in data:
        if not isinstance(element, str):
            raise TypeError('Ошибка! Все элементы должны быть типа str.')
        if len(element) != 4:
            raise ValueError('Ошибка! Все элементы должны быть 4-х символьны.')
    if len(data) == 1:
        return data[0]

    consensus_str = ''
    pattern = {}
    for run in range(4):
        for string in data:
            if string[run] not in pattern:
                pattern[string[run]] = 1
            else:
                pattern[string[run]] += 1
        if len(pattern) == 1:
            key = list(pattern.keys())
            consensus_str += str(key[0])
            pattern.clear()
        else:
            max_key_value = [0, 0]
            for key, value in pattern.items():
                if value == max_key_value[1] and key < max_key_value[0]:
                    max_key_value[0] = key
                if value > max_key_value[1]:
                    max_key_value[0] = key
                    max_key_value[1] = value
            consensus_str += str(max_key_value[0])
            pattern.clear()

    return consensus_str


if __name__ == '__main__':
    print(consensus(['ATTA', 'ACTA', 'AGCA', 'ACAA']))
