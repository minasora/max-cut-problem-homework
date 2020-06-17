import local_search as ls
import tabu_search as ts
import genenic_algroithm as ga
import simulated_annealing as sa
import max_cut_intance as m_instance
import copy
instance = m_instance.Problem_Instance("text.txt")
solution = ga.genetic_algorithm(instance)
print(solution.obj)