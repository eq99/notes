为了更好的理解 Python， 这次我们选择了一个稍微复杂一点的问题。



# 估算圆周率

下面给出估计圆周率的一种算法：随机的取两个质数，他们互质的概率等于 $6/\pi^2$。因此，假设随机取了 $n$ 对整数，找出了其中共有 $m$ 对整数互质，那么：
$$
\begin{align}
\frac{m}{n}&=\frac{6}{\pi^2} \\
\pi&=\sqrt{6n/m}
\end{align}
$$


```python
import math
import random

def is_coprime(x,y):
  return math.gcd(x,y) == 1

def estimate_pi(n):
  m = 0
  for i in range(0,n):
    x = random.randint(0,1000)
    y = random.randint(0,1000)
    if is_coprime(x,y):
      m = m + 1
  return math.sqrt(6*n/m)

pi = estimate_pi(1000_000)
print(pi)
```

接下来如何理解这段代码呢？

1. 先看倒数的两行：通过**调用函数**`esttmate_pi(1000_000)` 估算了圆周率并显示。

2. 再看`def estimate_pi(n)`：这里我们自定义了一个函数也就是估算圆周率的**函数**，它接受一个**参数** `n`，也就是随机的 $n$ 对整数。

3. 再看`for i in range(0,n):` 定义了一个**循环**，每次循环取两个随机的整数 $x,y$，然后通过**条件语句**`if is_coprime(x,y):`判断这两个数是否互质，如果互质就把 $m$ 加一。
4. 再看`return math.sqrt(6*n/m)`：**返回**算式 $\sqrt{6n/m}$ 的值，是一个小数，或说浮点数。

5. 再看`def is_coprime(x,y):`这是第3步中用来判断是否是质数的函数，它返回`True`或`False`。
6. 最后看`import random`和`import math`：这是引入外部**模块**，这些模块包含了许多已经写好的函数，拿来即用，不用自己写。
7. 你可能已经发现了，Python 定义函数，循环，条件判断不需要`{}`，但请注意程序的**缩进**，同一个层次代码的缩进层次要一致。如果你的程序出现类似

```python
File "<string>", line 13
    m = m + 1
    ^
IndentationError: expected an indented block
```

这样的错误的时候，请检查缩进格式。

# 总结

通过这段代码的学习，你已经学会了如何写 Python 程序。包括怎么定义函数，怎么返回函数值，怎么调用函数，怎么写循环，怎么写条件语句，怎么引入外部模块。

Python 代码利用**缩进**组织代码的结构层次，这是 Python 的一个特色。

到这里你已经能够写出许多代码了。接下来我们将学习更多 Python 的代码结构。

