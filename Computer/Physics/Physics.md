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



波动方程：

$y(x,t)=A\cos(2\pi(\frac{t}{T}-\frac{x}{\lambda})+\varphi)$

$y(x,t)=A\cos(\omega(t-\frac{x}{u})+\varphi)$





# 刚体运动

转动惯量：$I=\sum m_ir_i^2 = \int r^2dm$

力矩：$\vec{M}=\vec{r}\times \vec{F}=I\vec{\alpha}$

角动量：$L=I\omega$

转动动能：$E_k=\frac{1}{2}I\omega^2$



常见几何体转动惯量：



平行轴定理：若有任一轴与过质心的轴平行，且该轴与过质心的轴相距为 $d$, 则 $I=I_c+md^2$。

垂直轴定理：$I_Z=I_X+I_Y$。



# 静电场

定义式：$\vec{E}=\frac{\vec{F}}{q_0}$

点电荷：$\vec{E}=\frac{q}{4\pi\varepsilon_0 r^2}\vec{e_r}$，矢量叠加，利用对称性，元电荷积分。

$\frac{1}{4\pi\varepsilon_0}=9\times 10^9Nm^2C^{-2} $

电通量：$\varPhi_e=\int \vec{E}\cdot d\vec{S}$

高斯定理：$\oint \vec{E}\cdot d\vec{S} = \frac{\sum q_i}{\varepsilon_0}$



电势：$U_{ab}=V_a-V_b=\int_a^b \vec{E}\cdot d\vec{l}$

叠加法：$V=\sum V_i$



# 恒定磁场

电流密度：$\boldsymbol{j}=\frac{dI}{dS_0}\boldsymbol{e_n}$

电流连续方程：$\oint_S \boldsymbol{j}\cdot d\boldsymbol{S}=-\frac{dQ}{dt}$

电阻定律：$R=\rho \frac{l}{S}$

微分形式欧姆定律：$\boldsymbol{j}=\sigma \boldsymbol{E}$

$dB=\frac{\mu_0}{4\pi}\cdot\frac{dl\sin\theta}{r^2}$ 单位：$1T=1N\cdot A^{-1}\cdot m^{-1}$

$\mu_0=4\pi\times10^{-7} N\cdot A^{-2}$

无限长直导线周围磁场：$B=\frac{\mu_0 I}{2\pi a}$



磁通量：$\varPhi=\int_s \boldsymbol{B}\cdot d\boldsymbol{S}$

安培环路定里：$\oint_L \boldsymbol{B}\cdot d\boldsymbol{l}=\mu_0\sum I_i$



安培力：$d\boldsymbol{F}=Id\boldsymbol{l}\times\boldsymbol{B}$

洛伦兹力：$\boldsymbol{F}=q\boldsymbol{v}\times\boldsymbol{B}$

磁力矩：$\boldsymbol{M}=NSI\boldsymbol{e_n}\times \boldsymbol{B}$



# 电磁感应

楞次定律：闭合回路中感应电流激发的磁场总是阻碍磁通量的变化。

感生电动势：$\varepsilon=-\frac{d\Phi}{dt}$

动生电动势：$d\varepsilon=(\boldsymbol{v}\times\boldsymbol{B})\cdot d\boldsymbol{l}$，或：$E=BLv$



# 光干涉

光强：$I\propto E^2$, $E$是电场强度矢量。

相干光：振动方向相同，振动频率相同，相位差恒定



【杨氏双缝干涉】

明条纹：$\frac{d}{D}x=\pm k\lambda,k=0,1,2,...$

暗条纹：$\frac{d}{D}x=\pm (2k+1)\frac{\lambda}{2},k=0,1,2,...$

【薄膜干涉】

光程差：$\delta_0=2e\sqrt{n_2^2-n_1^2\sin^2i}$

考虑反射光的半波损失：$\delta_0+\delta^{\prime}$， 即光疏介质到光密介质的反射有：$\delta^{\prime}=\frac{\lambda}{2}$，否则 $\delta^{\prime}=$0。



# 光的衍射

单缝夫琅禾费衍射暗条纹：$a\sin(\theta)=\pm k\lambda,k=1,2,3,...$

明条纹：$a\sin(\theta)=\pm (2k+1)\frac{\lambda}{2},k=1,2,3,...$

并且 $\sin(\theta)\approx\theta$



光栅方程：$d\sin(\theta)=\pm k\lambda,k=0,1,2...$，明条纹。

缺级现象：同时满足：$d\sin(\theta)=\pm k\lambda, a\sin(\theta)=\pm k^{\prime}\lambda, k=\frac{d}{a}k^{\prime},k^{\prime}=1,2,3...$



# 偏振光

偏振度：$P=\frac{I_{max}-I_{min}}{I_{max}+I_{min}}$

自然光通过偏振片：$I=\frac{1}{2}I_s$

马吕斯定律：$I=I_0\cos^2(\alpha)$

布儒斯特定律：$\tan(i_b)=\frac{n_2}{n_1}$

![布儒斯特定律](布儒斯特定律.jpg)



# 光电效应

光电方程：$\frac{1}{2}mv_m^2=h\nu-A$

波粒二象性：
$$
\varepsilon=h\nu \\
p=\frac{h}{\lambda}
$$


# 康普顿效应

波长偏移公式：$\Delta \lambda=\lambda_C(1-\cos(\theta))$，其中 $\lambda_C=\frac{h}{m_0c}=2.43\times 10^{-3}nm$



# 氢原子



能量：$h\nu=E_n-E_m$，其中 $E_n=\frac{E_1}{n^2}, E_1=-13.6eV$



