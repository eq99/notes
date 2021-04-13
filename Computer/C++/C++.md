# C++ 学习笔记



# 开发环境搭建

- 安装编译器：

```sh
$ sudo apt install build-essential
$ g++ --version
```

- VScode 调试

<img src="./VScode Debuger.png" alt="VScode Debuger" style="zoom:50%;" />

安装官方c/c++插件，然后创建 `lanunch.json`就好了。

- 安装包管理器:

```sh
# https://docs.conan.io/en/latest/installation.html
$ pip install conan
```





# 类



## 构造函数与析构函数



[构造函数](http://c.biancheng.net/view/1401.html)





[什么时候调用析构函数？](https://www.cnblogs.com/AntonioSu/p/12269474.html)

析构函数是在对象消亡时，自动被调用，用来释放对象占用的空间。

有四种方式会调用析构函数：

1.**生命周期**：对象**生命周期结束**，会调用析构函数。

2.**delete**：调用delete，会删除指针类对象。

3.**包含关系**：对象Dog是对象Person的成员，Person的析构函数被调用时，对象Dog的析构函数也被调用。

4.**继承关系**：当Person是Student的父类，调用Student的析构函数，会调用Person的析构函数。









## 犯过的错误

- 声明构造函数加了 `void`
- class 与 struct 后面没加 `;`



