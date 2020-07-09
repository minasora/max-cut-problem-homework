import tabu_search as ts
import genenic_algroithm as ga
import simulated_annealing as sa
import max_cut_instance as m_instance
from plot_data import plot
import copy

# 读取算例
instance = m_instance.Problem_Instance("text.txt")

# 对tabu、sa生成初始解
solution1 = m_instance.Problem_solution(instance)
solution2 = copy.deepcopy(solution1)
# print(solution1)
# print(id(solution1))
# print(solution2)
# print(id(solution2))

# 用各算法求解最大割问题
# tabu_solution = ts.tabu_search(solution1, instance, 0.05, 1000)
sa_solution = sa.simulated_annealing(solution2, instance)
# ga_solution = ga.genetic_algorithm(instance)

# 绘制各算法对应图象
# plot('tabu.txt')
plot('sa.txt')
# plot('ga.txt')