import numpy

from .engine import *

# All angles are in degrees
# All multidimensional variables are numpy arrays

def quatFromAxAng (axis, angle):
    tail = axis * sin (angle)
    return numpy.array ((cos (angle), tail [0], tail [1], tail [2]))
    
def axAngFromQuat (q):
    angle = acos (q [0])
    axis = q [1:] / sin (angle)
    
def quatMul (q0, q1):
    return numpy.array ((
        q0 [0] * q1 [0] - q0 [1] * q1 [1] - q0 [2] * q1 [2] - q0 [3] * q1 [3],
        q0 [0] * q1 [1] + q0 [1] * q1 [0] + q0 [2] * q1 [3] - q0 [3] * q1 [2],
        q0 [0] * q1 [2] - q0 [1] * q1 [3] + q0 [2] * q1 [0] + q0 [3] * q1 [1],
        q0 [0] * q1 [3] + q0 [1] * q1 [2] - q0 [2] * q1 [1] + q0 [3] * q1 [0]       
    ))
        
def quatInv (q):
    return numpy.array ((q [0], -q [1], -q [2], -q [3]))
    
def quatVecRot (q, v):
    return quatMul (
        quatMul (
            q,
            (0, v [0], v [1], v [2])
        ),
        quatInv (q)
    ) / 2
    
def quatMatRot (q, m):
    m [:, 0] = quatVecRot (q, m [:, 0])
    m [:, 1] = quatVecRot (q, m [:, 1])
    m [:, 2] = quatVecRot (q, m [:, 2])
    return m
    