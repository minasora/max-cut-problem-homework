function flag = isMonge(A)
% flag = isMonge(A)
% 判断输入矩阵是否为Monge矩阵，输出1表示是，0表示不是。

diffA = diff(A,1,2); % 矩阵A每相邻两列的差分矩阵
sort_diffA = sort(diffA,'descend'); % 对差分矩阵各列降序排序
flag = all(diffA==sort_diffA,'all'); % 若矩阵A所有相邻两列的差分随行数递减，则说明矩阵A为Monge矩阵
end