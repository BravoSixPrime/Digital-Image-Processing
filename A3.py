#BT19ECE057
#Jayvardhan Patil
#Assignment-3
#To create two images one with a white circle another with a white rentangle at center 
#and to perform all logical operations on these images and display the output images. 

#importing required libraries.
import math 
import numpy as np
import cv2

Image_1 = np.zeros((512,512),np.uint8)         # Creating two black images
Image_2 = np.zeros((512,512),np.uint8)

Image_1 = cv2.circle(Image_1,(235,250),80,(255,255,255),-1)             # White Circle at Centre of Image1       
Image_2 = cv2.rectangle(Image_2,(100,300),(330,190),(255,255,255),-1)   # White Rectangle at Centre of Image2


# Now performing logic operations and displaying the output images

cv2.imshow("white circle at center image",Image_1)

cv2.imwrite("3/white circle at center image.jpg",Image_1)
cv2.waitKey(0)
cv2.imshow("white rectangle at center image",Image_2)
cv2.imwrite("3/white rectangle at center image.jpg",Image_2)
cv2.waitKey(0)

# AND operation
cv2.imshow("AND operation",cv2.bitwise_and(Image_1,Image_2))
cv2.imwrite("3/AND operation.jpg",cv2.bitwise_and(Image_1,Image_2))

cv2.waitKey(0)

# OR operation
cv2.imshow("OR operation",cv2.bitwise_or(Image_1,Image_2))
cv2.imwrite("3/OR operation.jpg",cv2.bitwise_or(Image_1,Image_2))
cv2.waitKey(0)

# NAND operation
cv2.imshow("NAND operation",cv2.bitwise_not(cv2.bitwise_and(Image_1,Image_2)))
cv2.imwrite("3/NAND operation.jpg",cv2.bitwise_not(cv2.bitwise_and(Image_1,Image_2)))
cv2.waitKey(0)

# NOR operation
cv2.imshow("NOR operation",cv2.bitwise_not(cv2.bitwise_or(Image_1,Image_2)))
cv2.imwrite("3/NAND operation.jpg",cv2.bitwise_not(cv2.bitwise_or(Image_1,Image_2)))
cv2.waitKey(0)

# EX-OR operation
cv2.imshow("EXOR operation",cv2.bitwise_xor(Image_1,Image_2))
cv2.imwrite("3/EXOR operation.jpg",cv2.bitwise_xor(Image_1,Image_2))
cv2.waitKey(0)

# EX-NOR operation
cv2.imshow("EXNOR operation",cv2.bitwise_not(cv2.bitwise_xor(Image_1,Image_2)))
cv2.imwrite("3/EXNOR operation.jpg",cv2.bitwise_not(cv2.bitwise_xor(Image_1,Image_2)))
cv2.waitKey(0)