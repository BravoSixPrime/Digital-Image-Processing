#DIP Assignment 8 - Canny Edge Detection
import cv2

# Read the original image
img = cv2.imread("image.jpg") 
# Display original image
cv2.imwrite('8/Original.jpg', img)
cv2.waitKey(0)

# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 

# Sobel Edge Detection
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
# Display Sobel Edge Detection Images
cv2.imwrite('8/Sobel X.jpg', sobelx)
cv2.waitKey(0)
cv2.imwrite('8/Sobel Y.jpg', sobely)
cv2.waitKey(0)
cv2.imwrite('8/Sobel X Y using Sobel() function.jpg', sobelxy)
cv2.waitKey(0)

# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
# Display Canny Edge Detection Image
cv2.imwrite('8/Canny Edge Detection.jpg', edges)
cv2.waitKey(0)

cv2.destroyAllWindows()