% 该脚本用于测试getMin0,getMin1正确性
clc;clear;close;

% 初始化，生成Monge矩阵
m = 50:50:500;
dist = 2;
len = length(m);
n = m - dist;

% 测试不同规模下两种算法的正确性
for i = 1:len
    for j = 1:20
        % 随机生成该维数下的Monge矩阵
        A = genMonge(m(i),n(i));
        % 运行getMin0，getMin1,以及min函数
        [a0,b0,~] = getMin0(A);
        [a1,b1,~] = getMin1(A);
        [a,b] = find(A == min(min(A)));
        if (a0 == a(1)) && (b0 == b(1))
            fprintf('getMin0：结果正确\n');
        else
            fprintf('getMin0：结果错误\n');
        end
        if (a1 == a(1)) && (b1 == b(1))
            fprintf('getMin1：结果正确\n');
        else
            fprintf('getMin1：结果错误\n');
        end
    end
end