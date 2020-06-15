% 该脚本用于测试并比较getMin0与getMin1的效率
% test函数用于测试并输出数据
clc;clear;close;

% 初始化
m = 50:50:500;% 此处可以修改输入，代表不同规模的矩阵
dist = [1,0.4,0.6,1.4];% 可以修改数值，但由于下方子图是以2*2得到的，长度不可更改

% 绘制图像
for i = 1:4
    [t_r0,t_r1,c_r0,c_r1] = test(m,dist(i));
    
    figure(1);
    subplot(2,2,i)
    plot(m,t_r0,'o-',m,t_r1,'^-');
    xlabel('m');
    ylabel('average time');
    title(['不同维数（m*n）矩阵下两种算法平均运算时间（n=',num2str(dist(i)),'m）']);
    legend('getMin0','getMin1','location','northwest');
    
    figure(2);
    subplot(2,2,i)
    plot(m,c_r0,'o-',m,c_r1,'^-');
    xlabel('m');
    ylabel('compare times');
    title(['不同维数（m*n）矩阵下两种算法平均比较次数（n=',num2str(dist(i)),'m）']);
    legend('getMin0','getMin1','location','northwest');
end

% 测试并输出数据
function [t_result0,t_result1,c_result0,c_result1] = test(m,dist)

% 构造不同规模的输入
n = round(m .* dist);
len = length(m);
% 记录getMin0运算时间的矩阵，一行为同一矩阵维数下不同Monge矩阵的运算时间
t0 = zeros(len,20);
% 记录getMin1运算时间的矩阵，一行为同一矩阵维数下不同Monge矩阵的运算时间
t1 = zeros(len,20);
% 记录getMin0比较次数的矩阵，一行为同一矩阵维数下不同Monge矩阵的比较次数
c0 = zeros(len,20);
% 记录getMin1比较次数的矩阵，一行为同一矩阵维数下不同Monge矩阵的比较次数
c1 = zeros(len,20);

% 测试不同规模下两种算法的计算时间
for i = 1:len
    for j = 1:20
        % 随机生成该维数下的Monge矩阵
        A = genMonge(m(i),n(i));
        % 记录getMin0的计算时间与比较次数
        tic;[~,~,calc_times] = getMin0(A);toc;
        t0(i,j) = toc;
        c0(i,j) = calc_times;
        % 记录getMin1的计算时间与比较次数
        tic;[~,~,calc_times] = getMin1(A);toc;
        t1(i,j) = toc;
        c1(i,j) = calc_times;
    end
end

% 求各维数矩阵算例平均计算时间
t_result0 = mean(t0,2)';
t_result1 = mean(t1,2)';
% 求各维数矩阵算例平均比较次数
c_result0 = mean(c0,2)';
c_result1 = mean(c1,2)';
end
