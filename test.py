import cv2
import numpy as np
# IMPORT IMAGE
img = cv2.imread("ans.png",1)

# REMOVE NOISE
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_, binary_threshold = cv2.threshold(gray,127,255,0)

# LINE DETECTION
_,contours_list,_ = cv2.findContours(binary_threshold.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# for i in c:
# 	area = cv2.contourArea(i)
# 	if area>1000:
# 		x.append(i)
required_sections_list = sorted(contours_list, key = cv2.contourArea, reverse = True)[2:6]

print(required_sections_list)
cv2.drawContours(img,required_sections_list,0,(0,0,255),2)
cv2.drawContours(img,required_sections_list,1,(0,255,255),2)
cv2.drawContours(img,required_sections_list,2,(255,0,255),2)
cv2.drawContours(img,required_sections_list,3,(255,0,0),2)

cv2.namedWindow('Marksheet', cv2.WINDOW_NORMAL)
cv2.imshow('Marksheet',img)
cv2.waitKey(0)
cv2.destroyAllWindows()