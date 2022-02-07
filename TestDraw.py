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

    # start and end coordinates of Rectangle
    x1Start = random.choice(range(30, 1920 - 460))
    y1Start = random.choice(range(30, 1080 - 460))
    x2End = x1Start + random.choice(range(30, 60))
    y2End = y1Start + random.choice(range(30, 60))

    # circle start coordinate
    x1CircStart = random.choice(range(35, 1020))
    y1CircStart = random.choice(range(35, 1020))


    # Circle radius
    radius = random.choice(range(15, 30))
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
        rect_center = ((x1Start + x2End) // 2, (y1Start + y2End) // 2)
        textX = (rect_center[0] - (textwidth // 2))
        textY = (rect_center[1] + (textheight // 2))

        img = cv2.rectangle(img, (x1Start, y1Start), (x2End, y2End), (b, g, r), -1)
        img = cv2.putText(img, label, (textX, textY), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (b1, g1, r1), fontthic)

    else:
        textX = (x1CircStart - (textwidth // 2))
        textY = (y1CircStart + (textheight // 2))

        img = cv2.circle(img, (x1CircStart, y1CircStart), radius, (b, g, r), -1)
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
