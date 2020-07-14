import tabu_search as ts
import genenic_algroithm as ga
import simulated_annealing as sa
import max_cut_instance as m_instance
from plot_data import plot
import copy
import time

# 读取算例
instance = m_instance.Problem_Instance("text.txt")

# 对tabu、sa生成初始解
solution1 = m_instance.Problem_solution(instance)
solution2 = m_instance.Problem_solution(instance)
# print(solution1)
# print(id(solution1))
# print(solution2)
# print(id(solution2))

# 用各算法求解最大割问题
time0 = time.clock()
tabu_solution = ts.tabu_search(solution1, instance, 0.05, 1000)
time1 = time.clock()
sa_solution = sa.simulated_annealing(solution2, instance)
time2 = time.clock()
ga_solution = ga.genetic_algorithm(instance)
time3 = time.clock()

# 计算算法求解时间
elapse1 = time1-time0
elapse2 = time2-time1
elapse3 = time3-time2

# 绘制各算法对应图象
plot('tabu6.txt')
plot('sa.txt')
plot('ga.txt')

# 打印求解时间
print("Time used:",elapse1)
print("Time used:",elapse2)
print("Time used:",elapse3)