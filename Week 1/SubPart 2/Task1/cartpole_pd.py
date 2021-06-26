'''

Task 1 -


The cartpole problem is a very important problem in the classical control. 
A pendulum is attached to a cart and we can apply force on the cart either along +x or -x
We try to keep the pole vertical.

A PD controller has been implemented to keep the pole at vertical.
You can adjust the PD gain throught the track-bars which will appear when you run the code.

Experiment with the PD gains and observe what effect they have on the pole and cart's motion and can you relate them with what you have learnt so far.

Find the ideal PD gains to keep the pole vertical with stability.

The code is not necessary to go through. Some elements like GYM and masks have been used which are not beneficial in current scope, so ignore them. You can look at the other lines.

'''

import numpy as np
import gym
import cv2
import time

'''
sigmoid function is used to map the values betwwen 0 and 1
here it is used so that the control input is smooth and erratic 
since cartpole ideally takes input between -1 and +1
'''

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


def callback():             #Dummy function for the track-bars
    pass

env = gym.make('CartPole-v1')               #Loading the cartpole problem in the simulation
desired_state = np.array([0, 0, 0, 0])      #desired state is to keep the pole upright and velocities 0 (Linear and angular both)
desired_mask = np.array([0, 0, 1, 0])       #Used in calculation

#P-D gains to be adjusted
cv2.namedWindow('controls')                        #Making track-bars to track the PD gains in realtime
cv2.createTrackbar('P', 'controls', 0, 500, callback)
cv2.createTrackbar('D', 'controls', 0, 500, callback)
P=cv2.getTrackbarPos('P', 'controls')
D=cv2.getTrackbarPos('D', 'controls')

k=cv2.waitKey(1) & 0xFF      #This here activates the track-bars                    
#P, D = 0.1, 0.5
t=0

#Select the track-bar window and Press ESCAPE to execute


while(True):
    k=cv2.waitKey(1) & 0xFF             #This gives a value of 27 to k as soon as ESCAPE key is pressed
    if k == 27:                         #If ESCAPE is pressed, the simulation starts
        state = env.reset()             #We reset the simulation                  
        derivative = 0                  #Reseting all the gains
        prev_error = 0
        t = 0                           #Reseting the time
        while(True):
            P=cv2.getTrackbarPos('P', 'controls')/100    #Getting the P from the trak-bars, P is divided by 100 to convert the range from 0-500(integers) to 0-5(floats) as that is the desired range
            D=cv2.getTrackbarPos('D', 'controls')/100    #Getting the D from the trak-bars, D is divided by 100 to convert the range from 0-500(integers) to 0-5(floats) as that is the desired range

            '''
            Divinding factors are determined experimentally, we let track-bars have values from 0-500 
            and divide the value we get from them to get adjust them to the required range
            For example, if track-bar is at 100, but I should be around 0.01, so we divide by 10000 to get the final value in desired range.
            This is done as track-bars only support integer values
            '''
        
            k=cv2.waitKey(1) & 0xFF  #This detects if ESCAPE key is pressed as well as is necessary to update the track-bars in real time
            t+=0.01               #Tracking the time.
            env.render()          #Showing the simulation, stepping it further
            error = state - desired_state           #The error is the difference between the current state and desired state
            derivative = error - prev_error         #The D term is the difference in current error and prev error, As the simulation is called at regular intervals, we don't divide by time. It gives us the rate at which the error is changing.
            prev_error = error              #Updating prev_error to use in next loop

            pd = np.dot(P * error + D * derivative, desired_mask)   #Calculating the action
            action = sigmoid(pd)                                #Smotthening it with sigmoid function
            action = np.round(action).astype(np.int32)          #Rounding off to an integer

            state, reward, done, info = env.step(action)        #Sending the action, that is force to be applied along +x or -x
            time.sleep(0.01)
            if(k==27):                              #Reseting the simulation in case ESCAPE key is pressed.
                print("Episode finished after {} timesteps".format(t+1))
                state = env.reset()
                env.render()
                break

env.close()