from typing import Dict, AnyStr, List


class Node:
    def __init__(self, name: AnyStr, neighbors: List):
        self.name = name
        self.neighbors = neighbors
        self.state = False
        self.trans_ori = '无'

    def check_node(self):
        print(self.name)
        for neighbor in self.neighbors:
            print(f"  --{neighbor['w']}--> {neighbor['name']}")

    def check_state(self):
        if self.state:
            print(f"{self.name}被{self.trans_ori}感染")
        else:
            print(f'{self.name}未被影响')


def get_graph():
    # w: 边的权重
    # 以这个概率来跑，基本上是影响不到其他节点～
    # node_info = {
    #     'a': [{'name': 'c', 'w': 0.2}],
    #     'b': [{'name': 'd', 'w': 0.5}, {'name': 'c', 'w': 0.3}],
    #     'c': [{'name': 'd', 'w': 0.1}, {'name': 'e', 'w': 0.2}],
    #     'd': [{'name': 'e', 'w': 0.2}],
    #     'e': [{'name': 'f', 'w': 0.6}],
    #     'f': [{'name': 'd', 'w': 0.3}, {'name': 'b', 'w': 0.4}, {'name': 'e', 'w': 0.6}],
    # }

    node_info = {
        'a': [{'name': 'c', 'w': 0.7}],
        'b': [{'name': 'd', 'w': 0.5}, {'name': 'c', 'w': 0.4}],
        'c': [{'name': 'd', 'w': 0.6}, {'name': 'e', 'w': 0.2}],
        'd': [{'name': 'e', 'w': 0.7}],
        'e': [{'name': 'f', 'w': 0.8}],
        'f': [{'name': 'd', 'w': 0.6}, {'name': 'b', 'w': 0.4}, {'name': 'e', 'w': 0.6}],
    }
    return {name: Node(name, neighbors) for name, neighbors in node_info.items()}

