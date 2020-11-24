###############################################################################
## Author: Team Supply Bot
## Edition: eYRC 2019-20
## Instructions: Do Not modify the basic skeletal structure of given APIs!!!
###############################################################################


######################
## Essential libraries
######################
import cv2
import numpy as np
import os
import math
import csv
import cv2.aruco as aruco
from aruco_lib import *
import sys, getopt


########################################################################
## using os to generalise Input-Output
########################################################################
codes_folder_path = os.path.abspath('.')
images_folder_path = os.path.abspath(os.path.join('..', 'Videos'))
generated_folder_path = os.path.abspath(os.path.join('..', 'Generated'))




############################################
## Build your algorithm in this function
## ip_image: is the array of the input image
## imshow helps you view that you have loaded
## the corresponding image
############################################
def process(ip_image):
    ###########################
    ## Your Code goes here
    alpha = 2.2
    beta = 20
    img1 =  cv2.convertScaleAbs(ip_image, alpha=alpha, beta=beta)
    cv2.imwrite(generated_folder_path+"/"+'bot.jpg',img1)
    def blur_edge(img, d=31):
        h, w  = img.shape[:2]
        img_p = cv2.copyMakeBorder(img, d, d, d, d, cv2.BORDER_WRAP)
        img_b = cv2.GaussianBlur(img_p, (2*d+1, 2*d+1), -1)[d:-d,d:-d]
        y, x = np.indices((h, w))
        dist = np.dstack([x, w-x-1, y, h-y-1]).min(-1)
        w = np.minimum(np.float32(dist)/d, 1.0)
        return img*w + img_b*(1-w)

    def motion_kernel(angle, d, sz=65):
        kern = np.ones((1, d), np.float32)
        c, s = np.cos(angle), np.sin(angle)
        A = np.float32([[c, -s, 0], [s, c, 0]])
        sz2 = sz // 2
        A[:,2] = (sz2, sz2) - np.dot(A[:,:2], ((d-1)*0.5, 0))
        kern = cv2.warpAffine(kern, A, (sz, sz), flags=cv2.INTER_CUBIC)
        return kern

    def defocus_kernel(d, sz=65):
        kern = np.zeros((sz, sz), np.uint8)
        cv2.circle(kern, (sz, sz), d, 255, -1, cv2.LINE_AA, shift=1)
        kern = np.float32(kern) / 255.0
        return kern

    
    opts, args = getopt.getopt(sys.argv[1:], '', ['circle', 'angle=', 'd=', 'snr='])
    opts = dict(opts)
    try:
        function = args[0]
    except:
        function = '../Generated/bot.jpg'
    win = 'TEAM NEW'
    img = cv2.imread('../Generated/bot.jpg', cv2.IMREAD_GRAYSCALE)
    if img is None:
        print('Failed to load file ', function)
        sys.exit(1)

    img = np.float32(img)/255.0
    img = blur_edge(img)
    IMG = cv2.dft(img, flags=cv2.DFT_COMPLEX_OUTPUT)
    defocus = '--circle' in opts

    def update(_):
        ang = np.deg2rad( cv2.getTrackbarPos('angle', win) )
        d = cv2.getTrackbarPos('d', win)
        noise = 10**(-0.1*cv2.getTrackbarPos('SNR (db)', win))

        if defocus:
            pointspread = defocus_kernel(d)
        else:
            pointspread = motion_kernel(ang, d)
                
        pointspread /= pointspread.sum()
        pointspread_pad = np.zeros_like(img)
        kh, kw = pointspread.shape
        pointspread_pad[:kh, :kw] = pointspread
        PSF = cv2.dft(pointspread_pad, flags=cv2.DFT_COMPLEX_OUTPUT, nonzeroRows = kh)
        PSF2 = (PSF**2).sum(-1)
        iPSF = PSF / (PSF2 + noise)[...,np.newaxis]
        RES = cv2.mulSpectrums(IMG, iPSF, 0)
        result = cv2.idft(RES, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT )
        result = np.roll(result, -kh//2, 0)
        result = np.roll(result, -kw//2, 1)
                
        cv2.imwrite('../Generated/bot_blur.jpg',255*result)
        cv2.destroyAllWindows()
    cv2.namedWindow(win)
    cv2.createTrackbar('angle', win, int(opts.get('--angle', 90)), 180, update)
    cv2.createTrackbar('d', win, int(opts.get('--d', 20)), 50, update)
    cv2.createTrackbar('SNR (db)', win, int(opts.get('--snr', 20)), 50, update)
    update(None)
    print('Done Debluring the frame...')
    
    #angle finder
    robot_state=0
    det_aruco_list = {}
    frame = cv2.imread("../Generated/bot_blur.jpg")
    det_aruco_list = detect_Aruco(frame)
    if det_aruco_list:
            img = mark_Aruco(frame,det_aruco_list)
            robot_state = calculate_Robot_State(img,det_aruco_list)
            print(robot_state)

    dicti = robot_state
    listi = [v for v in dicti.values()]
    
    
    cv2.imwrite("../Generated/aruco_with_id.png",img)
    print("Image Angle written successfully")
    return img, listi[0]

    
####################################################################
## The main program which provides read in input of one image at a
## time to process function in which you will code your generalized
## output computing code
## Do not modify this code!!!
####################################################################
def main(val):
    ################################################################
    ## variable declarations
    ################################################################
    i = 1
    ## reading in video 
    cap = cv2.VideoCapture(images_folder_path+"/"+"ArUco_bot.mp4")
    ## getting the frames per second value of input video
    fps = cap.get(cv2.CAP_PROP_FPS)
    ## getting the frame sequence
    frame_seq = int(val)*fps
    ## setting the video counter to frame sequence
    cap.set(1,frame_seq)
    ## reading in the frame
    ret, frame = cap.read()
    ## verifying frame has content
    print(frame.shape)
    ## display to see if the frame is correct
    #cv2.imshow("window", frame)
    cv2.waitKey(0);
    ## calling the algorithm function
    op_image, aruco_info = process(frame)
    ## saving the output in  a list variable
    line = [str(i), "Aruco_bot.jpg" , str(aruco_info[0]), str(aruco_info[3])]
    ## incrementing counter variable
    i+=1
    ## verifying all data
    print(line)
    ## writing to angles.csv in Generated folder without spaces
    with open(generated_folder_path+"/"+'output.csv', 'w') as writeFile:
        print("About to write csv")
        writer = csv.writer(writeFile)
        writer.writerow(line)
    ## closing csv file    
    writeFile.close()


############################################################################################
## main function
############################################################################################
if __name__ == '__main__':
    main(input("time value in seconds:"))
