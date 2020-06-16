from read_data import read_data
import random as rd
import numpy as np


class Problem_Instance:
    """
    the instance of a problem, consist of p,v and edge
    """
    p = 0
    v = 0
    edges = []

    def __init__(self, file_name):
        self.edges, self.p, self.v,  = read_data(file_name)


class Problem_solution:
    """
    a solution to the max-cut problem. '0' '1'  in the nodes which represents the in
    """
    nodes = []
    obj = 0
    updates = [] # 维护一个矩阵，储存了节点i 从0-1的obj的变化值

    def __init__(self, instance):
        """
        init from a instance
        :param instance:
        """
        for i in range(instance.p):
            self.nodes.append(rd.randint(0, 1)) # 随机划分两个集合
            self.updates.append(0)
        for i in range(instance.p):
            delta = 0
            for j in range(instance.p):
                if instance.edges[min(i, j), max(i, j)] == 1 :
                    if self.nodes[i] + self.nodes[j] == 1: # 已经相连的
                        delta += 1
                    else:
                        delta -= 1
            self.updates[i] = - delta
        self.get_obj(instance)

    def get_obj(self, instance):
        """
        对解进行更新
        :param instance:
        :return:
        """
        self.obj = 0
        for i in range(instance.p):
            for j in range(i, instance.p):
                if instance.edges[i, j] == 1 and self.nodes[i] != self.nodes[j]:
                    self.obj += 1
        return self.obj

    def update(self, instance, i):  # 反转节点i后对解进行更新
        self.obj = self.obj + self.updates[i]
        for j in range(instance.p):
            if j == i:
                self.updates[j] = -self.updates[j] # 原来的变负
            elif instance.edges[min(i, j), max(i, j)] == 1: # 假如i，j有边连接
                if self.nodes[i] + self.nodes[j] == 1:
                    self.updates[j] -= 2 # 原来已在一个集合的-=2
                else:
                    self.updates[j] += 2 # 原来不在一个集合的+=2



