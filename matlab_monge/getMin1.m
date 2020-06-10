function [a,b,calc_times] = getMin1(A)
% [a,b,calc_times] = getMin1(A)
% 返回Monge矩阵中最小元素的行列索引
% 利用了Monge矩阵行（列）最小元素所在列（行）数递增的特殊性质

% 获取矩阵的行列数
[m,n] = size(A);

% 初始化下一次搜索迭代的初始位置
col = 1;
row = 1;
% 初始化记录搜索过程中得到的所有候选最小元素的矩阵
% 第一行为元素值，第二行记录元素行索引，第三行记录元素列索引
cand = [];
% 初始化用于判断搜索范围是否有效的变量
s1=1;s2=1;
% 记录比较次数
calc_times = 0;

% 搜寻行列最小元素
% 终止条件为行列搜索最小元素索引只有一个不同或下一次搜索坐标无效
% 难点在于几种特殊情况的处理（都在左上角/最后一次搜索的范围为一行或一列）
while s1 > 0 && s2 > 0
    
    % 更新终止条件变量，当s1/s2=0意味着已经到了边界，该次搜索是最后一次搜索
    s1 = n - col;
    s2 = m - row;
    
    % 搜索行（列）最小元素所在列（行）
    y = col - 1 + find_min(A(row,col:n));
    x = row - 1 + find_min(A(row:m,col));
    
    % 若行列最小元素有一者在左上角，下一次搜索的开始位置需要特意更新
    if y ~= col && x ~= row % 行列都不在左上角
        % 更新记录候选最小元素的矩阵
        cand = [cand,[A(row,y);row;y],[A(x,col);x;col]];
        % 更新下一次搜索迭代的初始位置
        col = y;
        row = x;
    elseif y == col && x == row % 行列最小元素都在左上角
        % 更新记录候选最小元素的矩阵
        cand = [cand,[A(x,y);x;y]];
        % 更新下一次搜索迭代的初始位置
        col = y+1;
        row = x+1;
    elseif x == row % 列最小元素在左上角
        % 更新记录候选最小元素的矩阵
        cand = [cand,[A(x,y);x;y],[A(row,y);row;y]];
        % 更新下一次搜索迭代的初始位置
        col = y;
        row = x+1;
    else % 行最小元素在左上角
        % 更新记录候选最小元素的矩阵
        cand = [cand,[A(x,y);x;y],[A(x,col);x;col]];
        % 更新下一次搜索迭代的初始位置
        col = y+1;
        row = x;
    end
    calc_times = calc_times + s1 + s2 + 2;
end

% 比较候选矩阵里的最小值，返回行列
temp = find_min(cand(1,:));
a = cand(2,temp);
b = cand(3,temp);

% 记录比较次数
calc_times = calc_times + size(cand,2);
end

% 子函数，返回一维向量里最小元素的位置
function [min_loc] = find_min(v)
    % 初始化最小元素
    min_val = v(1);
    min_loc = 1;
    for i = 1:length(v)
        temp = v(i);
        if temp < min_val
            min_val = temp;
            min_loc = i;
        end
    end
end