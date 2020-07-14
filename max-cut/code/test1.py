import matplotlib.pyplot as plt
import tabu_search as ts
import max_cut_instance as m_instance
import copy

def plot(files):
    """
    读取迭代过程数据并绘制对应目标值变化图线
    :param files:记录文件所在目录列表
    :return:
    """
    iters = [[],[],[],[],[]]
    objs = [[],[],[],[],[]]
    best_objs = [[],[],[],[],[]]
    tabu_lens =[]

    for i in range(5):
        with open(files[i],'r') as f:
            data = f.read()
            iter_datas = data.split('\n\n')
            iter_datas.pop()  # 剔除末尾空值
            first_line = iter_datas.pop(0)  # 从数据中移除并读取第一行
            tabu_lens.append(first_line.split()[1])  # 读取禁忌长度

            for iter_data in iter_datas:
                lines = iter_data.split('\n')
                # 获取对应数据
                iter = lines[0].split()[1]
                iters[i].append(int(iter))
                obj = lines[2].split()[1]
                objs[i].append(int(obj))
                best_obj = lines[3].split()[1]
                best_objs[i].append(int(best_obj))

    plt.figure(figsize=(16, 9), dpi=150)
    for i in range(len(tabu_lens)):
        # 绘制图线
        plt.plot(iters[i], objs[i],linewidth=2)

    legends = ['temp_obj(tabu_len ={})'.format(tabu_len) for tabu_len in tabu_lens]
    plt.legend(legends)
    plt.xlabel('iters')
    plt.ylabel('objective')
    plt.title('Objective Value during the Iteration')

    plt.savefig('./image/tabu_all.png')
    plt.show()

    plt.figure(figsize=(16, 9), dpi=150)
    for i in range(len(tabu_lens)):
        # 绘制图线
        plt.plot(iters[i], best_objs[i],linewidth=2)

    legends = ['best_obj(tabu_len ={})'.format(tabu_len) for tabu_len in tabu_lens]
    plt.legend(legends)
    plt.xlabel('iters')
    plt.ylabel('objective')
    plt.title('Objective Value during the Iteration')

    # 存储并显示图线
    plt.savefig('./image/tabu_all_best.png')
    plt.show()

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
plot(['tabu{}.txt'.format(i) for i in [5,10,20,30,40]])