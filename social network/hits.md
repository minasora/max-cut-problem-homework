#### 思路

Github中节点的互相follow关系显然为一有向图。这和网页中的链接关系非常类似。所以我们考虑使用HITS算法对各个用户的hub和authority属性进行分析。

#### 算法

##### 基本假设

在Github社交网络中使用HITS算法的基本假设如下：

- 一个高authority用户会被很多高hub用户所follow。
- 一个高hub用户会follow很多高authority的用户。

##### 算法原理

为了得到每个用户的hub值和authority值，我们用以下方法确定：

- 用户hub值等于所有它follow的用户的authority值之和。
- 用户authority值等于所有follow它的用户的hub值之和。

##### 改进

和网页不同，Github用户自带stars属性，同样反应了用户的权威性，因此我们以该值作为各节点的初始值，以更好的反应其性质。

##### 具体流程

1. 设定迭代次数$k$
2. 每个节点按stars数赋初始$hub$值和$authority$值
3. 重复$k$次：
   - 更新$hub$值：每个节点的$hub$值=$\sum(该节点指向节点的authority值)$
   - 更新$authority$值：每个节点的$authority$值=$\sum(指向该节点的节点的hub值)$
   - 标准化各节点的两个得分