import tabu_search as ts
import max_cut_instance as m_instance
import copy
from plot_data import tabu_plots

# 测试不同禁忌长度下的禁忌搜索算法
instance = m_instance.Problem_Instance("text.txt")
solution1 = m_instance.Problem_solution(instance)
solution2 = copy.deepcopy(solution1)
solution3 = copy.deepcopy(solution1)
solution4 = copy.deepcopy(solution1)
solution5 = copy.deepcopy(solution1)
tabu_solution = ts.tabu_search(solution1, instance, 0.04, 1000)
tabu_solution = ts.tabu_search(solution2, instance, 0.08, 1000)
tabu_solution = ts.tabu_search(solution3, instance, 0.16, 1000)
tabu_solution = ts.tabu_search(solution4, instance, 0.24, 1000)
tabu_solution = ts.tabu_search(solution5, instance, 0.32, 1000)
tabu_plots(['tabu{}.txt'.format(i) for i in [5,10,20,30,40]])