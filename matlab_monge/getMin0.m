function [a,b,calc_times] = getMin0(A)
% [a,b,calc_times] = getMin0(A)
% 返回矩阵A中最小元素的行列索引
% 实现MATLAB内置函数min，根据官方说明，若有多个最小元素，只返回第一个元素的行列索引

% 获取矩阵A的行数与列数
[m,n] = size(A); 

% 初始化变量
min_val = A(1,1);
min_row = 1;
min_col = 1;
calc_times = 0;

% 遍历寻找最小值
for i = 1:m
    for j = 1:n
       temp = A(i,j);
       if temp < min_val
          min_val = temp;
          min_row = i;
          min_col = j;
       end
    end
    calc_times = calc_times + n;
end

% 返回最小元素位置
a = min_row;
b = min_col;
end

