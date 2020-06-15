clear; clc; close all; % 清除变量/命令行窗口/所有图像
% 测试isMonge函数
wiki_monge = [10,17,13,28,23;17,22,16,29,23;24,28,22,34,24;11,13,6,17,7;45,44,32,37,23;36,33,19,21,6;75,66,51,53,34];
wiki_flag = isMonge(wiki_monge);
fprintf('维基百科的Monge矩阵算例测试结果为：%d\n',wiki_flag);

% 测试genMonge函数
% 测试不同大小的算例
m = 50:50:500;
n = round(repmat(m,3,1).*[1,1.4,0.6]');
num_m = length(m);
num_n_type = size(n,1);
num_sample = 20; % 每个尺寸的算例测试10个
flag = zeros(num_m,num_sample,num_n_type); % 初始化逻辑值矩阵
for i = 1:num_n_type
    for j = 1:num_m
        for k = 1:num_sample
            temp = genMonge(m(j),n(i,j)); % 生成Monge算例
            flag(j,k,i) = isMonge(temp); % 判断生成的算例是否为Monge矩阵
        end
    end
end
fprintf('genMonge(m,n)函数生成的算例是否全部通过：%d\n',all(flag,'all'));