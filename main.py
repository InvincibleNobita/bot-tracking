#from math import dist
#from utils import dist
import utils
import cv2
from tracker import *
import time

#from computer import comp

# Create tracker object
tracker = EuclideanDistTracker()

cap = cv2.VideoCapture('bot-vid.mp4')

# Object detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

dist=[]

while True:
    
    ret, frame = cap.read()
    #blur_frame=cv2.GaussianBlur(frame,(5, 5),0)

    height, width, _ = frame.shape
    #print(height,width)
    #height=352
    #width=640

    # Extract Region of interest
    roi = frame[0:352,150: 360]

    # # 1. Object Detection
    # #// TODO:
    mask = object_detector.apply(roi) #change to roi here
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(roi, contours, -1, (0, 255, 0), 2)
    # #print(contours)
    detections = []
    for cnt in contours:
        # Calculate area and remove small elements
        
        area = cv2.contourArea(cnt)
        #print(area)
        #if area==0:continue
        if area > 10000:
            #print(area)
            #print(cnt)
            #cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(cnt)
            #print(x)
            cv2.rectangle(roi,(x,y),(x+w,y+h),(230,45,189))
    #         #x, y, w, h = cv2.rectangle()
    #         #x,y,w,h= cv2.rectangle(roi,(x,y),(x+w,y+h),(230,45,189))


            detections.append([x, y, w, h])
            #print(x)

    # # 2. ObjectQ Tracking
    boxes_ids = tracker.update(detections)
    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        #print(x,y,w,h)
        if id==0:
            cv2.putText(roi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 5)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cofbot=((x+w//2),(y+h//2))
            cv2.circle(roi,cofbot,3,(0,0,255),-1)
            endpnt=(300,20)
            cv2.circle(roi,endpnt,7,(0,0,255),-1)
            #dist=utils.dist(cofbot,endpnt)
            
            #cv2.putText(roi, str(dist1), (x, y - 35), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 5)
            # xy=utils.xyd(cofbot,endpnt)
            # cv2.circle(roi,xy,5,(0,0,255),-1)
            # cv2.line(roi,cofbot,xy,(122,122,210),7)
            # cv2.line(roi,xy,endpnt,(122,122,10),7)

            xy=utils.std(cofbot,endpnt)
            cv2.circle(roi,xy,5,(0,0,255),-1)
            cv2.line(roi,cofbot,xy,(122,122,210),7)
            cv2.line(roi,xy,endpnt,(122,122,10),7)

            dist1=utils.dist(cofbot,xy)
            dist2=utils.dist(xy,endpnt)
            '''
            0-> stop
            1 -> forward
            2 -> right
            3-> left
            '''
            if dist:
                if(dist1<=5):
                    print(dist1)
                    print("stop")
                    #comp(0)
                elif(dist1<dist[-1]):
                    dist.append(dist1)
                    print("forward")
                    #comp(1)
            else:
                dist.append(dist1)
                print(dist,dist1)
                





            #cv2.line(roi,((x+w//2),(y+h//2)),(200,200),(122,122,10),7)


    # # #cv2.imshow("roi", roi)
    if ret:
        cv2.imshow("Frame", frame)
        cv2.imshow("ro1", roi)
        #cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    time.sleep(0.095)

cap.release()
cv2.destroyAllWindows()