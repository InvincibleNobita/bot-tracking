import cv2
import numpy as np
pointsList=[]
def y():
    pass
cap=cv2.imread('arena-img.png')
cv2.namedWindow("HSV_Trackbars")

# range of Hue= 0-179, range of Saturation and Value = 0-255
cv2.createTrackbar("L_H", "HSV_Trackbars", 0, 179, y)
cv2.createTrackbar("L_S", "HSV_Trackbars", 0, 255, y)
cv2.createTrackbar("L_V", "HSV_Trackbars", 0, 255, y)
cv2.createTrackbar("U_H", "HSV_Trackbars", 179, 179, y)
cv2.createTrackbar("U_S", "HSV_Trackbars", 255, 255, y)
cv2.createTrackbar("U_V", "HSV_Trackbars", 255, 255, y)
while True:
    cv2.imshow('img',cap)
    hsv=cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
    # l_h = cv2.getTrackbarPos("L_H", "HSV_Trackbars")
    # l_s = cv2.getTrackbarPos("L_S", "HSV_Trackbars")
    # l_v = cv2.getTrackbarPos("L_V", "HSV_Trackbars")
    l_h=39
    l_s=49 
    l_v=50
    u_h = cv2.getTrackbarPos("U_H", "HSV_Trackbars")
    u_s = cv2.getTrackbarPos("U_S", "HSV_Trackbars")
    u_v = cv2.getTrackbarPos("U_V", "HSV_Trackbars")

    l_r = np.array([l_h, l_s, l_v])
    u_r = np.array([u_h, u_s, u_v])

    
    
    # low_blue=np.array([170,35,80])
    # high_blue=np.array([190,50,120])
    
    mask=cv2.inRange(hsv,l_r,u_r)
    res = cv2.bitwise_and(cap, cap, mask=mask)

    
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    s1=d1=0
    if len(pointsList)>1:
        break
    for cnt in contours:
        
        area = cv2.contourArea(cnt)
        if area> 1500:
            print(area)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(res,(x,y),(x+w,y+h),(230,45,189)) 
            
            if x<100:
                s1=[(x+w)//2,(y+h)//2]
            if x>500:
                d1=[(x+w)//2,(y+h)//2]
            if s1 and d1:
                pointsList.append([s1,d1])
    
    cv2.imshow('res',res) 
    if cv2.waitKey(1) ==27:
        break
#cap.release()
cv2.destroyAllWindows()
print(pointsList)
'''
s1=34 49 50
'''

    