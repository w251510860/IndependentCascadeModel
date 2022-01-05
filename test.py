from typing import List

from gen_graph import get_graph, Node
from random import random


def infl(node: Node, graph_data):
    infl_nodes = []
    for neighbor in node.neighbors:
        if graph_data[neighbor['name']].state:
            continue
        w = random()
        if w <= neighbor['w']:
            infl_nodes.append(neighbor['name'])
    return infl_nodes


def start(graph_data, infl_queue: List):
    while len(infl_queue) > 0:
        node = infl_queue.pop()
        infl_nodes = infl(graph_data[node], graph_data)
        for infl_node in infl_nodes:
            graph_data[infl_node].state = True
            graph_data[infl_node].trans_ori = node
        infl_queue.extend(infl_nodes)

    return graph_data


if __name__ == '__main__':
    graph_data = get_graph()
    infl_queue = ['b']
    graph_data = start(graph_data, infl_queue)
    for _, node in graph_data.items():
        node.check_state()

