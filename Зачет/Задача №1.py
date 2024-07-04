# def counter(n: int, k: int) -> int:
#     """
#     Функция итеративным способом определяет, кто вылетает на K-слоге считалочки,
#     и находит последнего оставшегося человека из первоначальных N-людей.
#
#     :param n: Количество человек
#     :param k: Количество слогов
#     :return: Номер последнего оставшегося человека
#     """
#
#     people = [i for i in range(1, n + 1)]
#
#     count = 0
#     while len(people) > 1:
#         for player in people:
#             count += 1
#             if count % k == 0:
#                 if player == people[-1]:
#                     people.remove(player)
#                     break
#                 people.remove(player)
#                 count += 1
#                 print(people)
#
#     return people[0]

def make_massive(n):
    massive = [i for i in range(1, n + 1)]
    return massive


def counter(massive, k):
    if len(massive) == 2:
        return massive[1]
    k -= 1
    if k > len(massive):
        k = k - len(massive)
    massive.pop(k)
    return counter(massive, k + 3)


if __name__ == '__main__':
    print(counter(make_massive(7), 3))
