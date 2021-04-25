

# 排列与组合

如何计数？

## 加法与乘法法则

加法：一步完成

乘法：分部完成

画模式

## 一一对应

Cayley定理：过有 $n$ 个标志顶点的树的数目为 $n^{n-2}$.

树：n 个顶点构成的连通图，无环。

假设树 T 是其中一棵树，依次删除其中标号最小的叶子节点, 并依次记下与叶子相连的结点标号：$b_1,b_2,...,b_{n-2}$，最后两个叶子节点不用删。那么，树 T 可由序列 $b_1,b_2,...,b_{n-2}$ 恢复：

对于$b_1$, 从序列 $1, 2,...,n$ 中取不再序列 $b_1,b_2,...,b_{n-2}$ 中的最小数，即为与 $b_1$ 对应的叶子节点$a_1$，找到$b_1$的对应节点之后，依次将他们中对应中的序列删除。依此可以重构整棵树 T.

由于序列 $b_1,b_2,...,b_{n-2}$ 共有 $n^{n-2}$ 种可能，故树的数目为: $n^{n-2}$。



## 排列

 一般排列（无重复 元）

圆周排列

可重复元排列





## 组合

一般组合（无重复元）

可重复组合

不相邻组合





## 组合恒等式

$$
\begin{align}
C(n,r)&=C(n-1,r)+C(n-1,r-1)\\
C(n,l)C(l,r)&=C(n,r)C(n-r,l-r)\\
C(m+n,r)&=C(m,0)C(n,r)+C(m,1)C(n,r-1)+\dots+C(m,r)C(n,0)\\
C(m+n,m)&=C(m,0)C(n,m)+C(m,1)C(n,m-1)+\dots+C(m,m)C(n,0)\\
&=C(m,m)C(n,m)+C(m,m-1)C(n,m-1)+\dots+C(m,0)C(n,0)\\
C(n+1,r+1)&=C(n,r)+C(n-1,r-1)+\dots+C(r,r)
\end{align}
$$





# 母函数

无序：普通型：$G(x)=\sum_{n=0}^{\infty}a_nx^n$

有序：指数型：$G_e(x)=\sum_{n=0}^{\infty}a_n\frac{x^n}{n!}$



广义牛顿二项式定理：
$$
(1+x)^{\alpha} = \sum \frac{\alpha(\alpha-1)(\alpha-2)\dots(\alpha-k+1)}{k!}x^k
$$




## Ferrers 图像

Ferrers 图像：一个自上而下的n层格子，$n$ 为第 $i$ 层的格子数。当 $n_i \ge n_{i+1}$ 时，即上层的格子数不小于下层的格子数时，称之为 Ferrers 图像。

性质：

- 每层至少一个格子。
- 第一行与第一列互换，第二行与第二列互换...所得的图像任然是 Ferrers 图像，并称他们是共轭的。



自共轭： Ferrers 图像和它的共轭相等。 

例：整数 $n$ 拆分为互不相同的若干个奇数和的拆分数等于把 $n$ 拆分成自共轭的 Ferrers 图像的拆分数相等。



## 指数型母函数



问题：

设有 n 个元素，其中 $a_1$ 重复了 $n_1$ 次， 其中 $a_2$ 重复了 $n_2$ 次，$\dots$ ，其中 $a_k$ 重复了 $n_k$ 次， 且 $n_1+n_2\dots+n_k=n$，从中取 $r$ 个，请问有多少中**排列**方法？



指数型母函数的定义：
$$
G_e(x)=a_0+a_1\frac{x}{1!}+\dots+a_n\frac{x^n}{n!}
$$


例：

设有 7 个有区别的球，放入4个有标志的盒子，要求第1，2个盒子含有偶数个球，第3个盒子含有奇数个球，有多少种分配方案？

解：

第1，2盒子：$1+\frac{x^2}{2!}+\frac{x^4}{4!}+\dots=\frac{e^x+e^{-x}}{2}$

第3盒子：$\frac{x^1}{1!}+\frac{x^3}{3!}+\dots=\frac{e^x-e^{-x}}{2}$

第4盒子：$1+\frac{x}{1!}+\frac{x^2}{2!}+\dots=e^x$

$G(x)=(\frac{e^x+e^{-x}}{2})^2(\frac{e^x-e^{-x}}{2})e^x=\frac{e^{4x}+e^{2x}-e^{-2x}-1}{8}$



## 递推关系





线性常系数齐次递推关系: $a_n+c_1a_{n-1}+...+c_ka_{n-k}=0$ ，已知 $a_0, a_1,...,a_{k-1}$。



1）特征方程无重根：

$(x-x_1)(x-x_2)...(x-x_k)=0$

$a_n=\sum A_ix_i^n$



2）k重根 $(x-x_k)^k=0$ 对应的项：

$(h_1n^{k-1}+h_2n^{k-2}+...+h_{k-1})x_k^n$



线性常系数非齐次递推关系: $a_n+c_1a_{n-1}+...+c_ka_{n-k}=b_n$ ，已知 $a_0, a_1,...,a_{k-1}$。









汉诺塔问题的递推式：
$$
h(n)=
\begin{cases}
2h(h-1)+1, \quad n>1\\
1, \quad n=1
\end{cases}
$$





## 错排问题

给定n个元素，他的每个元素都有一个指定的位置，若一个排列使得每个元素都不在指定位置上，则称这个排列为一个错排。

【解】

不妨设 $p_i\not =i, i=1,2,\dots,n$

当 n=1 时，错排数$D_1=0$

当n=2 时，错排数为$D_2=1$ 

假设 $p_n=i,1\le i<n$，

若$p_i=n$，则相当于相当于剩余的n-2个元素作错排 $D_{n-2}$

若$p_i\not = n$，则相当于n-1个元素作错排：$D_{n-1}$

由于 $p_n$ 可以有 $n-1$ 中选择， 故

$D_n=(n-1)(D_{n-1}+D_{n-2})$

$D_n-nD_{n-1}=-(D_{n-1}-(n-1)D_{n-2})$



## 多项式系数

$(x_1+x_2+\dots+x_n)^n=\sum C(n,n_1,\dots,n_m) x_1^{n_1}x_2^{n_2}\cdots x_m^{n_m}$

其中系数$C(n,n_1,\dots,n_m)=\frac{n!}{n_1!n_2!\cdots n_m!}$

它的项数为$C(n+m-1,n)$



## stirling数

第一类：$F_n=x(x+1)\cdots(x+n-1)=S(n,n)x^n+S(n,n-1)x^{n-1}+\cdots+S(n,1)x+S(n,0)$

第二类：n个有区别的球放入m个相同的盒子中，要求无一空盒，其方案数 $S(n,m)$称为第二类stirling数。

性质：

$S(n,k)=0,k>n$

$S(n,1)=1$

$S(n,n)=1$

$S(n,2)=2^{n-1}-1$

$S(n,n-1)=C(n,2)$



任选一个球A，如果它独占一个盒子，则剩下球的方法数：S(n-1,m-1)

如果它不独占一盒，先把其他球放入盒子：$S(n-1,m)$，再把球A放入一个盒子：$mS(n-1,m)$

所以$S(n,m)=mS(n-1,m)+S(n-1,m-1)$



| n个球有无区别 | m个盒子有无区别 | 有无空盒 | 方案数                                                       |
| ------------- | --------------- | -------- | ------------------------------------------------------------ |
| 有            | 有              | 有       | $m^n$                                                        |
| 有            | 有              | 无       | $m!S(n,m)$                                                   |
| 有            | 无              | 有       | $S(n,1)+S(n,2)+\cdots+S(n,m)$                                |
| 有            | 无              | 无       | $S(n,m)$                                                     |
| 无            | 有              | 有       | $C(m+n-1,n)$                                                 |
| 无            | 有              | 无       | $C(n-1,m-1)$                                                 |
| 无            | 无              | 有       | $G(x)=\frac{1}{(1-x)(1-x^2)\cdots(1-x^m)}$ 中$x^n$ 的系数，拆分 |
| 无            | 无              | 无       | $G(x)=\frac{x^m}{(1-x)(1-x^2)\cdots(1-x^m)}$ 中$x^n$ 的系数， |



## catalan数

数 $c_n=\frac{1}{n+1}C(2n,n)$ 称为第 n 个 catalan 数。



【例1】在一个凸 $n+1$边形在其内部插入不相交的对角线，将其分解为一些三角形，有多少种分法？

【解】

对于某条边，它只能在某一个三角形中。

$h_n=\sum_1^{n-1} h_kh_{n-k},n\ge 3$



令$G(x)=h_1x+\cdots+h_nx^n+...$

$G^2(x)=\sum \sum h_ih_jx^{i+j}=\sum_{n=2}^{\infty}(\sum_i^{n-1} h_ih_{n-i}x^n)$



$h_n=c_{n-1}$



【例二】$n$ 个数$a_1a_2...a_n$连乘，有多少种不同乘法方案？亦即括号匹配问题。

$(a_1a_2...a_k)(a_{k+1}...a_n)$

$h_n=\sum_1^{n-k} h_kh_{n-k}$


