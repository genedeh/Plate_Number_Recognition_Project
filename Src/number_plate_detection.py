import cv2
import imutils
import pytesseract

img = cv2.imread('Test_Area/Test_Image/Image(8).jpg', cv2.IMREAD_COLOR)
img = imutils.resize(img, width=500, height=200)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 2, 240)
cnts, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
img1 = img.copy()
cv2.drawContours(img1, cnts, -1, (0, 255, 0), 1)
cv2.imshow("img1", img1)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
screenCnt = None
img2 = img.copy()
cv2.drawContours(img2, cnts, -1, (0, 0, 0), 2)
cv2.imshow("img2", img2)

count = 0
idx = 7
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)
    if len(approx) == 4:
        screenCnt = approx
        x, y, w, h = cv2.boundingRect(c)
        aspectRatio = float(w) / h
        print(aspectRatio)
        if 0.65 <= aspectRatio <= 2.02:
            print("Not A PLate Number")
            break
        else:
            print("This is a Plate Number")
            new_img = img[y:y + h, x:x + w]
            cv2.imwrite('./' + "Result" + '.png', new_img)
            idx += 1
            break
cv2.drawContours(img, [screenCnt], -1, (0, 0, 0), 10)
cv2.imshow("Final image with plate detected", img)

Cropped_loc = './result.png'
plate_number = cv2.imread(Cropped_loc)
gray_plate_number = cv2.cvtColor(plate_number, cv2.COLOR_BGR2GRAY)
_, result = cv2.threshold(gray_plate_number, 158, 255, cv2.THRESH_BINARY)

cv2.imshow("cropped", plate_number)
cv2.imshow("Result", result)


def check_plate_number_text(image_text: str):
    if image_text == "":
        image_text = "Plate Number Not Detected"
        return image_text
    else:
        return image_text.replace(" ", "")


pytesseract.pytesseract.tesseract_cmd = r'C:\Users\KidChaos\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(result)
print(f" (4)Number is: {check_plate_number_text(text)}")
text = pytesseract.image_to_string(plate_number)
print(f" (1)Number is: {check_plate_number_text(text)}")
text = pytesseract.image_to_string(img2)
print(f" (2)Number is: {check_plate_number_text(text)}")
text = pytesseract.image_to_string(img)
print(f" (3)Number is: {check_plate_number_text(text)}")
cv2.waitKey(0)
cv2.destroyAllWindows()
