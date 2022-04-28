#BT19ECE057
#Jayvardhan Patil
#Assignment 1:
# 1) Read and dispaly a color image
# 2) Convert color image to grayscale and binary
# 3) Add constant value to it

# Importing required libraries
import math                                               
import numpy as np
import cv2

path = "./image.jpg" #declaring path of image
image = cv2.imread(path)                                  #Reading the image   
m,n,v = image.shape                                      
gray_image = np.zeros((m,n),np.uint8)                   
binary_image = np.zeros((m,n),np.uint8)  
added_const = np.zeros((m,n),np.uint8)

for i in range(m):        #Converting color Image to Grayscale by averaging
    for j in range(n): 
        k=0;                           
        for k in range(v):
            k += math.floor(image[i][j][k]/3)

        gray_image[i][j] = k

for x in range(m):        #Converting gray Image to binary, Threshold = 50
    for y in range(n):
        if gray_image[x][y]>=50 :
          binary_image[x][y]=0
        else:
          binary_image[x][y]=255


for x in range(m):        #Adding a constant value '34' to image
    for y in range(n):
        k=min(gray_image[x][y]+34,255)
        added_const[x][y]=k

#Dispalying the Images
cv2.imshow("original Image",image)
cv2.imwrite("1/original Image.jpg",image)
cv2.waitKey(0)
cv2.imshow('Grayscale Image',gray_image)
cv2.imwrite('1/Grayscale Image.jpg',gray_image)
cv2.waitKey(0)
cv2.imshow('Binary Image',binary_image)
cv2.imwrite('1/Binary Image.jpg',binary_image)
cv2.waitKey(0)
cv2.imshow('Grayscale Image + constant value ',added_const)
cv2.imwrite('1/Grayscale Image + constant value.jpg',added_const) 
cv2.waitKey(0)
cv2.destroyAllWindows()