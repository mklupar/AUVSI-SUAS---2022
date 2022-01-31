import os
import cv2
from TestCrop import NormImgSize
from TestDraw import DrawShapeOntoImage
from pathlib import Path


def main(Field_Directory: Path, Data_Set_Directory: Path):
    Data_Set_Directory.mkdir(parents=True, exist_ok=True)
    fieldImgPaths = os.listdir(Field_Directory)

    for index, filename in enumerate(fieldImgPaths, start=1):
        filepath = str(Field_Directory / filename)

        img = cv2.imread(filepath)
        croppedImg = NormImgSize(img)
        finalImg = DrawShapeOntoImage(croppedImg)

        DestinationPath = str(Data_Set_Directory / f'Copy{index}.jpg')
        cv2.imwrite(DestinationPath, finalImg)

if __name__ == '__main__':
    main(Path(r'D:\Pycharm Projects\Pycharm Data Processing\Fields'), Path(r'D:\Pycharm Projects\Pycharm Data Processing\DataSet'))