import cv2 as cv

#only for images,Video and live video
def rescaleFrame(frame,scale=0.75):
    #This function is used to rescale the frame of the video or image
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

#only for live video
def changeRes(width,height):
    #This function is used to change the resolution of the video
    capture.set(3,width)
    capture.set(4,height)

# Read the image
img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat', img)
resized_image=rescaleFrame(img,scale=0.2)
cv.imshow('Resized Cat',resized_image)



# Read the video
capture=cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue,frame=capture.read()
    frame_resized=rescaleFrame(frame,scale=0.2)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()