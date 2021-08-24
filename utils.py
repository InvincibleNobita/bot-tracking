from math import *

from computer import comp

def dist(a,b):
    #two tuples/ coordinates
    x1,y1=a[0],a[1]
    x2,y2=b[0],b[1]
    val=(((x2-x1)**2)+((y2-y1)**2))
    return sqrt(val)

def xyd(a,b):
    x1,y1=a[0],a[1]
    x2,y2=b[0],b[1]
    x=abs(x2-x1)
    y=abs(y2-y1)
    return (x,y)

def std(a,b):
    x1,y1=a[0],a[1]
    x2,y2=b[0],b[1]
    x=x1
    y=y2
    return (x,y)

def checker(dist,dist1):
    #print(dist,dist1)
    val=False
    if dist:
        
        if(dist1<=5):
            print(dist1)
            dist1=0
            dist.pop()
            print("stop")
            comp(0)
            # dist1=dist2
                
            val = True
            
        elif(dist1<dist[-1]):
            dist.pop()
            dist.append(dist1)
            print("forward")
            comp(1)
            comp(0)
    else:
        #if dist1:
        dist.append(dist1)
        #print(dist1)
    #     # else:
    #     #     dist.append(dist2)
    #     #     print(dist2)

    
    return val



    


