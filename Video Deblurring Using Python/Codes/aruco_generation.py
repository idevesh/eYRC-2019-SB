import numpy as np
import cv2
import cv2.aruco as aruco
 
 
'''
    drawMarker(...)
        drawMarker(dictionary, id, sidePixels[, img[, borderBits]]) -> img
'''
 
aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_50) #creating aruco dictionary...250 markers and a marker size of 6x6 bits
print(aruco_dict)
# second parameter is id number
# last parameter is total image size
img = aruco.drawMarker(aruco_dict, 25, 600) # 2-- marker id, as the chose dictionary is upto 250...so the id no ranges from 0 to 249....and 700x700 is the pixel size
# cv2.imwrite("Aruco_ids/test_marker11_big.jpg", img)
print (img.shape)
r,c = img.shape
r = r+50
c = c+50
img2 = np.ones((r,c), np.uint8)*255
img2[25:425,25:425] = img
cv2.imshow('frame',img2)
cv2.imwrite("aruco25.jpg", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
