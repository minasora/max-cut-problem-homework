import max_cut_instance as m_instance
import local_search as ls
import record_process as rp

# 初始化禁忌长度、最大迭代次数
tabu_len_multi = 0.1
Max_iters = 10000

def tabu_search(solution, instance, tabu_len_multi=tabu_len_multi, Max_iters=Max_iters):
    """
    禁忌搜索算法，返回迭代相应次数后得到的最优解
    :param solution:初始解
    :param instance:算例
    :param tabu_len_multi:禁忌长度乘数（禁忌长度=[节点数*禁忌长度乘数]）
    :param Max_iters:最大迭代次数
    :return:
    """
    tabu_len = int(instance.p * tabu_len_multi)  # 按节点数的百分比初始化禁忌长度
    tabu_list = [0 for i in range(instance.p)]  # 初始化禁忌表
    iter = 0  # 迭代次数
    best = solution.obj # 迭代当前最优值
    best_solution = solution
    record_data = "tabu_len: {}\n\n".format(tabu_len)

    while iter < Max_iters:
        solution_obj = solution.obj  # 当前解目标值
        local_temp = solution.updates[0]
        index = 0
        flag = 0
        record_data = record_data + "iteration: {}\n{}\nbest_obj: {}\n\n".format(iter,solution,best)
        print(solution.obj)

        for i in range(instance.p):
            temp = solution.updates[i]

            # 破禁准则
            if solution_obj + temp > best:
                index = i
                best = solution_obj + temp  # 破禁后更新最优值
                flag = 1
                break

            if tabu_list[i] != 0:  # 禁忌表数值非0时不予考虑
                continue
            elif temp > local_temp:
                local_temp = temp
                index = i

        solution = ls.flip(solution, index, instance)

        # 更新禁忌表
        tabu_list = [item - 1 if item > 0 else item for item in tabu_list]
        if flag == 0:  # 判断此次迭代是否为破禁后完成
            tabu_list[index] += tabu_len
        else:
            best_solution = solution  # 破禁后更新最优解

        iter += 1

    rp.record(record_data,"tabu")
    return best_solution
