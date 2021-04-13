# 操作系统



# 进程与线程



前驱图

一个又向无环图，用于描述程序，代码段或语句的先后执行顺序。





## 进程的定义与描述

进程的本质是一个结构体，称为 PCB，主要包括如下几个方面：

- 进程标识符。
- 进程当前状态。
- 进程队列指针。
- 程序合数据地址。
- 进程优先级。
- CPU 现场保护。
- 通信信息。
- 家族关系。
- 资源清单。

Linux 进程结构体部分如：

```c
struct task_struct{
    /* -1 unrunnable, 0 runnable, >0 stopped: */
	volatile long			state;
	/*
	 * This begins the randomizable portion of task_struct. Only
	 * scheduling-critical items should be added above here.
	 */
	randomized_struct_fields_start

	void				*stack;
	atomic_t			usage;
	/* Per task flags (PF_*), defined further below: */
	unsigned int			flags;
	unsigned int			ptrace;
	int				on_rq;
	int				prio;
	int				static_prio;
	int				normal_prio;
	unsigned int			rt_priority;

	const struct sched_class	*sched_class;
	struct sched_entity		se;
	struct sched_rt_entity		rt;
	struct sched_dl_entity		dl;

	unsigned int			policy;
	int				nr_cpus_allowed;
	cpumask_t			cpus_allowed;
	struct sched_info		sched_info;
	struct list_head		tasks;
	struct mm_struct		*mm;
	struct mm_struct		*active_mm;
}
```



结构体的组成如下图所示：

![task_struct](./task_struct.jpg)



进程的状态转换图：



![process_status](./process_status.png)


## 进程的生命周期

进程的创建：









## 进程的组织



### 线程  



# 进程同步与通信

 ## 同步与互斥的基本概念

临界资源：一次仅允许一个进程使用的资源。打印机，变量，代码段都可以是临界资源。

临界区：进程中访问临界资源的那段代码。

进入区：为了进入临界区使用临界资源，在进入区检查是否可以进入临界区。

临界区：访问临界资源。

退出区：清除“正在访问临界区”标志。

剩余区：其他代码段。



为了合理使用临界资源，应满足如下条件：

空闲让进：没有进程位于临界区时，可以允许一个进程进入临界区；

忙则等待：当已有进程进入临界区时，其他试图进入临界区的进程必须等待；

有限等待：对要访问临界区资源的进程来说，应该在有限的等待时间内进入自己的临界区。

让权等待：当进程不能进入临界区时，可以释放 CPU。



进程同步：多个相互合作的进程在一些关键点上需要相互等待或交换信息。“同步”不是“齐头并进”的意思，而是定义了一种先后关系，有时序的含义。

进程互斥：当一个进程占有资源时，不允许其他进程访问，只有当此进程释放资源时，其他进程允许访问。



**互斥算法**

下面的互斥算法不一定是正确的。

1. 交替算法：

```c++
int turn =0;

P0:{
    do {
        while(turn != 0);
        // P0 的临界区
        turn = 1;
        // P0 的其他代码
    }while(1)
}

P1:{
    do {
        while(turn != 1);
        // P1 的临界区
        turn = 0;
        // P1 的其他代码
    }while(1)
}
```

本算法满足忙则等待的条件，但不满足空闲让进的条件，因为 P1 不执行，P0 也无法执行。



2. 设置一个标志数组用来表示当前进程是否在临界区中运行，初值为假。当一个进程试图进入临界区时，先检查其他进程的标志，若没有一个为真，则设置自己的标志为真，并进入临界区，退出时设置标志为假。

问题：如果两个进程几乎同时检查对方的标志时，发现标志均为假，结果同时进入了临界区，违背“忙则等待”的原则。

3. 设置一个标志数组用来表示当前进程希望在临界区中运行，初值为假。当一个进程希望进入临界区时，先设置自己的标志为真，再检查其他进程的标志，若其他进程的标志有一个为真，则等待；否则进入临界区，退出时设置标志为假。

问题：若果两个进程都希望进入临界区，检查对方标志时均为真，由于相互谦让，他们有可能都无法进入临界区。

4. 方案一和三的结合体。

:bulb: 以上算法之所以出现问题，是因为临界资源状态的检查与修改没有作为一个整体来实现。​



硬件方法：

1. 禁止中断
2. 硬件指令方法



【锁机制】

```c
lock(w){
    while(w == 1){
        w=1;
    }
}

unlock(w){
    w = 0;
}


// P1,P2
//...
lock(w);
//临界区;
unlock(w);
//...
```



## 信号量

问题：设有 $M$ 个互斥的资源，有N 个同步的进程，每个进程每次占有 k 个资源，求信号量的取值范围？

信号号量s由两个成员 `count,queue` 构成，`count` 表示系统中某类资源的使用情况，初始值为一个非负数，当它大于0时，表示当前系统中可用的资源数目，当它的值小于0时，表示因请求该资源而阻塞的进程数量。`queue`用于记录阻塞的进程，初值为空队列。

信号量的值仅能P操作（也称wait 操作）和V操作（也称signal操作）修改。



```c
struct Semaphore{
    int count;
    Queue queue;
}

wait(Semaphore s){
    s.count--;
    if(s.count<0){
        //阻塞该进程
        //将其加入s.queue
    }
}

signal(Semaphore s){
    s.count++;
    if(s.count<=0){
        //从s.queue取出一个进程
        //将其加入就绪队列
    }
}
```



```c

Semaphore s = Semaphore(1);

cobegin
    P1();
	P2();
coend
    
P1(){
    //...
    P(s);
    //临界区
    V(s);
    //...
}
P2(){
    //...
    P(s);
    //临界区
    V(s);
    //...
}
```



 经典进程同步问题

【生产者-消费者问题】

生产者与消费者进程共享一个长度为n的有界缓冲区。缓冲区满时，生产者被阻塞；缓冲区空时，消费者被阻塞；生产者与消费者只能有一个操作缓冲区。实现的伪代码如下：

```c
semaphore full = 0;
semaphore empty = n;
semaphore mutex = 1;

producer(){
    while(1){
        produce();
        P(empty);
        P(mutex);
        //把数据放到缓冲区
        V(mutex);
        V(full);
    }
}

customer(){
    while(1){
        produce();
        P(full);
        P(mutex);
        //从缓冲区取出数据
        V(mutex);
        V(empty);
    }
}
```



【读者写者问题】

如果进程只对共享资源进行读操作，那么没有问题，但如果有进程对共享资源进行写操作，就会破坏数据的完整性。为了同步读写操作，需要对资源加锁，伪代码如下：

```c
semaphore rmutex =1;
semaphore wmutex =1;
int count = 0;

reader(){
    while(true){
        P(rmutex);
        if (count==0)P(wmutex);
        count++;
        V(rmutex);
        // read()
        P(rmutex);
        count--;
        if (count==0)V(wmutex);
        V(rmutex);
    }
}

writer(){
    while(true){
        P(wmutex);
		// write()
        V(wmutex);
    }
}

main(){
    //cobegin
    reader()
    writer()
    //coend
}
```



## 管程

管程定义了一个数据结构和能为并发进程所执行的的一组操作，这组操作能同步进程和操作管程中的数据。





## 进程通信

信号与管道是Unix系统最古老的通信机制，为了增强进程间通信能力，Unix System V 提出了共享内存，信号量，消息队列的通信机制。在计算算网络中，使用套接字实现不同主机进程间通信。



1. 管道
2. FIFO
3. 消息队列
4. 信号量
5. 共享内存
6. 套接字











# 调度与死锁







# 存储管理

# 虚拟存储

# 设备管理

# 文件管理
