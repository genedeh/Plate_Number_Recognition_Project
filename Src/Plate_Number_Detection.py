import os
import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image


class Plate_Number_Detection:
    def __init__(self, image_path: str, width: int, height: int, tesseract_cmd: str, result_image_type: str):
        self.width = width
        self.height = height
        self.tesseract_cmd = rf"{tesseract_cmd}"
        self.idx = 7
        self.screen_contour = None
        self.contours = None
        self.image1_reference = None
        self.image2_reference = None
        self.image_result = None
        self.plate_number = None
        if os.path.isfile(image_path):
            self.image_path = image_path
            self.image = cv2.imread(image_path, cv2.IMREAD_COLOR)
            if result_image_type == ".png" or result_image_type == ".jpg":
                self.result_image_type = result_image_type
            else:
                raise Exception("This Image Type Dose Not Match The Required Types")
        else:
            raise OSError("This Image Path Dose Not Exist")

    def get_contours(self):
        self.image = imutils.resize(self.image, width=self.width, height=self.height)
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)  # convert to grey scale
        gray = cv2.bilateralFilter(gray_image, 11, 17, 17)  # Blur to reduce noise
        edged_image = cv2.Canny(gray, 2, 240)  # Perform Edge detection
        self.contours, new = cv2.findContours(edged_image.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        self.image1_reference = self.image.copy()
        cv2.drawContours(self.image1_reference, self.contours, -1, (0, 255, 0), 1)
        cv2.imshow("1st Image Result", self.image1_reference)
        contours = sorted(self.contours, key=cv2.contourArea, reverse=True)[:30]
        self.image2_reference = self.image.copy()
        cv2.drawContours(self.image2_reference, contours, -1, (0, 0, 0), 2)
        cv2.imshow("2st Image Result", self.image2_reference)

    def verify_plate_number(self):
        # loop over contours
        for contour in self.contours:
            # approximate the contour
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.018 * peri, True)
            if len(approx) == 4:  # chooses contours with 4 corners
                self.screen_contour = approx
                x, y, w, h = cv2.boundingRect(contour)  # finds co-ordinates of the plate
                aspectRatio = float(w) / h
                print(aspectRatio)
                if 0.65 <= aspectRatio <= 2.02:
                    print("Not A PLate Number")
                    continue
                else:
                    print("This is a Plate Number")
                    new_img = self.image[y:y + h, x:x + w]
                    cv2.imwrite('./' + "Result" + '.png', new_img)  # stores the new image
                    self.idx += 1
                    break
            # draws the selected contour on original image
        cv2.drawContours(self.image, [self.screen_contour], -1, (0, 0, 0), 10)
        cv2.imshow("Final image with plate detected", self.image)

    def crop_image(self):
        Cropped_loc = './result.png'  # the filename of cropped image
        self.plate_number = cv2.imread(Cropped_loc)
        self.plate_number = cv2.cvtColor(self.plate_number, cv2.COLOR_BGR2GRAY)
        _, self.image_result = cv2.threshold(self.plate_number, 158, 255, cv2.THRESH_BINARY)

        cv2.imshow("cropped", self.plate_number)
        cv2.imshow("Result", self.image_result)

    def check_plate_number_text(self, text: str):
        if text == "":
            text = "Plate Number Not Detected"
            return text
        else:
            return text.replace(" ", "")

    def get_plate_number_text(self):
        pytesseract.pytesseract.tesseract_cmd = self.tesseract_cmd
        text = pytesseract.image_to_string(self.image_result)
        print(f" First detection printed this: {self.check_plate_number_text(text)} / ", end=" ")
        text = pytesseract.image_to_string(self.plate_number)
        print(f" Second detection printed this: {self.check_plate_number_text(text)} / ", end=" ")
        text = pytesseract.image_to_string(self.image2_reference)
        print(f" Third detection printed this: {self.check_plate_number_text(text)} / ", end=" ")
        text = pytesseract.image_to_string(self.image1_reference)
        print(f" Fourth detection printed this: {self.check_plate_number_text(text)} / ", end=" ")


PND = Plate_Number_Detection("Test_Area/Test_Image/Image(5).jpg", 500, 500, r"C:\Users\KidChaos\AppData\Local\Programs"
                                                                            r"\Tesseract-OCR\tesseract.exe", ".png")
PND.get_contours()
PND.verify_plate_number()
PND.crop_image()
PND.get_plate_number_text()
cv2.waitKey(0)
cv2.destroyAllWindows()
