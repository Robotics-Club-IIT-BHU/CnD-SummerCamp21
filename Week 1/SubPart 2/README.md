## Subpart 2

# Understanding Proportional Integral Derivative (PID) Controller

**NOTE:** Make sure you have covered the Control Systems document of subpart 1 before proceeding further.

## Introduction

- **Proportional-integral-derivative** (PID) controllers are **widely used** in industrial systems despite the significant developments of recent years in control theory and technology. 

<p align="center">
 <img  width="600" height="300" src="https://scontent.fdel1-1.fna.fbcdn.net/v/t1.6435-9/s960x960/116803440_2419316341707160_1898308850773093529_n.png?_nc_cat=110&ccb=1-3&_nc_sid=730e14&_nc_ohc=DvRbtAlYNk4AX9BtV70&_nc_ht=scontent.fdel1-1.fna&tp=30&oh=b2975b1af2f92ab0f75ab2bea6166400&oe=60D9CC71">
 <p align="center">
 <i>PID rules the control universe</i><br> 
</p>

- PID is an example of a **closed loop system**.
- They **perform well** for a wide class of processes. 
- Also, they give **robust performance** for a wide range of operating conditions and, they are easy to implement using analogue or digital hardware.
- PID is perhaps the most important,popular and simplistic **feed back controller**,out there.The significance of which could be done justice only by the videos below and *not even us !!*
- Refer this video by **Aerospace Controls Laboratory of Massachusetts Institute of Technology (MIT)**.

[![Control-And-Dynamics](https://img.youtube.com/vi/4Y7zG48uHRo/0.jpg)](https://www.youtube.com/watch?v=4Y7zG48uHRo)

- A brief introduction of PID by  Brian Douglas
- [![Control-And-Dynamics](https://img.youtube.com/vi/UR0hOmjaHp0/0.jpg)](https://www.youtube.com/watch?v=UR0hOmjaHp0)

> **NOTE:** 
>
> - Try watching the videos again to understand as much as possible. It has a lot of important information.
> - After you think you have some background about PID start reading below. 

To put things in perspective, we will have to go through some definitions.

------

## Variations of PID controllers

### 1. Proportional Controller aka P Controller

- Proportional controller is mostly used **in first order processes** with single energy storage **to stabilize the unstable process**. 

- The main usage of the P controller is to **decrease the steady state error** of the system. 

- As the **proportional gain factor K** increases, the **steady state error** of the system **decreases**. 

- However, despite the reduction, **P control can never** manage to **eliminate** the **steady state error** of the system. 

- As we **increase the proportional gain**, it provides **smaller amplitude** and **phase margin**, **faster dynamics** satisfying wider frequency band and **larger sensitivity** to the noise. 

- We can **use** this controller **only** when our **system is tolerable** to a **constant steady state error**. 

- In addition, it can be easily concluded that applying **P controller decreases** the **rise time**.

- Moreover, **after** certain value of **reduction on the steady state error**, **increasing K** only **leads to overshoot** of the system response. 

- P control also **causes oscillation if sufficiently aggressive** in the presence of lags and/or dead time.

  > **Assignment**: Learn about dead time in control systems.

- The more lags (higher order), the more problem it leads. Plus, it directly **amplifies process noise**.

- A P controller consists of only a linear gain Kp. The output of such controller can be simply given as

- 
  
  ```bash
  output = Kp * error
  ```

### 2. Proportional-Derivative Controller aka PD Controller

- A controller which **changes the input** of the controller to **proportional plus derivative of error signal** is called **PD** controller.
- It is used to **damp the oscillations** that arise because of increasing the proportional constant.

- 
  
  ```bash
  output = (Kp * error) + (Kd * ((error - previous error)/Δt))  
  
  where, Δt is a small duration of time
  ```

### 3.  Proportional-Integral-Derivative Controller aka PID Controller

- A controller which **changes the input** of the controller to **proportional plus derivative of error signal plus the integral of the error** is called **PID** controller.
- It is used to **remove the steady state error** which might arise in PD controller.

```bash
sum err = sum err + error
output = (Kp * error) + (Kd * ((error - previous error)/Δt)) + (Ki * sum err * Δt)
```



More mathematically PID is represented as

# output =    [![img](https://camo.githubusercontent.com/e6a30bc3ca5bb6ddd88d3bc365f72a657c737decb4c3b4cd756e39d5770bee19/68747470733a2f2f656e637279707465642d74626e302e677374617469632e636f6d2f696d616765733f713d74626e253341414e64394763526d524475415a39336a376657663032464476754658704e416c6a4f59364f5a774b646d7a754c6d322d6f657270384c356726757371703d434155)](https://camo.githubusercontent.com/e6a30bc3ca5bb6ddd88d3bc365f72a657c737decb4c3b4cd756e39d5770bee19/68747470733a2f2f656e637279707465642d74626e302e677374617469632e636f6d2f696d616765733f713d74626e253341414e64394763526d524475415a39336a376657663032464476754658704e416c6a4f59364f5a774b646d7a754c6d322d6f657270384c356726757371703d434155)

-  Wanna C PID,..here it's in action..
   1. [Single motor target tracking](https://www.youtube.com/watch?v=fusr9eTceEo).
   2. [Self-balancing PID-ball tracker](https://www.youtube.com/watch?v=57DbEEBF7sE)

## References

1. The series of videos by **MATLAB** will help to grasp the concept of PID in the best way possible. You can watch the entire playlist from [here](https://www.youtube.com/playlist?list=PLn8PRpmsu08pQBgjxYFXSsODEF3Jqmm-y).

2. This document by **National Programme on Technology Enhanced Learning** will help you get some great insights about PID. You can download it from [here](https://nptel.ac.in/content/storage2/courses/108105063/pdf/L-12(SS)%20(IA&C)%20((EE)NPTEL).pdf).
3. You can read more about pid in the **blog by brettbeauregard** [here](http://brettbeauregard.com/blog/2011/04/improving-the-beginners-pid-introduction/).
