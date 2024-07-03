from random import randint
import time


def qsort(container: list[int]) -> list[int]:
    if len(container) > 1:
        middle = container[len(container) // 2]
        left_container = []
        right_container = []
        equal_container = []

        for element in container:
            if element < middle:
                left_container.append(element)
            elif element > middle:
                right_container.append(element)
            else:
                equal_container.append(element)
        return qsort(left_container) + equal_container + qsort(right_container)

    return container


if __name__ == '__main__':
    massive = [randint(13, 25) for i in range(10 ** 6)]
    start1 = time.time()
    print(qsort(massive))
    end1 = time.time()
    print((end1 - start1) * 10 ** 3)

""" 
Выбрал быструю сортировку, т.к.:
1) на таком крупном массиве маловероятно, что будут эффективны сортировки пузырьком и подсчётами из-за сложности N^2
2) конкурент - сортировка слиянием - показала в среднем в 10 раз худший результат по времени 
(в среднем 400 vs 4000 за 10 итераций)
"""
