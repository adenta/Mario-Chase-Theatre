import io,math,random
import numpy as np

def buildCircle(r):
    y,x = np.ogrid[-r: r+1, -r: r+1]
    mask = x**2+y**2 <= r**2-1

    return mask
def drawCircle(circle):
    for row in circle:
        st = ""
        for col in row:
            if col and random.randint(0,100)>5 :
                st+= "  "
            else:
                st+= "##"
        print st

print buildCircle(5)
drawCircle(buildCircle(15))
