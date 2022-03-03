# takes images from the CroppedFields Folder and places target over those images. Save this new image to DataSet folder.
import random
import cv2
import string
import time
import numpy as np


def DrawShapeOntoImage(img):
    # Shape choose setup
    possibleShapes = [6]  # [i for i in range(1, 14)]  # list 1 - 13 for all shapes
    possibleLabels = [1, 2]  # Letter or Number pick

    # start and end coordinates of Shapes
    x1Start = random.choice(range(30, 1920 - 65))
    y1Start = random.choice(range(30, 1080 - 65))
    x2End = x1Start + random.choice(range(30, 60))
    y2End = y1Start + random.choice(range(30, 60))

    # circle start coordinate
    x1CircStart = random.choice(range(35, 1020))
    y1CircStart = random.choice(range(35, 1020))

    # Circle radius
    radius = random.choice(range(15, 30))
    # Font type
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontthic = 1
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

    def PlaceText(ShapeCenter, img):  # Places text at the center of the shape
        textX = (ShapeCenter[0] - (textwidth // 2))
        textY = (ShapeCenter[1] + (textheight // 2))
        img = cv2.putText(img, label, (textX, textY), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (b1, g1, r1), fontthic)

    if shape == 1:  # Rectangle
        img = cv2.rectangle(img, (x1Start, y1Start), (x2End, y2End), (b, g, r), -1)
        rect_center = ((x1Start + x2End) // 2, (y1Start + y2End) // 2)
        PlaceText(rect_center, img)

    elif shape == 2:  # Circle
        textX = (x1CircStart - (textwidth // 2))
        textY = (y1CircStart + (textheight // 2))

        img = cv2.circle(img, (x1CircStart, y1CircStart), radius, (b, g, r), -1)
        img = cv2.putText(img, label, (textX, textY), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (b1, g1, r1), fontthic)

    elif shape == 3:  # Trapezoid
        contour = np.array(
            [[x1Start, y1Start], [x1Start + 20, y1Start], [x1Start - 10, y1Start + 30], [x1Start + 30, y1Start + 30],
             [x1Start, y1Start], [x1Start - 10, y1Start + 30], [x1Start + 20, y1Start],
             [x1Start + 30, y1Start + 30]])  # coords of where to fill color

        cv2.fillPoly(img, [contour], (b, g, r))  # fills in the shape.

        trap_center = (x1Start + 12, y1Start + 15)  # center of the trapezoid
        PlaceText(trap_center, img)

    elif shape == 4:  # Pentagon
        contour = np.array([[x1Start, y1Start], [x1Start + 24, y1Start + 20],
                            [x1Start + 16, y1Start + 46], [x1Start - 16, y1Start + 46],
                            [x1Start - 26, y1Start + 20]], np.int32)
        cv2.fillPoly(img, [contour], (b, g, r))  # fills in the shape.

        pent_center = (x1Start, y1Start + 27)  # center of the trapezoid
        PlaceText(pent_center, img)

    elif shape == 5:  # Hexagon
        contour = np.array([[x1Start, y1Start], [x1Start + 36, y1Start], [x1Start + 54, y1Start + 18],
                            [x1Start + 36, y1Start + 36], [x1Start, y1Start + 36], [x1Start - 18, y1Start + 18]],
                           np.int32)
        cv2.fillPoly(img, [contour], (b, g, r))  # fills in the shape.
        hex_center = (x1Start + 18, y1Start + 18)
        PlaceText(hex_center, img)

    elif shape == 6:  # triangle
        contour = np.array([[x1Start, y1Start], [x1Start + 50, y1Start], [x1Start + 25, y1Start - 35]], np.int32)
        cv2.fillPoly(img, [contour], (b, g, r))
        tri_center = (x1Start + 26, y1Start - 15)
        PlaceText(tri_center, img)

    elif shape == 7:  # semi circle
        img = cv2.ellipse(img, (x1Start, y1Start), (30, 30), 0, 270, 450, (b, g, r), -1)
        semi_center = (x1Start + 15, y1Start)
        PlaceText(semi_center, img)

    elif shape == 8:  # quarter circle
        img = cv2.ellipse(img, (x1Start, y1Start), (40, 40), 0, 0, 90, (b, g, r), -1)
        quarter_center = (x1Start + 17, y1Start + 15)
        PlaceText(quarter_center, img)

    elif shape == 9:  # square
        cv2.rectangle(img, (x1Start, y1Start), (x1Start + 40, y1Start + 40), (b, g, r), -1)
        square_center = (x1Start + 21, y1Start + 20)
        PlaceText(square_center, img)
    elif shape == 10:  # heptagon
        contour = np.array([[x1Start, y1Start], [x1Start + 15, y1Start + 10], [x1Start + 22, y1Start + 30],
                            [x1Start + 10, y1Start + 44],
                            [x1Start - 10, y1Start + 44], [x1Start - 22, y1Start + 30], [x1Start - 15, y1Start + 10]],
                           np.int32)
        cv2.fillPoly(img, [contour], (b, g, r))  # fills in the shape.
        hep_center = (x1Start, y1Start + 20)
        PlaceText(hep_center, img)
    elif shape == 11:  # octagon
        contour = np.array([[x1Start + 15, y1Start], [x1Start + 30, y1Start + 15], [x1Start + 30, y1Start + 45],
                            [x1Start + 15, y1Start + 60],
                            [x1Start - 15, y1Start + 60], [x1Start - 30, y1Start + 45], [x1Start - 30, y1Start + 15],
                            [x1Start - 15, y1Start]], np.int32)

        cv2.fillPoly(img, [contour], (b, g, r))  # fills in the shape.
        oct_center = (x1Start, y1Start + 30)
        PlaceText(oct_center, img)
    elif shape == 12:  # star
        contour = np.array([[x1Start, y1Start], [x1Start + 52, y1Start], [x1Start + 9, y1Start + 26],
                            [x1Start + 26, y1Start - 17], [x1Start + 52, y1Start + 26], [x1Start, y1Start]], np.int32)
        contour2 = np.array([[x1Start, y1Start], [x1Start + 52, y1Start], [x1Start + 30, y1Start + 15],
                             [x1Start, y1Start]], np.int32)

        cv2.fillPoly(img, [contour], (b, g, r))  # fills in the shape.
        cv2.fillPoly(img, [contour2], (b, g, r))  # fills rest of the shape
        star_center = (x1Start + 29, y1Start + 4)
        PlaceText(star_center, img)
    elif shape == 13:  # cross
        img = cv2.rectangle(img, (x1Start, y1Start), (x1Start + 20, y1Start + 50), (b, g, r), -1)
        img = cv2.rectangle(img, (x1Start - 20, y1Start + 20), (x1Start + 40, y1Start + 33), (b, g, r), -1)
        rect_center = (x1Start + 12, y1Start + 25)
        PlaceText(rect_center, img)

        # placing text at the center of the shape

    # trying to not kill my computer
    time.sleep(0.1)
    return img


if __name__ == '__main__':
    path = r'D:\Pycharm Projects\Pycharm Data Processing\Fields\Grass_Field.jpg'
    img = cv2.imread(path)
    img = cv2.resize(img, (1920, 1080))

    img = DrawShapeOntoImage(img)
    # Show image
    cv2.imshow('image', img)
    cv2.waitKey(0)
# TODO: create more shapes and find more fields to finish data set
