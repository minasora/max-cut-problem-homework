# 最大割问题优化算法

此次最大割问题课程作业使用python实现

## 代码介绍

该最大割问题优化算法代码主要包含六个部分：

- 读取数据（read_data.py）
- 自定义算例类文件（max_cut_instance.py）
- 邻域搜索与邻域动作（local_search.py）
- 三种优化算法实现（tabu_search.py/simulated_annealing.py/genetic_algorithm.py）
- 保存迭代记录与绘制图线（record_process.py/plot_data.py）
- 测试代码（test.py/test1.py，前者测试了三种算法，后者测试了不同禁忌长度下的禁忌搜索算法）

## 其他文件

- txt文件为对应算法的迭代过程记录文件，tabu后面的数字代表禁忌长度

- image文件夹内包含算法测试后生成的图象

