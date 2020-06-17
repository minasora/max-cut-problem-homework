import max_cut_intance as m_instance

iterations = 1000


def slip(solution, i, instance):
    """
    将一个点转到另外一个集合
    :param solution:原来你的解
    :param i: 结点位置
    :return: 更新后的solution
    """
    solution.nodes[i] = 1 - solution.nodes[i]
    solution.update(instance, i)
    return solution


def local_search(solution, instance, iters=iterations):
    """
    邻域搜索
    :param solution:
    :param iters:
    :return:
    """
    for i in range(iters):
        t = solution.updates.index(max(solution.updates))
        solution = slip(solution, t, instance)
        if max(solution.updates) <= 0:  # 提前局部最优
            break
    return solution
