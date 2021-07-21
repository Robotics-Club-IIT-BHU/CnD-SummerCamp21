'''A simple example script, which implements an LQR controller for a double integrator.
'''

from __future__ import print_function, division

import controlpy
import scipy
import numpy as np

# Example system is a double integrator:
A = np.array([[ 0.      ,    1.        ]
 ,[19.76914034 , 0.        ]])
B = np.array([[0.        ]
 ,[0.28817989]])


# Define our costs:
Q = np.array([[ 10,   0],[  0, 1000]])
R = [[0.0001]]

# Compute the LQR controller
gain, X, closedLoopEigVals = controlpy.synthesis.controller_lqr(A,B,Q,R)
print('The computed gain is:')
print(gain)

print('The closed loop eigenvalues are:')
print(closedLoopEigVals)


