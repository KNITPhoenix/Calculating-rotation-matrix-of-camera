###############
##Design the function "findRotMat" to  return 
# 1) rotMat1: a 2D numpy array which indicates the rotation matrix from xyz to XYZ 
# 2) rotMat2: a 2D numpy array which indicates the rotation matrix from XYZ to xyz 
#It is ok to add other functions if you need
###############

import numpy as np
import cv2

def findRotMat(alpha, beta, gamma):
    alpha=np.deg2rad(alpha)
    beta=np.deg2rad(beta)
    gamma=np.deg2rad(gamma)

    r1=np.array([[np.cos(alpha),(-1)*np.sin(alpha),0],[np.sin(alpha),np.cos(alpha),0],[0,0,1]])
    r2=np.array([[1,0,0],[0,np.cos(beta),(-1)*np.sin(beta)],[0,np.sin(beta),np.cos(beta)]])
    r3=np.array([[np.cos(gamma),(-1)*np.sin(gamma),0],[np.sin(gamma),np.cos(gamma),0],[0,0,1]])

    a=np.dot(r2,r1)
    rotMat1=np.dot(r3,a)

    r1 = np.array([[np.cos(-alpha), (-1) * np.sin(-alpha), 0], [np.sin(-alpha), np.cos(-alpha), 0], [0, 0, 1]])
    r2 = np.array([[1, 0, 0], [0, np.cos(-beta), (-1) * np.sin(-beta)], [0, np.sin(-beta), np.cos(-beta)]])
    r3 = np.array([[np.cos(-gamma), (-1) * np.sin(-gamma), 0], [np.sin(-gamma), np.cos(-gamma), 0], [0, 0, 1]])

    a=np.dot(r2,r3)
    rotMat2=np.dot(r1,a)

    return rotMat1,rotMat2

if __name__ == "__main__":
    alpha = 45
    beta = 30
    gamma = 60
    rotMat1, rotMat2 = findRotMat(alpha, beta, gamma)
    print(rotMat1)
    print(rotMat2)
