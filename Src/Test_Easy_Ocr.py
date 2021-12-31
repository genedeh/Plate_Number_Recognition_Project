import easyocr
import cv2

reader = easyocr.Reader(["en"], gpu=True)

img = cv2.imread("Test_Area/Test_Image/Image(5).jpg", cv2.IMREAD_COLOR)
result = reader.readtext(img, detail=1, paragraph=False)
print(result)
