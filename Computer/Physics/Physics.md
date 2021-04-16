# 大学物理公式速查





# 运动学

## 曲线运动

位置：$\vec{r}=x\vec{i}+y\vec{j}+z\vec{k}, |r|=\sqrt{x^2+y^2+z^2}$

速度：$\vec{v}=\frac{d\vec{r}}{dt}=\frac{dx}{dt}\vec{i}+\frac{dy}{dt}\vec{i}+\frac{dz}{dt}\vec{i}$

速度大小：$v=|\vec{v}|=\frac{ds}{dt}=\sqrt{v_x^2+v_y^2+v_z^2}$

自然坐标系：$\vec{v}=\frac{ds}{dt}\vec{e_\tau}$



位移：$\Delta \vec{r} = \vec{r_2}-\vec{r_1}$

加速度：$\vec{a}=\frac{d\vec{v}}{dt}$

大小：$a= \sqrt{a_\tau^2+a_n^2}=\sqrt{a_x^2+a_y^2+a_z^2}$

自然坐标表示：$\vec{a}=a_\tau\vec{e_\tau}+a_n\vec{e_n}=\frac{dv}{dt}\vec{e_\tau}+\frac{v^2}{\rho}\vec{e_n}$



## 圆周运动

角速度：$\omega =\frac{d\theta}{dt}$

角加速度：$\alpha=\frac{d\omega}{dt}=\frac{d^2\theta}{dt}$

与线量的关系：

$ds=Rd\theta$

$v=R\omega$

$a_\tau=R\alpha$

$a_n=R\omega^2$





# 牛顿力学

牛一：惯性定律。

牛二：$\vec{F}=m\vec{a}=m\frac{d\vec{v}}{dt}$

直角坐标系分量式：

$F_x=ma_x=m\frac{dx}{dt}$

$F_y=ma_y=m\frac{dy}{dt}$

$F_z=ma_z=m\frac{dz}{dt}$

自然坐标系分量式：

$F_\tau=ma_\tau=m\frac{dv}{dt}$

$F_n=m\frac{v^2}{\rho}$



重力：$\vec{F}=m\vec{g}$

万有引力：$\vec{F}=-G\frac{m_1m_2}{r^2}\vec{e_r}$

弹簧：$\vec{F}=-kx\vec{i}$

摩擦力：$F=\mu F_N$



# 功与能



做功：$A=\int \vec{F}\cdot d\vec{r}$，使用分解或投影有利于计算。

动能定律：$A=\frac{1}{2}mv^2-\frac{1}{2}mv_0^2$

重力势能：$E_p=mgh$

弹性势能：$E_p=\frac{1}{2}kx^2$

引力势能：$E_p=-G\frac{m_1m_2}{r}$



冲量：$\vec{I}=\int \vec{F}dt$

动量：$\vec{p}=m\vec{v}$

动量定理：$\vec{I}=m\vec{v_2}-m\vec{v_1}$



# 机械振动

力学特征：$F=-kx$

运动学方程：$x=A\cos(\omega t+\varphi)$

能量特征：$E=\frac{1}{2}mv^2+\frac{1}{2}kx^2$

关系：$T= \frac{1}{\nu}=\frac{2\pi}{\omega}$



合成：

$A=\sqrt{A_1^2+A_2^2+2A_1A_2\cos(\varphi_2-\varphi_1)}$

$\tan\varphi=\frac{A_1\sin\varphi_1+A_2\sin\varphi_2}{A_1\cos\varphi_1+A_2\cos\varphi_2}$



# 刚体运动

转动惯量：$I=\sum m_ir_i^2 = \int r^2dm$

力矩：$\vec{M}=\vec{r}\times \vec{F}=I\vec{\alpha}$

角动量：$L=I\omega$

转动动能：$E_k=\frac{1}{2}I\omega^2$



# 静电场

定义式：$\vec{E}=\frac{\vec{F}}{q_0}$

点电荷：$\vec{E}=\frac{q}{4\pi\varepsilon_0 r^2}\vec{e_r}$，矢量叠加，利用对称性，元电荷积分。

电通量：$\varPhi_e=\int \vec{E}\cdot d\vec{S}$

高斯定理：$\oint \vec{E}\cdot d\vec{S} = \frac{\sum q_i}{\varepsilon_0}$



电势：$U_{ab}=V_a-V_b=\int_a^b \vec{E}\cdot d\vec{l}$

叠加法：$V=\sum V_i$



