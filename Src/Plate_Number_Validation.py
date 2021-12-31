import cv2
import imutils
import numpy
from Edge_Detection import EdgeDetection


class PlateNumberValidation:
    def __init__(self, image_path, screen_contour, contours):
        self.image_path = image_path
        self.image = cv2.imread(self.image_path, cv2.IMREAD_COLOR)
        self.screen_contour = screen_contour
        self.contours = contours
        self.idx = 7

    def validate_plate(self):
        global new_img
        for contour in self.contours:
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.018 * peri, True)
            if len(approx) == 4:
                self.screen_contour = approx
                x, y, w, h = cv2.boundingRect(contour)
                aspectRatio = float(w) / h
                print(f"Poly : {approx}")
                print(aspectRatio)
                if aspectRatio <= 1.414:
                    print("Not A PLate Number")
                    continue
                else:
                    print("This is a Plate Number")
                    new_img = self.image[y:y + h, x:x + w]
                    self.idx += 1
                    break
            else:
                print(f"Not Poly : {approx}")
                continue
        cv2.drawContours(self.image, [self.screen_contour], -1, (255, 255, 255), 10)
        cv2.imshow("Final image with plate detected", self.image)
        return new_img


edge_detection = EdgeDetection("Test_Area/Test_Image/Image(1).jpg", (0, 255, 0), (255, 255, 0))
result = edge_detection.full_edge_detection()
screen_contour1 = result[0]
contour1 = result[1]
validation = PlateNumberValidation("Test_Area/Test_Image/Image(1).jpg", screen_contour1, contour1)
validation.image = imutils.resize(validation.image, width=500, height=500)
validation.validate_plate()
cv2.waitKey(0)
cv2.destroyAllWindows()
