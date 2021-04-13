# 概率论笔记

- 作者: 千森 @19-计科
- QQ:  2414711236                                                   
- 用法: 本笔记对课本重要的知识点与公式做了整理，可作为考试的复习指导，也可用作解题速查手册。

[TOC]



# 1. 随机事件与概率

## 1.1. 事件的关系与运算

方法：画韦恩图。

## 1.2. 公式

1. 加法公式：

$$
P(A\cup B)=P(A)+P(B)-P(AB)
$$

2. :sparkles: 乘法公式：

$$
P(AB)=P(B)P(A|B)
$$

3. 全概率公式：

$$
\begin{align}
P(A)&=P(B)P(A|B)+P(\overline{B})P(A|\overline{B}) \\

P(A)&=\sum_{i=1}^n P(B_i)P(A|B_i)
\end{align}
$$

4. :sparkles: 贝叶斯公式：

$$
P(B_i|A)=\frac{P(B_i)P(A|B_i)}{\sum_{j}P(B_j)P(A|B_j)}
$$

> 理解：将A视为某种结果，$B_j$为导致这个结果的若干原因。

5. 事件独立：

$$
P(AB)=P(A)P(B)
$$

> 提示：注意相关与独立的区别。



# 2. 随机变量与概率分布

## 2.1. 分布函数

1. 定义：

$$
F(x)=P(X\le x) \\

F(x,y)=P(X\le x,Y\le y)
$$

2. 性质：

- $F(x)$是单调增函数。
- $F(\infty)=1,\quad F(-\infty)=0$
- $F(-\infty,y)=F(x,-\infty)=0$
- $F(\infty,\infty)=1$

3. 计算：

离散的：

$$
\begin{align}
F(x)&=P(X\le x)=\sum_{x_k\le x}P(X=X_k)=\sum_{x_k\le x}p_k \\

F(x,y)&=\sum_{x_i\le x}\sum_{y_j\le y}p_{ij}

\end{align}
$$

连续：
$$
\begin{align}
F(x)&=\int_{-\infty}^x f(y)dy,\quad -\infty<x<\infty \\

F(x,y)&=\int_{-\infty}^x\int_{-\infty}^yf(u)f(v)dudv,\quad (x,y)\in\mathbb{R}^2

\end{align}
$$

4. 求概率：

$$
\begin{align}
P(a<X\le b)& =F(b)-F(a)=\int_a^bf(x)dx \\

P(x_1<X\le x_2,y_1<Y\le y_2)& =F(x_2,y_2)-F(x_2,y_1)-F(x_1,y_2)+F(x_1,y_1)\\

P(X\le x,y<\infty)& =F(x,\infty)=F_X(x)\quad 边缘分布

\end{align}
$$

> 练习：p125例题3.7.3

## 2.2. 分布函数的求法：

### 2.2.1. :sparkles: 一维积分转化法

设$X:f_X(x),\quad Y:f_Y(y),\quad Y=g(X)$
$$
\int_{-\infty}^\infty h[g(x)]f_X(x)dx=\int_a^b h(y)p(y)dy
$$
这里，$h(x)$不参与实质计算。
$$
f_Y(y)=
\begin{cases}
p(y) & a<y<b\\
0    & 其他
\end{cases}
$$

### 2.2.2.  :sparkles: 二维积分转化法

设$(X,Y)$的联合概率密度为$f(x,y)$, $g(x,y)$是实值函数，$Z=g(X,Y)$:
$$
\int_{-\infty}^\infty\int_{-\infty}^\infty h[g(x,y)]f(x,y)dxdy=\int_a^bh(z)p(z)dz,\quad a<b
$$
则$Z=g(X,Y)$的概率密度为：
$$
f_Z(z)=
\begin{cases}
p(z), & a<z<b\\
0, &其他
\end{cases}
$$

> 提示：用z的表达式替换一个例如y，变换积分把z放到最外面，积分区域也要相应调整。
>
> 练习：教材P119例题3.6.7

### 2.2.3. 边缘概率密度

$$
f_X(x)=\int_{-\infty}^\infty f(x,v)dv
$$

> 理解：把y积分掉。

## 2.3. 独立性

$$
\begin{align}
F(x,y)&=F_X(x)F_Y(y)\\

P(X\le x, Y\le y)&=P(X\le x)P(Y\le y)\\

p_{ij}&=p_i(X)p_j(Y)\\

f(x,y)&=f_X(x)f_Y(y)
\end{align}
$$

## 2.4. 条件分布

### 2.4.1. 定义

离散型：
$$
P(X=x_i|Y=y_i)=\frac{p_{ij}}{\sum p_j(Y)},\mbox{ where }p_j(Y)=\sum_{i}p_{ij}\\
$$
连续型：
$$
f_{X|Y}(x|y)=\frac{f(x,y)}{f_Y(y)}=\frac{f(x,y)}{\int_{-\infty}^\infty f(x,y)dx}
$$


## 2.5. 分布速查表


|               分布               |             参数             | 分布律或概率密度                                             |           期望           | 方差                       |
| :------------------------------: | :--------------------------: | :----------------------------------------------------------- | :----------------------: | -------------------------- |
|             单点分布             |             $c$              | $P(X=c)=1$                                                   |            c             | 0                          |
|             两点分布             |           $0<p<1$            | $P(X=0)=1-p; \\ P(X=1)=p$                                    |           $p$            | $p(1-p)$                   |
|             二项分布             |      $0<p<1 \\ n \ge 1$      | $P(X=k)=\binom{n}{k}p^k(1-p)^{n-k} \\ k=0, 1,\dots,n$        |           $np$           | $np(1-p)$                  |
|  泊松分布$\mathscr{P}(\lambda)$  |         $\lambda >0$         | $P(X=k)=\frac{\lambda^k}{k!}e^{-\lambda} \\ k=0,1,\dots$     |        $\lambda$         | $\lambda$                  |
| 指数分布$\varepsilon(\lambda) $  |         $\lambda >0$         | $f(x)=\lambda e^{-\lambda x},x\in(0,\infty)$                 |   $\frac{1}{\lambda}$    | $\frac{1}{\lambda^2}$      |
|         均匀分布$U[a,b]$         |           $a < b$            | $f(x)=\frac{1}{b-a}I_{[a,b]}(x)$                             |     $\frac{a+b}{2}$      | $\frac{(b-a)^2}{12}$       |
|    高斯分布$N(\mu,\sigma^2)$     | $\mu\in\mathbb{R}\\\sigma>0$ | $f(x)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x-\mu)^2}{2}}$   |          $\mu$           | $\sigma^2$                 |
| 伽马分布$\Gamma(\alpha,\lambda)$ |    $\alpha>0\\\lambda>0$     | $f(x)=\frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\lambda x}I_{(0,\infty)}(x)$ | $\frac{\alpha}{\lambda}$ | $\frac{\alpha}{\lambda^2}$ |
|         $\chi^2(n)$分布          |          $n \ge 1$           | ~                                                            |           $n$            | $2n$                       |
|            $t(n)$分布            |          $n \ge 1$           | ~                                                            |        $0,(n>1)$         | $\frac{n}{n-2},(n>2)$      |
|           $F(m,n)$分布           |          $m,n\ge1$           | ~                                                            |  $\frac{n}{n-2},(n>2)$   | ~                          |

# 3. 随机变量的数字特征

## 3.1. 期望

### 3.1.1. 定义：

$$
E(X)=
\begin{cases}

\sum_k x_kp_k \\
\\
\int_{-\infty}^{+\infty}xf(x)dx

\end{cases}
$$

### 3.1.2. 性质：

$$
E(kX)=kE(x)\\

E\left(\sum X_i\right)=\sum E(X_i)\\

E\left(\prod Xi\right)=\prod E(X_i),如果X_i相互独立
$$

### 3.1.3. 函数的期望：

$$
E(g(X))=
\begin{cases}

\sum_k g(x_k)p_k \\
\\
\int_{-\infty}^{+\infty}g(x)f(x)dx

\end{cases}
$$



## 3.2. 方差

### 3.2.1. 定义

$$
D(X)=E(X-E(X))
$$

## 3.3. 性质：

$$
\begin{align}
D(X)&=E(X^2)-(E(X))^2\\

D(kX)&=k^2D(X)\\

D\left(\sum_i X_i \right)&=\sum D(X_i),\quad 如果X_i相互独立
\end{align}
$$

## 3.4. 协方差

### 3.4.1. 定义

$$
\begin{align}
Cov(X,Y)&=E\bigg(\big(X-E(X)\big)\big(Y-E(Y)\big)\bigg)\\

\rho_{XY}&=\frac{Cov(X,Y)}{\sqrt{D(X)}\sqrt{D(Y)}}\\
 
\end{align}
$$

### 3.4.2. 计算公式

$$
\begin{align}
D(X+Y)&=D()+D(Y)+Cov(X,Y)\\

Cov(X,Y)&=E(XY)-E(X)E(Y)\\

Cov(aX,bY)&=abCov(X,Y)
\end{align}
$$

### 3.4.3. 相关性性质

$$
\begin{align}
X,Y&\ 不相关\\
Cov(X,Y)& =0 \\
E(XY)&=E(X)E(Y)\\
D(X+Y)&=D(X)+D(Y)
\end{align}
$$

> 提示：注意与独立区别开来
>
> 特例：二维正态分布独立等价于不相关。

# 4. 概率极限定理

## 4.1. 切比雪夫不等式：

$$
P(|X-E(X)|\ge \varepsilon)\le \frac{D(X)}{\varepsilon^2}
$$

## 4.2. 大数定理：

$$
\lim_{n\to\infty} P\left(\left|\frac{1}{n}\sum_{k=1}^n-\mu\right|>\varepsilon\right)=0
$$



## 4.3. 中心极限定理：

$$
\frac{\sum_iX_i-n\mu}{\sqrt{n}\sigma} \sim N(0,1),这里是近似服从
$$



### 棣莫弗-拉普拉斯定理

设$n_A$为$n$重伯努利实验中$A$出现的次数，又$A$在每次实验中发生的概率为$p$，则
$$
\frac{n_A-np}{\sqrt{np(1-p)}}\sim N(0,1)
$$
因此概率计算式为：
$$
P(a\le n_A\le b)=\varPhi(\frac{b-np}{\sqrt{np(1-p)}})-\varPhi(\frac{a-np}{\sqrt{np(1-p)}}),\mbox{ where }a\le b,n\to\infty
$$


### 4.3.1. 练习

1. 教材p194例题

2. 教材p190例题5.2.1

# 5. 数理统计

## 5.1. 一些统计量的定义

设$X_1,X_2,\dots,X_n$是来自总体$X$的样本, 且$E(X)=\mu,\ D(X)=\sigma^2$。

|       统计量名称       | 定义                                                         | 期望                  | 方差                                 |
| :--------------------: | :----------------------------------------------------------- | --------------------- | ------------------------------------ |
| 样本均值$\overline{X}$ | $\overline{X}=\frac{1}{n}\sum_{i=1}^nX_i$                    | $E(\overline{X})=\mu$ | $D(\overline{X})=\frac{\sigma^2}{n}$ |
|     样本方差$S^2$      | $S^2=\frac{1}{n-1}\sum_{i=1}^n (X_i-\overline{X})^2$         | $E(S^2)=\sigma^2$     |                                      |
|     样本标准差$S$      | $S=\sqrt{S^2}$                                               |                       |                                      |
|    样本$k$阶矩$A_k$    | $A_k=\frac{1}{n}\sum_{i=1}^n X_i^k,\ (k=1,2,\dots)$          |                       |                                      |
|  样本$k$阶中心矩$B_k$  | $B_k=\frac{1}{n}\sum_{i=1}^n (X_i-\overline{X})^k,(k=1,2,\dots)$ |                       |                                      |

## 5.2. 抽样分布的定义

| 分布名                                               | 定义                                                         | 期望                  | 方差                  |
| ---------------------------------------------------- | ------------------------------------------------------------ | --------------------- | --------------------- |
| 自由度为 $n$ 的 $\chi^2$分布 $\chi^2 \sim \chi^2(n)$ | $\chi^2=X_1^2+X_2^2+ \dots +X_n^2,\quad X_i \sim N(0,1)$     | $n$                   | $2n$                  |
| 自由度为 $n$ 的 $t$分布 $T \sim t(n)$                | $T=\frac{X}{\sqrt{Y/n}},\quad X \sim N(0,1),Y \sim \chi^2(n)$ | $0,(n>1)$             | $\frac{n}{n-2},(n>2)$ |
| 自由度为 $n_1,n_2$ 的 $F$分布 $F \sim F(n_1,n_2)$    | $F=\frac{X_1/n_1}{X_2/n_2},\quad X_1 \sim \chi^2(n_1),X_2 \sim \chi^2(n_2)$ | $\frac{n}{n-2},(n>2)$ |                       |

## 5.3. 正态总体抽样分布公式


$$
\frac{\overline{X}-\mu}{\sigma/\sqrt{n}} \sim N(0,1)
$$

$$
\frac{(n-1)S^2}{\sigma^2} =\sum_{i=1}^n \frac{(X_i-\overline{X})}{\sigma^2} \sim \chi^2(n-1)
$$

$$
\frac{\overline{X}-\mu}{S/\sqrt{n}} \sim t(n-1)
$$

$$
T=\frac{\overline{X_1}-\overline{X_2}-(\mu_1-\mu_2)}{S_w\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}}
\sim t(n_1+n_2-2)

\mbox{, Where }S_w^2=\frac{(n_1-1)S_1^2+(n_2-1)S_2^2}{n_1+n_2-2}
$$


$$
\frac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2} \sim F(n_1-1,n_2-1)
$$



# 6. 6.参数估计

## 6.1. 矩估计

第一步：计算$E(X),E(X^2)$:
$$
\begin{cases}
E(X)=\int xf(x)dx = g_1(\theta) \\
E(X^2)=\int x^2f(x)dx = g_2(\theta)
\end{cases}
$$


第二步: 列方程:
$$
\begin{cases}
g_1(\theta) = E(X) =\frac{1}{n}\sum_{i=1}^nX_i = \overline{X}\\
g_2(\theta) = E(X^2)=\frac{1}{n}\sum_{i=1}^nX_i^2

\end{cases}
$$
第三步：用$X_i$的式子表示$\hat{\theta_i}$

### 6.1.1. 知识点练习

1. 教材p219例7.1.3

## 6.2. 似然函数

似然函数的定义：
$$
L(\theta)=L(\theta;x_1,\dots,x_n)=
\begin{cases}

\prod_{i=1}^n p(x_i;\theta) & 离散型\\

\\%空行

\prod_{i=1}^n f(x_i;\theta) & 连续型型

\end{cases}
$$
最大似然法：求使得$L(\theta)$取最大值的$\theta$用做估计：$\hat{\theta}(X_1,\dots,X_n)$.

1. 观察法，最大值点看得出。
2. 导数法：

$$
\frac{\partial\ln L(\theta)}{\partial \theta_i}=0,\quad i=0,1,\dots,k
$$



### 6.2.1. 知识点练习

1. 教材p223例题

## 6.3. 参数估计速查表

<img src="常见分布参数估计.jpg" alt="常见分布参数估计"  />

## 6.4. 优良准则

1. 无偏性：$E(\hat{\theta})=\theta$

2. 有效性：$D(\hat{\theta})$越小越有效

## 6.5. 区间估计

以下是正态总体$N(\mu,\sigma^2)$的估计

| 情形                        | 枢轴量                                                    | 估计                                                         |
| --------------------------- | --------------------------------------------------------- | ------------------------------------------------------------ |
| $\sigma^2$已知时$\mu$的估计 | $\frac{\overline{X}-\mu}{\sigma/\sqrt{n}} \sim N(0,1)$    | $(\overline{X}\pm\frac{\sigma}{\sqrt{n}} z_{\alpha/2})$      |
| $\sigma^2$未知时$\mu$的估计 | $\frac{\overline{X}-\mu}{S/\sqrt{n}} \sim t(n-1)$         | $(\overline{X}\pm\frac{\sigma}{\sqrt{n}} t_{\alpha/2}(n-1))$ |
| $\mu$已知时$\sigma^2$的估计 | $\frac{\sum_{i=1}^n(X_i-\mu)^2}{\sigma^2} \sim \chi^2(n)$ | $\left( \frac{\sum_{i=1}^n(X_i-\mu)^2}{\chi^2_{\alpha/2}(n)},\frac{\sum_{i=1}^n(X_i-\mu)^2}{\chi^2_{1-\alpha/2}(n)} \right)$ |
| $\mu$未知时$\sigma^2$的估计 | $\frac{(n-1)S^2}{\sigma^2} \sim \chi^2(n-1)$              | $\left( \frac{(n-1)S^2}{\chi^2_{\alpha/2}(n-1)},\frac{(n-1)S^2}{\chi^2_{1-\alpha/2}(n-1)} \right)$ |

# 7. 假设检验

## 7.1. $\mu$的检验

### 7.1.1. $\sigma$已知：

| 原假设$H_0$   | 检验统计量                                               | 拒绝域                |
| ------------- | -------------------------------------------------------- | --------------------- |
| $\mu=\mu_0$   | $\frac{\overline{x}-\mu_0}{\sigma/\sqrt{n}} \sim N(0,1)$ | $|u|\ge z_{\alpha/2}$ |
| $\mu\le\mu_0$ | 同上                                                     | $u\ge z_{\alpha}$     |
| $\mu\ge\mu_0$ | 同上                                                     | $u\le -z_{\alpha}$    |

> **理解小技巧：**
>
> $\mu=\mu_0$说明大概在中间，因此拒绝两边。
>
> $\mu<\mu_0$说明大概率在左边，因此拒绝右边。
>
> $\mu>\mu_0$说明大概率在右边，因此拒绝左边。



![1607563900111](C:\Users\sen\Desktop\Note\数学\u检验.jpg)

### 7.1.2. $\sigma$未知：
| 原假设$H_0$   | 检验统计量                                          | 拒绝域                     |
| ------------- | --------------------------------------------------- | -------------------------- |
| $\mu=\mu_0$   | $\frac{\overline{x}-\mu_0}{S/\sqrt{n}} \sim t(n-1)$ | $|t|\ge t_{\alpha/2}(n-1)$ |
| $\mu\le\mu_0$ | 同上                                                | $t\ge t_{\alpha}(n-1)$     |
| $\mu\ge\mu_0$ | 同上                                                | $t\le -t_{\alpha}(n-1)$    |

## 7.2. $\sigma$的检验

### 7.2.1. $\mu$未知：

| 原假设$H_0$             | 检验统计量                                   | 拒绝域                                                       |
| ----------------------- | -------------------------------------------- | ------------------------------------------------------------ |
| $\sigma^2=\sigma_0^2$   | $\frac{(n-1)S^2}{\sigma^2} \sim \chi^2(n-1)$ | $\chi^2\le \chi^2_{1-\alpha/2}(n-1)\mbox{ or }\chi^2\ge \chi^2_{\alpha/2}(n-1)$ |
| $\sigma^2\le\sigma^2_0$ | 同上                                         | $\chi^2\le \chi^2_{1-\alpha}(n-1)$                           |
| $\sigma^2\ge\sigma^2_0$ | 同上                                         | $\chi^2\ge \chi^2_{\alpha}(n-1)$                             |

### 7.2.2. $\mu$已知：

| 原假设$H_0$             | 检验统计量                                                | 拒绝域                                                       |
| ----------------------- | --------------------------------------------------------- | ------------------------------------------------------------ |
| $\sigma^2=\sigma_0^2$   | $\frac{\sum_{i=1}^n(X_i-\mu)^2}{\sigma^2} \sim \chi^2(n)$ | $\chi^2\le \chi^2_{1-\alpha/2}(n)\mbox{ or }\chi^2\ge \chi^2_{\alpha/2}(n)$ |
| $\sigma^2\le\sigma^2_0$ | 同上                                                      | $\chi^2\ge \chi^2_{\alpha}(n)$                               |
| $\sigma^2\ge\sigma^2_0$ | 同上                                                      | $\chi^2\le \chi^2_{1-\alpha}(n)$                             |



![1607563818402](C:\Users\sen\Desktop\Note\数学\x方检验.jpg)

## 7.3. 其他

### 7.3.1. $\sigma$已知，$\mu_1-\mu_2$的检验：

$$
\frac{\overline{x}-\overline{y}}{\sqrt{\frac{\sigma_1^2}{n_1}+\frac{\sigma_2^2}{n_2}}} \sim N(0,1)
$$

### 7.3.2. $\sigma$未知，$\mu_1-\mu_2$的检验：

$$
T=\frac{\overline{x_1}-\overline{x_2}}{S_w\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}}
\sim t(n_1+n_2-2)

\mbox{, Where }S_w^2=\frac{(n_1-1)S_1^2+(n_2-1)S_2^2}{n_1+n_2-2}
$$

### 7.3.3. $\mu$未知$\sigma_1^2/\sigma_2^2$的检验：

$$
\frac{S_1^2}{S_2^2} \sim F(n_1-1,n_2-1)
$$

> 提示：请对比正态总体抽样分布公式

## 7.4. 总结

难点：

1. 统计量的选取。
2. 分位数的计算与查找，数字看得真晕。
3. 检验过程的理解。
4. 样本统计量的计算，要是给出均值方差还好，不然自己算很花时间