import matplotlib.pyplot as plt

def plot(file):
    """
    读取迭代过程数据并绘制对应目标值变化图线
    :param file:记录文件所在目录
    :return:
    """
    iters = []
    objs = []
    best_objs = []

    with open(file,'r') as f:
        data = f.read()
        iter_datas = data.split('\n\n')
        iter_datas.pop()  # 剔除末尾空值
        first_line = iter_datas.pop(0)  # 从数据中移除并读取第一行

        for iter_data in iter_datas:
            lines = iter_data.split('\n')
            # 获取对应数据
            iter = lines[0].split()[1]
            iters.append(int(iter))
            obj = lines[2].split()[1]
            objs.append(int(obj))
            try:
                best_obj = lines[3].split()[1]
                best_objs.append(int(best_obj))
            except Exception:
                print("当前文件无best_obj数据！")

    plot_iter(iters,objs,best_objs, first_line, file)

def plot_iter(iters,objs,best_objs, first_line, file):

    plt.figure(figsize=(16, 9), dpi=120)

    if 'tabu' in file:
        tabu_len = first_line.split()[1]  # 读取禁忌长度

        # 绘制图线
        plt.plot(iters, objs)
        plt.plot(iters, best_objs)
        plt.legend(['temp_obj', 'best_obj'])
    else:
        # 绘制图线
        plt.plot(iters, objs)
        plt.legend(['obj'])

    plt.xlabel('iters')
    plt.ylabel('objective')
    plt.title('Objective Value during the Iteration')

    # 存储并显示图线
    plt.savefig(file.replace('.txt','.png'))
    plt.show()