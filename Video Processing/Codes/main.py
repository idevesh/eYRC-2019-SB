import cv2
import numpy as np
import os
def partA():
    cap = cv2.VideoCapture('../Videos/RoseBloom.mp4')
    video_images = '../Generated'
    if not cap.isOpened():
        exit(0)

    frameFreq = 25
    tot_frame=0
    id=0
    while True:
        ret,frame=cap.read()
        if ret is False:
            break
        tot_frame+=1
        if tot_frame%frameFreq == 0:
            id+=1
            if id == 6:
                image_name = '../Generated/frame_as_' + str(id) + '.jpg'
                cv2.imwrite(image_name,frame)
                print("Creating ",image_name)
    cap.release()

def partB():
    image = cv2.imread('../Generated/frame_as_6.jpg')
    red_channel = image[:,:,2]
    red_image = np.zeros(image.shape)
    red_image[:,:,2] = red_channel
    image_name1 = '../Generated/frame_as_6_red.jpg'
    cv2.imwrite(image_name1,red_image)
    cv2.waitKey(0)
    print("Created ",image_name1)
partA()
partB()
