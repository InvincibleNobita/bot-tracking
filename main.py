import utils
import cv2
from tracker import *
import time

from computer import comp

tracker = EuclideanDistTracker()

cap = cv2.VideoCapture('bot-vid.mp4')

object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

dist=[]

while True:
    
    ret, frame = cap.read()
    
    #TODO: Check the height and width of your frame and put it in line 26
    height, width, _ = frame.shape
    print("Manish",height,width)
    time.delay(5)
    
    roi = frame[0:352,150: 360]

    
    
    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    detections = []
    for cnt in contours:
        
        
        area = cv2.contourArea(cnt)
        print(area) #TODO: check the area of your bot and accordingly set the if condition
        
        
        if area > 10000:
            
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(roi,(x,y),(x+w,y+h),(230,45,189))     
            detections.append([x, y, w, h])

    boxes_ids = tracker.update(detections)
    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        
        if id==0:
            cv2.putText(roi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 5)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cofbot=((x+w//2),(y+h//2))
            cv2.circle(roi,cofbot,3,(0,0,255),-1)
            endpnt=(300,20)
            cv2.circle(roi,endpnt,7,(0,0,255),-1)
          

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
                    comp(0)
                elif(dist1<dist[-1]):
                    dist.append(dist1)
                    print("forward")
                    comp(1)
            else:
                dist.append(dist1)
                print(dist1)
    if ret:
        cv2.imshow("Frame", frame)
       

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()