import max_cut_instance as m_instance
import random as rd
import copy
from local_search import flip
import record_process as rp

T = 30  # 种群数量
max_iters = 100  # 最大迭代次数
alpha = 0.1  # 突变概率


def crossover(solution_A, solution_B, instance):
    """
    对两个解进行交叉，交叉方式为2进制交叉
    :param solution_A:
    :param solution_B:
    :return: 两个子代
    """
    j = rd.randint(0, instance.p - 1)
    mid = solution_A.nodes[j]
    solution_A.nodes[j] = solution_B.nodes[j]
    solution_B.nodes[j] = mid
    solution_A.get_obj(instance)
    solution_B.get_obj(instance)
    return solution_A, solution_B


def select(solutions, instance, T):
    """
    选择：从solutions 中获得下一代，方法使用锦标赛算法
    :param solutions: 种群
    :return: new_solutions 新种群
    """
    new_solutions = []
    for t in range(T):
        i = rd.randint(0, T - 2)
        j = rd.randint(i + 1, T - 1)  # 不断随机找子代
        solution = copy.deepcopy(max(solutions[i:j]))
        new_solutions.append(solution)
    return new_solutions


def mutation(solution, instance):
    """
    突变,单点变异，随机取反一位
    :param solution:原来的解
    :return: 随机反转以后的解
    """
    i = rd.randint(0, instance.p - 1)
    flip(solution, i, instance)
    return solution


def genetic_algorithm(instance, T=T, max_iters=max_iters, alpha=alpha):
    """
    对给定问题实例进行遗传算法
    :param instance: 问题实例
    :return: 返回一个solution，种群中最优解
    """
    solutions = []
    record_data = 'T {} alpha {}\n\n'.format(T, alpha)

    for i in range(T):  # 构造初始解
        solution = m_instance.Problem_solution(instance)
        solutions.append(solution)
    for i in range(max_iters):
        iter = i
        for j in range(T):  # 交叉
            i = rd.randint(0, T - 1)
            j = rd.randint(0, T - 1)  # 随机生成两个子代
            solutions[i], solutions[j] = crossover(solutions[i], solutions[j], instance=instance)
        for i in range(T):
            pd = rd.random()
            if pd < alpha:
                mutation(solutions[i], instance)  # 一定概率发生突变
        solutions = select(solutions, instance, T)  # 选择
        solution = max(solutions)
        record_data = record_data + "generation: {}\n{}\n\n".format(iter, solution)
        print(solution.obj)
    solution = max(solutions)
    rp.record(record_data, "ga")
    return solution
