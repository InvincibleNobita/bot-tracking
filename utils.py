from math import *


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


    


