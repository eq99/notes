到现在为止你已经学习会了如何使用 Python 变量，如何使用 Python 做数学运算，如何用 Python 处理字符串，如何使用 Python 中的函数，如何使用 Python 的循环与条件语句。接下来我们进入基础教程的最后一个重要主题：Python 中的列表和字典。



# 列表 List

【主题一】什么是列表？

直接定义列表有些困难，可以通过观察例子对列表建立感性的认识。

```python
numbers = [1,2,3,4]
pets = ['二哈','猫咪','仓老鼠']
adcs = ['鲁班七号', '虞姬', '伽罗', '后羿']
empty = []
```

从上面的例子说明列表是由`[]`括起来的一组对象，对象之间用`,`隔开。

 【主题二】如何创建列表？

1. 枚举列表中的元素：

```python
computer_basics = ['数学','编程设计','计算机组成原理','算法与数据结构','操作系统','计算机网络','编译原理','数据库']

print(computer_basics)
```



2. 通过像空列表中添加元素:

```python
even_numbers = []
for k in range(0,5):
  even_numbers.append(2*k)

print(even_numbers)
# [0, 2, 4, 6, 8]
```



【主题三】如何访问列表中的元素？

1. 通过下标访问

```python
program_languages = ['Python', 'C++', 'java', 'golang', 'javascript', 'SQL', 'Rust']

print(f'学习 {program_languages[0]} 的人超帅!')
```

2. 通过`for...in...`访问

```python
players = ['贝利','马拉多纳','C罗','梅西']

for player in players:
  print(player)
```

【主题四】如何获取列表中部分元素？

通过切片的方式，切片的模式为`[i:j:k]`，其中`i`为起始下标，如果省略，则为0；`j`为结束下标，如果省略，最为最后一个元素；`k`为步长，如果省略，则为1。

如果`i,j`为负数，代表从最后一个元素向前数。

```python
pi = [3,1,4,1,5,9,2,6]

y1 = pi[1:3]
print(y1)
# [1,4]

y2 = pi[1:8:2]
print(y2)
# [1, 1, 9, 6]

y3 = pi[1:]
print(y3)
# [1,4,1,5,9,2,6]

y4 = pi[1:-2]
print(y4)
# [1, 4, 1, 5, 9]

y5 = pi[-2:-1]
print(y5)
# [2]
```

**注意**：`[i,j]`表示的区间是左闭右开 $[i,j)$



【主题五】如何合并两个列表？

```python
evens = [0,2,4,8,10]
odds = [1,3,5,7,9]
numbers = [*evens, *odds]
print(numbers)
# [0, 2, 4, 8, 10, 1, 3, 5, 7, 9]
```



# 字典

【主题一】什么是字典？

先看两个字典的例子：

```python
user = {
  'name': 'Looke', 
  'birthday': '2021-07-02',
  'hobby': '打豆豆'
}

print(user)

computer = {
  'cpu': 'R5 5600X 散片',
  '主板': '微星B550M迫击炮',
  '显卡': 'RTX 3070TI 星耀',
  '内存': '英睿达3200Hz 8G*2',
  '硬盘': '西数sn750 1T',
  '电源': '安钛克HCG750',
  '机箱': 'DF700Flux'
}

print(computer)
```

从上面的例子可以看出字典是用`{}`括起来的键值对 (key-value)。键值对之间用`,`分隔。同时可以看出字典可以清楚的描述对象的属性。

【主题二】如何建立字典？

1. 通过前一个例子那样的枚举法。
2. 向空字典中添加条目：

```python
menu = {}
menu['广东烧鹅'] = '￥99.8'

print(menu)
# {'广东烧鹅': '￥99.8'}
```

如果你想用`append()`，不好意思`AttributeError: 'dict' object has no attribute 'append'`。

【主题三】如何访问字典中的元素？

1. 通过键 (key) 访问值(value)

```python
computer = {
  'cpu': 'R5 5600X 散片',
  '主板': '微星B550M迫击炮',
  '显卡': 'RTX 3070TI 星耀',
  '内存': '英睿达3200Hz 8G*2',
  '硬盘': '西数sn750 1T',
  '电源': '安钛克HCG750',
  '机箱': 'DF700Flux'
}

print(computer['显卡'])
# RTX 3070TI 星耀
```

如果访问不存在的键：

```python
computer = {
  'cpu': 'R5 5600X 散片',
  '主板': '微星B550M迫击炮',
  '显卡': 'RTX 3070TI 星耀',
  '内存': '英睿达3200Hz 8G*2',
  '硬盘': '西数sn750 1T',
  '电源': '安钛克HCG750',
  '机箱': 'DF700Flux'
}

print(computer['散热'])
# Traceback (most recent call last):
#   File "script.py", line 11, in 
#     print(computer['散热'])
# KeyError: '散热'
```

2. 通过`get()`方法

```python
computer = {
  'cpu': 'R5 5600X 散片',
  '主板': '微星B550M迫击炮',
  '显卡': 'RTX 3070TI 星耀',
  '内存': '英睿达3200Hz 8G*2',
  '硬盘': '西数sn750 1T',
  '电源': '安钛克HCG750',
  '机箱': 'DF700Flux'
}

print(computer.get('显卡'))
print(computer.get('散热'))
# RTX 3070TI 星耀
# None
```

你发现这两种方法的区别了吗？

3. 通过`for...in...` 方法

```python
computer = {
  'cpu': 'R5 5600X 散片',
  '主板': '微星B550M迫击炮',
  '显卡': 'RTX 3070TI 星耀',
  '内存': '英睿达3200Hz 8G*2',
  '硬盘': '西数sn750 1T',
  '电源': '安钛克HCG750',
  '机箱': 'DF700Flux'
}

for item in computer:
  print(item, computer[item])
  
# cpu R5 5600X 散片
# 主板 微星B550M迫击炮
# 显卡 RTX 3070TI 星耀
# 内存 英睿达3200Hz 8G*2
# 硬盘 西数sn750 1T
# 电源 安钛克HCG750
# 机箱 DF700Flux
```

另外一种访问键值对的方法：

```python
computer = {
  'cpu': 'R5 5600X 散片',
  '主板': '微星B550M迫击炮',
  '显卡': 'RTX 3070TI 星耀',
  '内存': '英睿达3200Hz 8G*2',
  '硬盘': '西数sn750 1T',
  '电源': '安钛克HCG750',
  '机箱': 'DF700Flux'
}

for key, value in computer.items():
  print(key, value)
  
# cpu R5 5600X 散片
# 主板 微星B550M迫击炮
# 显卡 RTX 3070TI 星耀
# 内存 英睿达3200Hz 8G*2
# 硬盘 西数sn750 1T
# 电源 安钛克HCG750
# 机箱 DF700Flux
```

【主题四】合并两个字典。

```python
database = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'postgres',
    'USER': 'postgres',
    'PASSWORD': '123456',
    'HOST': 'localhost',
    'PORT': '5432'
}

redis = {
    "BACKEND": "django_redis.cache.RedisCache",
    "LOCATION": "redis://127.0.0.1:6379/1",
}

config = {**database, **redis}

print(config)
# {'ENGINE': 'django.db.backends.postgresql', 'NAME': 'postgres', 'USER': 'postgres', 'PASSWORD': '123456', 'HOST': 'localhost', 'PORT': '5432', 'BACKEND': 'django_redis.cache.RedisCache', 'LOCATION': 'redis://127.0.0.1:6379/1'}

```



# 总结

列表与字典是 Python 最常见的两种容器对象。除了上述基本的用法之外还有其他用法，更多用法可以参考官网 [数据结构](https://docs.python.org/zh-cn/3/tutorial/datastructures.html)一章。

值得注意的是列表与字典的值可以不仅仅是数字，字符串这样的对象，还可以是列表，字典，函数等。

