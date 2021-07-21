# Why  LQR if we already have PID? 

The application of industrial robots has greatly increased in recent  years making production systems more and more efficient. With this in  mind, increasingly efficient controllers are needed for those robots. 

<p align="center">
<img  width="" height="" src="https://user-images.githubusercontent.com/56964828/126338592-12198b94-8ab3-4935-a49a-062eda016648.png">
 <p align="center">
 <i></i><br>
</p>

The LQR control technique represents a intermediate control solution between the simple techniques, such as PID, and more complex ones, such as predictive control, when it comes to design and equation .

Whereas sometimes, LQR controllers are robust and produce a very low steady state error, but with a big transition delay and using multiple feedback gains, that makes them a bad choice when the system needs fast parameters update and has no direct access to all states of the plant. On the other hand, a PID controller gives a faster response but not with robust gains as the previous controller. [[1]](https://fei.edu.br/~psantos/PID2737725.pdf)

So the best controller depends on the problem and which one might perform well is something that one gains by experience .


<p align="center">
<img  width="" height="" src="https://user-images.githubusercontent.com/56964828/126339069-5a8d4ada-bd69-4a7b-bef6-8c3043feead7.png">
 <p align="center">
 <i></i><br>
</p>


# All roads lead to inverted pendulum .

#### Pendulums are Everywhere

![Real -world application of an inverted pendulum - the Segway](https://www.quanser.com/wp-content/uploads/2019/09/Segway-200x300.jpg)

*The inverted pendulum DOES represent many real-world systems*. Examples include the Segway, the human posture systems, the launching  of a rocket, and so on. Basically, any system that requires vertical  stabilization has dynamics that are similar to an inverted pendulum.  Sure, the dynamics in these real-world systems are more complex, but  they are related. The work involved in modeling and controlling an  inverted pendulum carries over to many engineering areas. [[2]](https://www.quanser.com/blog/why-is-the-pendulum-so-popular/)

Also the maths is easy .

# Challenge of the Week

## Goals for the challenge

1. Implement a LQR based controller to balancing the self balancing bot  using Torque Control.
2. Develop a LQR controller to make the bot stay upright.
3. Calibrate the Gains to get the best performance and minimum turbulence.
4. Infer from the exercise how different error coefficients affect the performance and stability.

# 

# INSTRUCTIONS 

1. Download this folder.
2. The code in folder "exercise" has to  be edited.
3. You have two controller options although submission for only LQR will be taken.
4. You are free to make any changes you like based on your algo.
5. "test_lqr.py" and "test_urdf" are just for you to get familiar with the function used and the environment.
6. **Hint** - Consider the self balancing bot as a inverted pendulum on a pole (cartpole) problem.
7. Refer to **CartPole_help** subfolder in order to get some help in calculating the A and B matrices for the problem. 

# You did it

<p align="center">
<img  width="300" height="" src="https://user-images.githubusercontent.com/56964828/126336991-0385ea7d-fead-46e6-9b04-da756da30c24.png">
 <p align="center">
 <i></i><br>
</p>


Once you have completed the challenge, we want you to submit the updated "SelfBalance_withLQR.py" file on the link given below.

[Weekly Challenge 2 - Submission](https://docs.google.com/forms/d/e/1FAIpQLSc0jwEoPoOjBOpDa16rTE8ZwNaHI4cGr4ITpnLxSISYBk6wEw/viewform?usp=sf_link)





