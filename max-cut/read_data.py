import numpy as np
def read_data(file_name):
    """
    read data from txt
    :param file_name:
    :return: edge and nodes number p and edge number v
    """

    with open(file_name) as f:
        data = f.readlines()
    _,p,v = data[0].replace('\n','').split(' ')
    edges = np.zeros((int(p), int(p)))
    for i in data[1:]:
        if i == '\n':
            break
        line_data = i.split(' ')
        first, second = int(line_data[1]), int((line_data[2]).replace('\n', ''))
        first, second = min(first, second), max(first, second)
        edges[first-1, second-1] = 1 # 有边设为1

    return edges, int(p), int(v)