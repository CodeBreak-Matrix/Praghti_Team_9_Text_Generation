import cv2
import numpy as np

#events = [i for i in dir(cv2) if 'EVENT' in i]
#dir() inbuilt method to show all classes and functions in cv2 library
#print(events)

def click_event(event, x,y, flags, param):
    #Arguments: event (which mouse button clicked), x and y coordinates of the click, flags and param
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

#img = np.zeros((512,512,3),np.uint8)
img = cv2.imread('messi5.jpg',1)
cv2.imshow("Image", img)

cv2.setMouseCallback("Image",click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()