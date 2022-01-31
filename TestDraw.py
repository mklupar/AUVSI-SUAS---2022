# takes images from the CroppedFields Folder and places target over those images. Save this new image to DataSet folder.
import random
import cv2
import string
import os
import time

def DrawShapeOntoImage(img):

    # Shape choose setup
    possibleShapes = [1, 2]
    possibleLabels = [1, 2]


    # start coordinate
    x1 = random.choice(range(20, 620))
    y1 = random.choice(range(20, 460))
    # end coordinate
    x2 = x1 + random.choice(range(30, 100))
    y2 = y1 + random.choice(range(30, 100))

    # Circle radius
    radius = random.choice(range(10, 75))
    # Font type
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontthic = 2

    # Draw Shape
    # Text inside shape
    textType = random.choice(possibleLabels)
    if textType == 1:
        label = random.choice("0123456789")
    else:
        label = random.choice(string.ascii_letters.upper())

    # get boundry of text
    textwidth, textheight = cv2.getTextSize(label, font, 1, fontthic)[0]

    # pick image shape and text
    shape = random.choice(possibleShapes)

    # text color choose
    b1 = random.choice(range(0, 255))
    g1 = random.choice(range(0, 255))
    r1 = random.choice(range(0, 255))

    # image color choose
    b = random.choice(range(0, 255))
    g = random.choice(range(0, 255))
    r = random.choice(range(0, 255))

    if shape == 1:
        # get coords based on boundary
        rect_center = ((x1 + x2) // 2, (y1 + y2) // 2)
        textX = (rect_center[0] - (textwidth // 2))
        textY = (rect_center[1] + (textheight // 2))

        img = cv2.rectangle(img, (x1, y1), (x2, y2), (b, g, r), -1)
        img = cv2.putText(img, label, (textX, textY), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (b1, g1, r1), fontthic)

    else:
        textX = (x1 - (textwidth // 2))
        textY = (y1 + (textheight // 2))

        img = cv2.circle(img, (x1, y1), radius, (b, g, r), -1)
        img = cv2.putText(img, label, (textX, textY), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (b1, g1, r1), fontthic)


    # trying to not kill my computer
    time.sleep(0.1)
    return img


if __name__ == '__main__':
    path = r'D:\Pycharm Projects\Pycharm Data Processing\CroppedFields\Copy1.jpg'
    img = cv2.imread(path)
    
    img = DrawShapeOntoImage(img)
    # Show image and save them to the DataSet folder
    cv2.imshow('image', img)

#TODO: create more shapes and find more fields to finish data set
