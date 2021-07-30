# Model Predictive Control (MPC)
**Note- This section is to just give you an intuition of MPC. Our aim is to introduce you to state of art controllers. You are encouraged to explore these domains by yourself. If you feel intimidated or feel like its too tough to understand, its completely fine. You are not dumb, We took way long to undertsand it too :p**

*The key here is not to give up.*

So far we have talked about linear systems but sadly our environment is complicated and linear systems are hard to find. Most complex robots will have non-linear dynamics. So we need a robust controller that can handle systems with non-linear dynamics. Here lands in the MPC, the state-of-the-art controller which can be employed to control almost any system.

<p align="center">
<img width="300" height = "" src="assets\meme1.jpg">
 <p align="center">
 <i>MPC - The holy grail of Control Theory</i><br>
</p>

Contrary to popular belief due to its high usage and popularity in industry, MPC does not stand for Most Popular Control, rather it stands for **Model Predicitve Control**. You might ask why is it so popular and widely used ? Well the answer is simple, it can see the future.

<p align="center">
<img width="500" height = "250" src="assets\Doctor-Strange.jpg">
 <p align="center">
 <i>MPC can literally predict the future</i><br>
</p>

## MPC Pipeline

<p align="center">
<img width="650" height = "200" src="assets\mpc pipeline.png">
 <p align="center">
 <i></i><br>
</p>

Here **plant** stands for the system (linear or non linear), that needs to be controlled.
**Refrences** are what the states of the plant should be ideally i.e. the states that the controller is trying to reach.
As you can see the MPC controller takes in the references and the current state of the plant to generate the new control action. 

## Inside the MPC

<p align="center">
<img width="650" height = "300" src="assets\insidempc.png">
 <p align="center">
 <i></i><br>
</p>

Inside the MPC are the system equations of the plant called the **plant model**. Basically what the MPC does is, it simulates the plant model upto a certain point in future based on the input states of the plant and gives the best possible control law. Then the first step of the control law is executed and the whole process starts again.
The main optimization problem for a MPC is as follows. 

<p align="center">
<img width="530" height = "222" src="assets\optimization problem.png">
 <p align="center">
 <i></i><br>
</p>

## The Power of MPC

<p align="center">
<img width="494" height = "281" src="assets\powerofgod.png">
 <p align="center">
 <i>freshers after understanding MPC:</i><br>
</p>

The most common example relevant to this camp for MPC would be, you guessed it right, **an inverted pendulum on a cart**. But in week 1 you were able to control it *easily* using a PD controller, then why do we need a MPC here? Simply because by using an MPC we can easily make the pendulum upright (theta=180) from its stable equilibrium position(theta=0), something which cannot be achieved by other controllers that you have studied.

This is primarily beacuase you can't make the cart move fast enough to make the pendulum upright in the first go. You need to oscillate the cart in order to build up some kinetic energy and then transfer it to the potential energy. Also, the dynamics of the pendulum are not linear all through it's trajectory.

<p align="center">
<img width="550" height = "320" src="assets\anim_cartpole.gif">
 <p align="center">
 <i></i><br>
</p>

Bored of the simple inverted pendulum on a cart? Well, MPC can handle a lot more complicated things. One simple example is Dual inverted pendulum with obstacle avoidance. It can be executed like this - 

<p align="center">
<img width="550" height = "320" src="assets\dual_pend.gif">
 <p align="center">
 <i>Dual inverted pendulum, it's not as easy as it looks</i><br>
</p>

To give you a hint about how complicated the above problem is, here are the dynamic equations for a dual inverted pendulum - 

<p align="center">
<img width="400" height = "" src="assets\dual_eqn.png">
 <p align="center">
 <i>Dual inverted pendulum - The Dynamics</i><br>
</p>

Need some motivation? Here is a fantastic example on how MPC works on real life robots - 

First, even this amazing dancing robots use some kind of MPC modelling for control - 

* [![Mini Cheetah](https://img.youtube.com/vi/fn3KWM1kuAw/0.jpg)](https://youtu.be/fn3KWM1kuAw)

Here are some more awesome examples!!

* [![Mini Cheetah](https://img.youtube.com/vi/6JlVol3eyNI/0.jpg)](https://youtu.be/6JlVol3eyNI)

* [![Biped](https://img.youtube.com/vi/xzCn1nQiVPI/0.jpg)](https://youtu.be/xzCn1nQiVPI)

* [![Quadcopter](https://img.youtube.com/vi/dL_ZFSvLXlU/0.jpg)](https://youtu.be/dL_ZFSvLXlU)

* [![Manipulator](https://img.youtube.com/vi/mFNgbS3L3Ug/0.jpg)](https://youtu.be/mFNgbS3L3Ug)


Learning about MPC will make working on real robots a lot more ecxciting for you as once you know MPC, it opens up a vast amount of possibilities that you can achieve with it. We hope we have convinced you to start learning MPC right now. Well, All the best to you.

You can contact the mentors for more resources and information whenever you want.

<p align="center">
<img width="400" height = "" src="assets\meme3.gif">
 <p align="center">
 <i>And off we go now, Stay tuned for more</i><br>
</p>



## Recommended watchlist
1. [MPC playlist by MATLAB](https://youtube.com/playlist?list=PLn8PRpmsu08ozoeoXgxPSBKLyd4YEHww8)
2. [Model Predictive Control by Steve Brunton](https://youtu.be/YwodGM2eoy4)

## Additional Links if you are feeling adventurous
1. [If you want to play with MPC in python we suggest this library.](https://www.do-mpc.com/en/latest/)
2. [Convex optimization](https://youtube.com/playlist?list=PLqwozWPBo-FuPu4d9pFOobsCF1vDGdY_I)
3. [An exhaustive course on Control Theory including MPC](https://www.youtube.com/playlist?list=PLyqSpQzTE6M91gU9WE5AOMhAkCf6HGbey)

