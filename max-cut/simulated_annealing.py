import local_search as ls
import record_process as rp
import max_cut_instance as m_instance
import random as rd
import math

T = 10000  # 温度
T_min = pow(10,-5)  # 冷却温度
Max_iters = 10000  # 最大迭代次数
r = 0.99  # 降火


def E_evaluation(delta, T):
    """
    返回多大可能接受新解
    :param obj:
    :param new_obj:
    :return: 概率
    """
    if delta > 0:
        return 1
    else:
        return math.exp(delta / T)

def simulated_annealing(solution, instance, T=T, T_min=T_min, Max_iters=Max_iters, r=r):
    """
    模拟退火算法
    :param solution:
    :param instance:
    :param T:
    :param T_min:
    :param Max_iters:
    :param r:
    :return: 迭代对应次数所得解
    """
    iter = 0
    record_data = 'T {} T_min {} r {}\n\n'.format(T, T_min, r)

    while iter < Max_iters and T > T_min:
        record_data = record_data + "iteration: {}\n{}\n\n".format(iter, solution)
        i = rd.randint(0, instance.p - 1)
        delta = solution.updates[i]
        p = E_evaluation(delta, T)
        p_rd = rd.random()
        print(iter,solution.obj,T,p)

        if p_rd < p:
            solution = ls.flip(solution, i, instance)

        T = r * T
        iter += 1

    rp.record(record_data,"sa")
    return solution
