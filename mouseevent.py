import cv2
import numpy as np

def click_event(event, x,y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
        print(x,' , ',y)
        strXY= str(x)+' '+str(y)
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(img, strXY, (x,y),font, 1, (255,255,0),1)
        cv2.imshow("Image", img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green= img[y,x,1]
        red= img[y,x,2]
        strXY = 'B:'+str(blue)+' G:'+str(green)+' R:'+str(red)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, strXY, (x, y), font, 1, (0, 255, 0), 1)
        cv2.imshow("Image", img)
        
#If we wish to use NumPy to create a blank image
#img = np.zeros((512,512,3),np.uint8)
img = cv2.imread('messi5.jpg',1)
cv2.imshow("Image", img)

cv2.setMouseCallback("Image",click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
