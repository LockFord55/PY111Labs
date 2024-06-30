from typing import Union

import networkx as nx
from matplotlib import pyplot


def make_graph(weight_list: Union[list, tuple]) -> nx.DiGraph:
    """
    Функция на основе стоимости шагов, создает граф, экземпляр класса NetworkX

    :param weight_list: массив, содержащий стоимости шагов по графу
    :return: взвешенный направленный граф NetworkX
    """
    nodes_and_edges = []
    for i in range(len(weight_list)):
        nodes_and_edges.append((i, i+1, weight_list[i]))
        if weight_list[i] != weight_list[-1]:
            nodes_and_edges.append((i, i+2, weight_list[i+1]))

    graph = nx.DiGraph()
    graph.add_weighted_edges_from(nodes_and_edges)

    # nx.draw_spring(graph, node_color='blue', node_size=1000, with_labels=True, arrows=True)
    # pyplot.show()

    return graph


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    ...  # TODO c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы
    shortcut = nx.dijkstra_predecessor_and_distance(graph, 0)
    for node in graph.nodes:
        if node not in shortcut[1]:
            shortcut[1][node] = float('inf')
    result_list = list(shortcut[1].values())
    return result_list[-1]


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = make_graph(stairway)  # TODO функция, которая формирует граф по стоимости ступеней
    print(stairway_path(stairway_graph))  # 72
