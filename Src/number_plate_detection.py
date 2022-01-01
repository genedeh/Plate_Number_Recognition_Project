import cv2
import os
import imutils
from Src.plate_number_image_to_text import overlay_ocr_text


def plate_number_detection(image_path):
    if os.path.exists(image_path):
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        image = imutils.resize(image, width=500, height=200)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17)
        edged_image = cv2.Canny(gray_image, 2, 240)
        contours, new = cv2.findContours(edged_image.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        image1 = image.copy()
        cv2.drawContours(image1, contours, -1, (0, 255, 0), 1)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]
        screen_contour = None
        image2 = image.copy()
        cv2.drawContours(image2, contours, -1, (0, 0, 0), 2)
        idx = 7
        for contour in contours:
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.018 * peri, True)
            if len(approx) == 4:
                screen_contour = approx
                x, y, width, height = cv2.boundingRect(contour)
                aspectRatio = float(width) / height
                if 0.65 <= aspectRatio <= 2.02:
                    break
                else:
                    new_img = image[y:y + height, x:x + width]
                    cv2.imwrite('./' + "Result" + '.png', new_img)
                    idx += 1
                    break
        cv2.drawContours(image, [screen_contour], -1, (0, 0, 0), 10)

        Cropped_location = './result.png'
        plate_number = cv2.imread(Cropped_location)
        gray_plate_number = cv2.cvtColor(plate_number, cv2.COLOR_BGR2GRAY)
        _, result = cv2.threshold(gray_plate_number, 158, 255, cv2.THRESH_BINARY)

        try:
            final_result = overlay_ocr_text(image_path, "FINAL RESULT")
            if final_result is None:
                return "NO PLATE_NUMBER DETECTED"
            else:
                return final_result
        except TypeError:
            pass
    else:
        raise OSError(f"{image_path} DOSE NOT EXIST IN YOU CURRENT WORKING DIRECTORY")


result = plate_number_detection("Test_Area/Test_Image/Image(2).jpg")
# if result == "LSR 542GE":
#     print("PASSED")

cv2.waitKey(0)
cv2.destroyAllWindows()
