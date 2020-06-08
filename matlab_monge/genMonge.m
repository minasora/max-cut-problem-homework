function A = genMonge(m,n)
% Monge = genMonge(m,n)
% 随机生成元素为自然数的m*n的Monge矩阵A

A_c1 = round(rand(m,1)*50); % 随机生成矩阵A的第一列
rand_diff = round(rand(m,n)*30)-15; % 随机生成相邻两列的差分矩阵
sort_diff = sort(rand_diff,'descend'); % 将差分矩阵降序排序
A = cumsum([A_c1,sort_diff],2);% 用矩阵A的第一列加上累积差分矩阵得到Monge矩阵A
if any(A < 0, 'all') % 检验生成的矩阵A中是否存在负数
    A = A + abs(min(A,[],'all')) + round(rand(1,1)*10); % 加上最小的负数的绝对值，使矩阵A所有元素为自然数
end