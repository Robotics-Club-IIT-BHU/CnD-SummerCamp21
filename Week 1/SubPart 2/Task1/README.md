## Task 1

# [CartPole-v1](https://gym.openai.com/envs/CartPole-v1/)

A pole is attached by an un-actuated joint to a cart, which moves along a friction less track. The system is controlled by applying a force of +1 or -1 to the cart. The pendulum starts upright, and the goal is to prevent it from falling over. A reward of +1 is provided for every timestep that the pole remains upright. The episode ends when the pole is more than 15 degrees from vertical, or the cart moves more than 2.4 units from the centre.

This control can be implemented with only PD parts of the equation as there cannot occur a steady state error. Hence, here we only use a PD controller. We will learn more about the steady state errors and I part of the equation in the next task.

<p align="center">
 <img  width="400" height="400" src="https://takashi-matsushita.github.io/jekyll/assets/img/posts/CartPole.gif">
 <p align="center">
 <i>cartpole</i><br> 
</p>


A PD controller has been implemented to keep the pole at vertical.
You can adjust the PD gain throught the track-bars which will appear when you run the code.

# Challanges for Task 1

1. Experiment with the PD gains and observe what effect they have on the pole and cart's motion and can you relate them with what you have learnt so far.
2. Find the ideal PD gains to keep the pole vertical with stability.

The code is not necessary to go through. Some elements like GYM and masks have been used which are not beneficial in current scope, so ignore them. You can look at the other lines.


# INSTRUCTIONS -

1. Download this folder, along with the python code and src.
2. Execute the python code.
3. Press Escape key after selecting the track-bar window in order to start the simulation.
4. Press Escape again to reset it and run it again.


# Game Time

<p align="center">
 <img  width="400" height="250" src="https://media.makeameme.org/created/its-game-time-8510ddeeb0.jpg">
 <p align="center">
 <i>Wohoo!!!</i><br> 
</p>

Once You complete the above Task, Here is a game we would like you to play. 
We call this - *Did You Get The Control?*

Here You'll be asked a few interesting questions based on the task you just did.
The goal here is not to win, but to build an intuition about the stuff and learning new things.
All the best!!!

Note: This is non-evaluative and is just meant for strengthening your knowledge.

Here is the link to the part 1. All the Best

[Did You Get The Control? - Part 1](https://forms.gle/HiqN1sfw1TyaDugs5)
