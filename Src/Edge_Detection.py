import cv2
import os
import imutils


class EdgeDetection:
    def __init__(self, image_path: str, line_color: tuple):
        if os.path.isfile(image_path):
            self.image_path = image_path
            self.image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        else:
            print("This Image Path Dose Not Exist")
        if len(line_color) == 3:
            self.line_color = line_color
        else:
            print("This Color Code Is Incorrect")

    def resize(self, width=500, height=200):
        self.image = imutils.resize(self.image, width=width, height=height)
