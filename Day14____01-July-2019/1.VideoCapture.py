import cv2 as cv
v=cv.VideoCapture(0)
while(1):
    r,i=v.read() # r is the return type of image
    cv.imshow('img',i)
    k=cv.waitKey(3)
    if(k==ord('q')):
        cv.destroyAllWindows()
        break















