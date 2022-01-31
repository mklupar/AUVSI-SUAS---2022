# Crops image from fields folder and puts them into cropped fields folder.
import numpy as np
import cv2
import glob
import os


def NormImgSize(image, size=(1920, 1080)):
    return cv2.resize(image, size)  # resize the image


if __name__ == '__main__':
    path = r'D:\Pycharm Projects\Pycharm Data Processing\Fields\Grass Field.jpg'
    img = cv2.imread(path)

    img = NormImgSize(img)
    # Show image and save them to the DataSet folder
    cv2.imshow('image', img)

