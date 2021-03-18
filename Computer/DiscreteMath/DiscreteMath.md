# 逻辑推理

## 命题

命题：能判断真假的陈述句。

简单命题或原子命题：不能分为更简单的句子。用小写字母 $p, q, r$ 表示。简单命题的真值是确定的，由称命题常项。

命题变项或命题变元： $x+1>5$ 不是命题，当 $x$ 的值确定后才能判断真假。也用小写字母 $p, q, r$ 表示。

复合命题：由简单命题用逻辑连接词连接而称的命题。

连接词如下：

| 名称       | 符号              | 举例                  | 含义                     |
| ---------- | ----------------- | --------------------- | ------------------------ |
| 否定连接词 | $\neg$            | $\neg p$              | 非 $p$                   |
| 合取连接词 | $\and$            | $p \and q$            | $p$ 且  $q$，合取式      |
| 析取连接词 | $\or$             | $p \or q$             | $p$ 或 $q$， 析取式      |
| 蕴含连接词 | $\rightarrow$     | $p \rightarrow q$     | 若 $p$ 则 $q$， 蕴含式   |
| 等价连接词 | $\leftrightarrow$ | $p \leftrightarrow q$ | $p$ 当且仅当 $q$，等价式 |
| 与非联结词 | $\uparrow$        | $p \uparrow q$        | $\neg (p \and q)$        |
| 或非联结词 | $\downarrow$      | $p \downarrow q$      | $\neg (p \or q)$         |

命题符号化步骤：

1. 把命题中的简单命题拎出来，用小写英文字母表示。
2. 用逻辑词把简单命题连接起来。

**例题**

​	小李只能选一个梨或苹果。

​	$p$：小李拿一个梨

​	$q$：小李拿一个苹果

​	---> $(p \and \neg q) \or (\neg p \and q)$

注意这里的或为排斥或。



## 公式

命题公式或公式：由命题常项与命题变项用连接词连接起来的式子。

赋值或解释：设 $A$ 由命题变项 $p_1,p_1,\dots,p_n$ 组成，为 $p_1,p_1,\dots,p_n$ 指定一组真值叫赋值。有 $n$ 个命题变项的公式有 $2^n$ 种赋值。

真值表：列出公式所有赋值方法的表。

永真式或重言式：公式 $A$ 在所有的赋值方法下均为真。

永假式或矛盾式：公式 $A$ 在所有的赋值方法下均为假。

可满足式：公式 $A$ 至少有一种赋值方法为真。永真式是可满足式，反之不成立。

$n$ 元真值函数：$F:\{0,1\}^n \rightarrow \{0,1\}$

**等值**：设 $A,B$ 是两个命题公式，若等价式 $A \rightarrow B$ 是重言式，则称 $A $与 $B$ 是等值的，记做 $A \Leftrightarrow B$。

常见的等值公式列表：

| 公式                                                         | 说明     |
| :----------------------------------------------------------- | -------- |
| $\neg \neg A \Leftrightarrow A$                              | 双重否定 |
| $ A \or A \Leftrightarrow A$                                 |          |
| $ A \and A \Leftrightarrow A$                                |          |
| $ A \or B \Leftrightarrow B \or A$                           |          |
| $ A \and B \Leftrightarrow B \and A$                         |          |
| $(A \or B)\or C \Leftrightarrow A \or (B \or C)$             |          |
| $(A \and B)\and C \Leftrightarrow A \and (B \and C)$         |          |
| $A \or (B\and C \and D) \Leftrightarrow (A \or B) \and (A \or C) \and (A \or D)$ |          |
| $A \and (B\or C) \Leftrightarrow (A \and B) \or (A \and C)$  |          |
| $\neg (A \or B) \Leftrightarrow \neg A \and \neg B$          |          |
| $\neg (A \and B) \Leftrightarrow \neg A \or \neg B$          |          |
| $A \or (A\and C) \Leftrightarrow A $                         |          |
| $A \and (A\or C) \Leftrightarrow A $                         |          |
| $A \or 1 \Leftrightarrow 1$                                  |          |
| $A \and 0 \Leftrightarrow 0$                                 |          |
| $A \or 0 \Leftrightarrow A$                                  |          |
| $A \and 1 \Leftrightarrow A$                                 |          |
| $A \or \neg A \Leftrightarrow 1$                             |          |
| $A \and \neg A \Leftrightarrow 0$                            |          |
| $A \rightarrow B \Leftrightarrow \neg A \or B$               |          |
| $A \leftrightarrow B \Leftrightarrow (A \rightarrow B) \and (B \rightarrow A)$ |          |
| $A \rightarrow B \Leftrightarrow \neg B \rightarrow \neg A$  |          |
| $A \leftrightarrow B \Leftrightarrow \neg A \leftrightarrow \neg B$ |          |
| $(A \rightarrow B)\and(A \rightarrow \neg B) \Leftrightarrow \neg A$ |          |

等值置换：若 $A \Leftrightarrow B$ ，则 $\varPhi(A) \Leftrightarrow \varPhi(B)$



## 范式

简单析取式：由有限个命题变项或其否定构成的析取式。

简单合取式：由有限个命题变项或其否定构成的合取式。

析取范式：由有限个简单合取式构成的析取式。

合取范式：由有限个简单析取式构成的合取式。



两个性质：

一个析取范式是矛盾式，当且仅当它的每个简单合取式是矛盾式。

一个合取范式是重言式，当且仅当它的每个简单析取式是重言式。



范式存在定理：

任何一个公式都存在一个与之等值的析取范式与合取范式。但是不唯一。



极小项与极大项：

设有 $n$ 个命题变项，若在简单合取式中每个命题变项与其否定有且仅有一个出现一次，这样的简单合取式称为极小项。 $n$ 个命题变项可形成  $2^n$ 个极小项。

设有 $n$ 个命题变项，若在简单析取式中每个命题变项与其否定有且仅有一个出现一次，这样的简单析取式称为极大项。 $n$ 个命题变项可形成  $2^n$ 个极大项。

标记方法：把命题变项按字典序排列，如 $a, c, \neg e, p, \neg q, r, x_1, x_2$；对应二进制位为：$11010111$，有 $\neg $ 的用0表示，没有的用1表示；对应十进制描述：$m_{215}$，其实就是二进制模式对应的十进制数。



主析取范式：如果公式 $A$ 的析取范式的简单合取式全是极小项。任何公式都有唯一的主析取范式。

主合取范式：如果公式 $A$ 的合取范式的简单析取式全是极大项。任何公式都有唯一的主合取范式。



求主析取范式方法1：

1. 先求 $A$ 析取范式 $A^{\prime}$
2. 若$A^{\prime}$ 的某简单合取式不含某个命题变项 $p$ 或 $\neg p$ , 则:

$$
B\Leftrightarrow B\and 1 \Leftrightarrow B\and (p \or \neg p) \Leftrightarrow (B\and p)\or( B \and \neg p)
$$

3. 把变成极小项的简单合取式用写成 $m_i$ 的形式。
4. 将 $m_i$ 合并，然后从小到大排列。



主析取范式与主合取范式的应用：

1. 判断两个公式是否等值
2. 判断公式的类型：重言式，矛盾式，可满足式？
3. 真与假赋值方法

:memo: 思考题：

- 永假式的主析取范式与主合取范式是什么？

- $p \and q$ 的主析取范式与主合取范式是什么？



## 全功能集

全功能集：设 $S$ 是一个联结词的集合，如果任一真值函数都可用仅含 $S$ 中的联结词的命题公式表示，则称 $S$ 为全功能集。

:star:**定理**：$\{\neg,\and, \or \}$， $\{\neg, \and\}$，$\{\neg, \or\}$，$\{\neg, \rightarrow\}$ ，$\{\uparrow\}$，$\{\downarrow\}$ 都是全功能集。

证明方法：

由于任何公式可以表示成主析取范式，第一个成立。

由于 $p\or q \Leftrightarrow \neg \neg (p \or q) \Leftrightarrow \neg (\neg p \and\neg q )$，可见 $\or$ 可以由 $\neg, \and$ 替换。

其实任何包含全功能集的联结词集合式全功能集。



最简展开式：对主析取范式进行简化，使其包含最少的运算。

:sparkles: 最简展开式求解方法：卡诺图法。



## 推理

若 $(A_1 \and A_2\and\dots\and A_n ) \rightarrow B$ 为重言式，则称  $A_1 \and A_2\and\dots\and A_n$ 推出结论 $B$ 的推理正确，$B$ 称为 $A_1 \and A_2\and\dots\and A_n$ 的有效结论或逻辑结论。



与用 $A \Leftrightarrow B$ 表示 $A \leftrightarrow B$ 是重言式类似，用 $A \Rightarrow B$ 表示 $A \rightarrow B$ 是重言式。

:bulb:推理正确不能保证结论正确。

推理定律：

| 定律                                                         | 描述       |
| ------------------------------------------------------------ | ---------- |
| $A \Rightarrow (A\or B)$                                     | 附加       |
| $(A\and B) \Rightarrow A$                                    | 化简       |
| $(A\rightarrow B) \and A \Rightarrow B$                      | 假言推理   |
| $(A\rightarrow B) \and \neg B \Rightarrow \neg A$            | 拒取式     |
| $(A\or B) \and \neg A \Rightarrow B$                         | 析取三段论 |
| $(A\rightarrow B) \and (B\rightarrow C)\Rightarrow (A\rightarrow C)$ | 假言三段论 |
| $(A\leftrightarrow B) \and (A\leftrightarrow C)\Rightarrow (A\leftrightarrow C)$ | 等价三段论 |
| $(A\rightarrow B) \and (C\rightarrow D) \and (A \or C)\Rightarrow (B\or D)$ | 构造性两难 |

构造证明两种技巧：

1. 附加前提证明法，把结论变成前提：

$$
(A_1\and A_2\and \dots\and A_n)\rightarrow (A\rightarrow B) \Leftrightarrow (A_1\and A_2\and \dots\and A_n \and A)\rightarrow B
$$

其实：$\neg A_n \or (\neg A \or B)\Leftrightarrow \neg A_n \or \neg A \or B$

2. 归谬法：

$$
(A_1\and A_2\and \dots\and A_n \and A)\rightarrow (B) \Leftrightarrow \neg (A_1\and A_2\and \dots\and A_n \and A \and \neg B)
$$

只要 $A_1\and A_2\and \dots\and A_n \and A \and \neg B$ 是矛盾式，就能说明推理正确。





# 一阶逻辑

一阶逻辑也称谓词逻辑。

## 基本概念

个体常项：表示具体的和特定的个体的词，常用小写的英文字 $a,b,c,\dots$母表示。

个体变项：表示抽象的，或泛指的个体，常用小写的英文字 $x,y,z,\dots$母表示。

个体域，论域：个体变相的取值范围。当无特殊说明时，个体域只宇宙所有事物，称为全总个体域。

谓词常项：表示具体性质或关系的谓词，一般用大写英文字母 $F,G,H,\dots$ 表示。

谓词变项：表示抽象或泛指的谓词。

$F(x)$： 表示个体变项 $x$ 具有性质 $F$ 。

$L(x,y)$： 表示个体变项 $x,y$ 具有关系 $L$ 。

有时也把以上两种个体变项与谓词的联合体称作谓词。

 $n$ 元谓词：含 $n$ 个个体词的谓词称为 $n$ 元谓词，用 $P(x_1,x_2,\dots,x_n)$ 表示，它是以个体变项的个体域为定义域，以 $\{0,1\}$ 为值域的函数，它不是命题。

0元谓词：不带个体变项的谓词，0元谓词常项都是命题。

量词：除了个体词和谓词，还需要表示数量的词。量词用全称量词和存在量词两种。

**全称量词**：一切，所有，用 $\forall$ 表示，$\forall x$ 表示个体域中所有的个体，$\forall x F(x)$ 表示个体域中的所有个体都具有性质 $F$。

**存在量词**：有一个，存在，用 $\exist$ 表示，$\exist x$ 表示存在个体域中的个体，$\exist x F(x)$ 表示个体域中存在有个体具有性质 $F$。

:bulb:注意所讨论的个体域，可引入特性谓词。



**谓词公式转化为命题公式**

设个体域为有限集 $D={a_1,a_2,\dots,a_n}$，则
$$
\forall xA(x) \Leftrightarrow A(a_1)\and A(a_2)\and\dots\and A(a_n)\\
\exist xA(x) \Leftrightarrow A(a_1)\or A(a_2)\or\dots\or A(a_n)
$$
:warning: 量词顺序不能随便颠倒。

例如：设 $D$ 为实数集，$H:x+y=5$

那么 $\forall x \exist yH(x,y)$ 与 $\forall x \exist yH(x,y)$ 表达的含义不同，前者为真而后者为假。



## 一阶谓词逻辑公式及解释

字母表定义如下：

- 个体常项：$a,b,c,\dots,a_i,b_i,c_i\dots$
- 个体变项：$x,y,z,\dots,x_i,y_i,z_i,\dots$
- 函数符号：$f,g,h,\dots,f_i,g_i,h_i,\dots$
- 谓词符号：$F,G,H,\dots,F_i,G_i,H_i\dots$
- 量词符号：$\forall,\exist$
- 联结词符：$\neg,\and,\or,\rightarrow,\leftrightarrow$
- 括号和逗号：$(),$



项的递归定义：

1. 个体常项和个体变项是项

2. 若 $\phi(x_1,x_2,\dots,x_n)$ 是任意n元函数，$t_1,t_2,\dots,t_n$ 是项，则 $\phi(t_1,t_2,\dots,t_n)$ 也是项

3. 只有限次使用以上两个规则生成的符号串才是项。



原子公式：

设 $\R(x_1,x_2,\dots,x_n)$ 是任意n元谓词，$t_1,t_2,\dots,t_n$ 是项，则 $\R(t_1,t_2,\dots,t_n)$ 称为原子公式。



合式公式：

1. 原子公式是合式公式
2. 若 $A$ 是合式公式，$\neg A$ 也是合式公式。
3. 若 $A,B$ 是合式公式， 则 $A\and B,A\or B, A\rightarrow B, A\leftrightarrow B$也是合式公式。
4. 若 $A$ 是合式公式，则 $\forall xA, \exist x A$ 也是合式公式。
5. 有限次利用以上规则构成的符号串才是合式公式。

合式公式又称谓词公式，简称公式。



在合式公式 $\forall xA, \exist x A$ 中，称 $x$ 为指导变项，$A$ 为相应量词的辖域。在辖域中，$x$ 的所有出现称为约束出现，A中不是约束出现的变项称为自由出现。







#  集合论



# 代数结构



# 图论





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



