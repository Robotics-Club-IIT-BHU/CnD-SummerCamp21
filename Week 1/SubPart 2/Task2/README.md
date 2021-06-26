## Task 2

# Altitude of a QuadRotor

The mass of the quadrotor introduces a steady state error while trying to gain a certain altitude. Only PD control becomes useless here as it cannot counter the steady state error. To counter the steady state error, we introduce an integral error into the equation and get the PID controller.

<p align="center">
 <img  width="400" height="400" src="https://i.pinimg.com/originals/d2/9b/5b/d29b5bec682f9f0e608fd63c999609a2.gif">
 <p align="center">
 <i>quadroto</i><br> 
</p>

This problem aims to experimentally show you the importance of the Integral term for removing the steady state error.

Here is a reference video to build intuition for this task - 
* [Intiutive way to learn PID control](https://www.youtube.com/watch?v=wkfEZmsQqiA)

The video very well explains the steady state error and why it can occur in case of a drone. Try to focus on the steady state error and why Integral gain is necessary to counter it.

A PID controller has been implemented to adjust the altitude of the drone.
You can adjust the PID gain throught the track-bars which will appear when you run the code.

# Challanges for Task 2

1. Experiment with the PID gains and observe what effect they have on the drone's motion and can you relate them with what you have learnt so far.
2. Find the ideal PID gains such that the drone reaches the height of 3 meters without much fluctuation and as fast/stably as possible.
3. Observe why it is almost impossible to control the drone perfectly with using an additional integrating term.
4. The code is not necessary to go through, but understanding the code will benefit while doing the Task 3 and further weeks. That's why the code has been well-commented.


# INSTRUCTIONS -

1. Download this folder, along with the python code and src.
2. Execute the python code.
3. Press ENTER key after selecting the simulation window in order to start the simulation.
4. Press ENTER key again to reset it and run it again.


# Game Time

<p align="center">
 <img  width="300" height="300" src="https://media.tenor.com/images/be5f2535ea4977d3c652603aa63af49c/tenor.gif">
 <p align="center">
 <i>Welcome back to the party!!!</i><br> 
</p>

We are here with another round of
*Did you get the control?*

Here You'll be asked a few interesting questions based on the task you just did.
The goal here is not to win, but to build an intuition about the stuff and learning new things.
All the best!!!

Note: This is non-evaluative and is just meant for strengthening your knowledge.

Here is the link to the part 2. All the Best

[Did You Get The Control? - Part 2](https://forms.gle/c7hHHMQuF4BzJ3Li8)
