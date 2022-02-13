#BT19ECE057
#Jayvardhan Patil
#Assignment 2:
# 1) Read and dispaly a color image
# 2) Convert color image to grayscale
# 3) Making some part of the image black

# Importing required libraries
import math                                               
import numpy as np
import cv2

path = "./image.jpg" #declaring path of image
image = cv2.imread(path)                                  #Reading the image   
m,n,v = image.shape                                      
gray_image = np.zeros((m,n),np.uint8)                   
result_image = np.zeros((m,n),np.uint8)  

for i in range(m):              #Converting color Image to Grayscale by averaging
    for j in range(n): 
        k=0;                           
        for k in range(v):
            k += math.floor(image[i][j][k]/3)

        gray_image[i][j] = k
        result_image[i][j] = k

for x in range(35,270,1):         #Making some part of the image black
   for y in range(45,270,1):
       result_image[x][y] = 0

#Dispalying the Images
cv2.imshow("original Image",image)
cv2.waitKey(0)
cv2.imshow('Grayscale Image',gray_image)
cv2.waitKey(0)
cv2.imshow('New Image',result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()