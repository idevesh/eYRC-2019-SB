import numpy as np
import cv2
import cv2.aruco as aruco
from aruco_lib import *

frame = cv2.imread("../Generated/bot_blur.jpeg")
robot_state=0
det_aruco_list = {}


det_aruco_list = detect_Aruco(frame)
if det_aruco_list:
	img = mark_Aruco(frame,det_aruco_list)
	robot_state = calculate_Robot_State(img,det_aruco_list)
	print(robot_state)        
cv2.imwrite("output.jpg",frame)
cv2.destroyAllWindows()
