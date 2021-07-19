# Welcome Back

<p align="center">
 <img  width="300" height="300" src="assets/download.jpeg">
 <p align="center">
 <i>It's learning time!!</i><br> 
</p>

Let's dig a little deeper into the controls and dynamics together this week. We begin our journey with the world of **Linear Systems.**

## Linear Systems
A system (say a robot or anything that you want to control) whose dynamics can be represented as a differential equation of the form 

<p align="center">
<img  width="200" height="100" src="assets/linear.png">
 <p align="center">
 <i>The equation defines how system is changing with repect to the current state of the system.</i><br> 
</p>

is called a **Linear System.**

Here, A is a square matrix (of dimension nxn) that represents the dynamics of the system and X is a vector of dimension (nx1) which represents the state of a system.

The state consists of the variables that are used to define the current state of affairs of the system. 

For example, In a robot the state may include it's velocity and position. Then the matrix A will form the dynamics of the robot defining the relation between the derivatives of the position and velocity to actual position and velocity.

## Forming the Linear Equation

The simplest example of a linear system is a spring mass system like this - 

<p align="center">
<img  width="400" height="200" src="assets/spring_mass.png">
 <p align="center">
 <i>Simple spring mass system</i><br> 
</p>

You can easily solve it using newton's laws of motion but we prefer to solve this through langrange equations as these equations come in handy with complicated systems. We hope you didn't miss your physics classes, but even if you did, lagrange equations are pretty simple. Here is a video link to brief you upto that. This also contains the solution to the given problem.

<p align="center">
<img  width="400" height="300" src="assets/meme1.jpg">
 <p align="center">
 <i>Here comes the physics!!</i><br> 
</p>

[![Langrangian Mechanics](https://img.youtube.com/vi/KpLno70oYHE/0.jpg)](https://youtu.be/KpLno70oYHE)

Now, from the video you can infer that we can write the dynamics equation for the given system in the form of

<p align="center">
<img  width="70" height="40" src="assets/mass_eq.png">
 <p align="center"> 
</p>

Now, we can write this equation in term of matrices and vectors. The equation can be written as - 

<p align="center">
<img  width="400" height="200" src="assets/lin_eqn.png">
 <p align="center">
 <i>Linear Equation for spring mass system</i><br> 
</p>

Here, x and x(dot) are the variables that define the state of the system at ay given time step.


## Linearizing a non-linear system

Well, most systems are pretty complex and it is not possible to represent them in a linear form. So, usually we have tricks to approximate a non-linear system to a linear system about a particular point. 

**Non-linear systems** have a non-linear relation between the current state and the change of state. The differential equation representing a non-linear equation can be written as - 

<p align="center">
<img  width="200" height="" src="assets/non_lin.png">
 <p align="center">
 <i>Here, f(x) is a non linear function.</i><br> 
</p>

Non-linear systems are hard to control and hence it helps if we can approximate them as linear systems and develop control schemes for them.

There are only some fixed states in the system about which you can linearize your non-linear system. These states are called fixed states and these can be found by the equation

<p align="center">
<img  width="200" height="150" src="assets/fixPt.png">
 <p align="center">
 <i></i><br> 
</p>

In case you are bored, just remember in the end all this physics/maths will be worth it.

<p align="center">
<img  width="" height="" src="assets/meme2.jpeg">
 <p align="center">
 <i>Keep Going!!</i><br> 
</p>

Now, to linearize about the fixed state, first we need to find the jacobian matrix of f(x). Now, jacobian is a first order differential matrix which is a very important tool in robotics. We currently cannot go in depth of what jacobian is, but this is how you calculate it for a given differential equation - 

So the above equation, when written in a matrix form, assuming there are two state variables x1 and x2 would be represented as - 

<p align="center">
<img  width="300" height="180" src="assets/non_linM.png">
 <p align="center">
 <i></i><br> 
</p>

The jacobian for this will be given as - 

<p align="center">
<img  width="300" height="180" src="assets/jacob.png">
 <p align="center">
 <i></i><br> 
</p>

Then, finally to linearise a system about a fixed point, we put in the **fixed state** variables in the jacobian to get A matrix

<p align="center">
<img  width="300" height="180" src="assets/a_mat.png">
 <p align="center">
 <i></i><br> 
</p>

Now, we can write our non-linear system as an approximated linear system about the state x(bar) represented by the equation - 

<p align="center">
<img  width="200" height="100" src="assets/linear.png">
 <p align="center">
 <i></i><br> 
</p>

Hence, we have successfully linearized a non-linear system about a fixed state. 

**Note- This linearization is valid only when the state of the system remains close to the fixed state. If the system diverges away from the fixed point, approximation will become invalid and the system will collapse.**


Mastering Eigen Values and Eigen Vectors -

To proceed further we need some idea about eigen values and eigen vectors. So read this article about eigen values and eigen vectors - 

[Eigen values and Eigen vectors](https://www.mathsisfun.com/algebra/eigenvalue.html)


<p align="center">
<img  width="" height="" src="assets/meme3.gif">
 <p align="center">
 <i>Congratulations on completing SubPart - 1</i><br> 
</p>

# Game Time

<p align="center">
<img  width="" height="" src="assets/meme4.gif">
 <p align="center">
 <i>Guess who's back? back again.</i><br> 
</p>  

Now, we'll apply all that we have learnt on a simple inverted pendulum. It's time for Did You Get Control?

[Did You Get Control? - Part 3](https://forms.gle/1kCRmMr2SBnp4Pkw7)

