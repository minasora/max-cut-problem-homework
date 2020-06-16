import local_search as ls
import tabu_search as ts
import genenic_algroithm as ga
import simulated_annealing as sa
import max_cut_intance as m_instance

instance = m_instance.Problem_Instance("text.txt")
solution = m_instance.Problem_solution(instance)
solution = sa.Simulated_Annealing(solution, instance)
print(solution.obj)
print(solution.get_obj(instance))



