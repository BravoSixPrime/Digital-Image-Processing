#BT19ECE057
#Jayvardhan Patil
#Assignment-4
#Reading a color image and display its Red, Green and Blue components


import cv2
path ="./image.jpg" #declaring path of image
original = cv2.imread(path)                                  #Reading the image
original_red = cv2.imread(path)
original_green = cv2.imread(path)
original_blue = cv2.imread(path)

#Converting Images to Red, Green and Blue
original_blue[:,:,1],original_blue[:,:,2] = 0,0     #For Blue : Green and Red = 0
original_green[:,:,0],original_green[:,:,2] = 0,0   #For Green : Red and Blue = 0          
original_red[:,:,0],original_red[:,:,1] = 0,0       #For Red : Blue and Green = 0

#Dispalying Images
cv2.imwrite("4/Original Image.jpg",original)
cv2.waitKey(0)
cv2.imwrite("4/Original Image.jpg",original_red)
cv2.waitKey(0)
cv2.imwrite("4/Green Component.jpg",original_green)
cv2.waitKey(0)
cv2.imwrite("4/Blue Component.jpg",original_blue)
cv2.waitKey(0)