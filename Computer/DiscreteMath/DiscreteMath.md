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
| $A \or (B\and C) \Leftrightarrow (A \or B) \and (A \or C)$   |          |
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



