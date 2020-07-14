import numpy as np

def read_data(file_name):
    """
    read data from txt
    :param file_name:
    :return: edge and nodes number p and edge number v
    """

    with open(file_name) as f:  # 自动关闭打开的资源语句
        data = f.readlines()  # 读取所有行
    _, p, v = data[0].replace('\n', '').split(' ')
    edges = np.zeros((int(p), int(p)))  # 构建表示节点是否连接的矩阵
    for i in data[1:]:
        if i == '\n':
            break  # 读取到最后一行单独为换行符时跳出循环
        line_data = i.split(' ')  # 划分每一行中的三个数据
        first, second = int(line_data[1]), int((line_data[2]).replace('\n', ''))  # 获取对应数据，如：e 5 1\n中的5与1
        first, second = min(first, second), max(first, second)  # 小者在前，大者在后，即行数取小，只记一次
        edges[first - 1, second - 1] = 1  # 有边设为1

    return edges, int(p), int(v)  # 返回节点边长矩阵以及节点数与边数
