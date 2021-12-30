import cv2
import os
import imutils


class EdgeDetection:
    def __init__(self, image_path: str, line_color: tuple, line_color2: tuple, line_thickness=1):
        self.line_thickness = line_thickness
        if os.path.isfile(image_path):
            self.image_path = image_path
            self.image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        else:
            print("This Image Path Dose Not Exist")
        if len(line_color) == 3 and len(line_color2) == 3:
            self.line_color = line_color
            self.line_color2 = line_color2
        else:
            print("This Color Code Is Incorrect")

    def resize(self, width=500, height=500):
        self.image = imutils.resize(self.image, width=width, height=height)

    def first_edge_detection(self):
        self.resize()
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        bilateral_filter_gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17)
        edged_image = cv2.Canny(bilateral_filter_gray_image, 2, 240)
        contours, new = cv2.findContours(edged_image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        image = self.image.copy()
        cv2.drawContours(image, contours, -1, self.line_color, self.line_thickness)
        cv2.imshow("Edges Detected", image)
        return contours

    def full_edge_detection(self):
        contours = self.first_edge_detection()
        new_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]
        screenContour = None
        new_image = self.image.copy()
        cv2.drawContours(new_image, new_contours, -1, self.line_color2, self.line_thickness)
        cv2.imshow("img2", new_image)

        return screenContour, contours


edge_detection = EdgeDetection("Test_Image/Image(3).png", (0, 255, 0), (255, 255, 0))
edge_detection.full_edge_detection()
cv2.waitKey(0)
cv2.destroyAllWindows()
