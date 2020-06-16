import local_search as ls
import max_cut_intance as m_instance
import random as rd
import math
T = 100000 # 温度
T_min = 100 # 冷却温度
Max_iters = 100000 # 最大迭代次数
r = 0.99 # 降火

def E_evaluation(delta, T):
    """
    返回多大可能接受新解
    :param obj:
    :param new_obj:
    :return: 概率
    """
    if delta > 0:
        return 0
    else:
        return math.exp(delta/T)

def Annealing(T):
    """
    退火
    :param T:
    :return:
    """

def Simulated_Annealing(solution, instance , T = T, T_min = T_min, Max_iters = Max_iters, r = r):
    iter = 0
    while iter < Max_iters and T > T_min:
        i = rd.randint(0, instance.p-1)
        delta = -solution.updates[i]
        p = E_evaluation(delta, T)
        p_rd = rd.random()
        if p_rd < p:
            solution = ls.slip(solution, i, instance)
        T = r*T
    return solution
