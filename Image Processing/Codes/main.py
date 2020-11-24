import cv2
import numpy as np
import os
import csv
bird = cv2.imread('../Images/bird.jpg')
cat = cv2.imread('../Images/cat.jpg')
flow = cv2.imread('../Images/flowers.jpg')
horse = cv2.imread('../Images/horse.jpg')

h1,w1,c1=bird.shape
img_bird='bird.jpg'
    
h2,w2,c2=cat.shape
img_cat='cat.jpg'
    
h3,w3,c3=flow.shape
img_flow = 'flowers.jpg'
    
h4,w4,c4=horse.shape
img_horse = 'horse.jpg'
    
def partA():
    mh1=h1/2
    mw1=w1/2
    mh2=h2/2
    mw2=w2/2
    mh3=h3/2
    mw3=w3/2
    mh4=h4/2
    mw4=w4/2
    with open('../Generated/stats.csv','w',newline='') as csvfile:
        filewriter = csv.writer(csvfile,delimiter = ',',quotechar='|',quoting=csv.QUOTE_NONE)
        filewriter.writerow([img_bird,h1,w1,c1])    
        filewriter.writerow([img_cat,h2,w2,c2])
        filewriter.writerow([img_flow,h3,w3,c3])
        filewriter.writerow([img_horse,h4,w4,c4])

    
    print("Created stats.csv file in the generated folder.")
def partB():
    image = cv2.imread('../Images/cat.jpg')
    red_channel = image[:,:,2]
    red_img = np.zeros(image.shape)
    red_img[:,:,2] = red_channel
    image_name1 = '../Generated/cat_red.jpg'
    cv2.imwrite(image_name1,red_img)
    print("Created cat_red.jpg in generated folder.")

def partC():
    b, g, r = cv2.split(flow)
    alpha_channel = np.ones(b.shape, dtype=b.dtype) * 50
    img_BGRA = cv2.merge((b, g, r, alpha_channel))
    cv2.imwrite('../Generated/flowers_alpha.png',img_BGRA)
    print("Created flowers_alpha.png in the generated folder.")
def partD():
    gray_img = cv2.cvtColor(horse, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('../Generated/horse_gray.jpg',gray_img)
    print("Created horse_gray.jpg in the generated folder.")
    
partA()
partB()
partC()
partD()
