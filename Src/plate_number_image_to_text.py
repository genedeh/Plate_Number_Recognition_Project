import easyocr
import matplotlib.pyplot as plt
import cv2
from Src.database import get_nigeria_plate_number_code

def recognize_text(image_path):
    """loads an image and recognizes text."""

    reader = easyocr.Reader(['en'], gpu=False)
    return reader.readtext(image_path)


def overlay_ocr_text(image_path, save_name):
    """loads an image, recognizes text, and overlays the text on the image."""
    plate_number = None
    nigeria_number_plate_codes = get_nigeria_plate_number_code()
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    dots_per_inch = 80
    figure_width, figure_height = int(image.shape[0] / dots_per_inch), int(image.shape[1] / dots_per_inch)
    plt.figure()
    figure, list_result = plt.subplots(1, 2, figsize=(figure_width, figure_height))
    list_result[0].imshow(image)
    print("....GETTING TEXT....")
    result = recognize_text(image_path)
    for (bbox, text, prob) in result:
        text_has_num = any(chr.isdigit() for chr in text)
        text = text.upper()
        splitted_text = text.split()
        if text_has_num:
            plate_number_country_code = splitted_text[0]
            if plate_number_country_code in nigeria_number_plate_codes:
                (top_left, top_right, bottom_right, bottom_left) = bbox
                top_left = (int(top_left[0]), int(top_left[1]))
                bottom_right = (int(bottom_right[0]), int(bottom_right[1]))
                cv2.rectangle(img=image, pt1=top_left, pt2=bottom_right, color=(0, 255, 0), thickness=100)
                cv2.putText(img=image, text=text, org=(top_left[0], top_left[1] - 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=10, color=(255, 0, 0), thickness=80)
                plate_number = text
                print(f"Final plate Number: {text}")
                break
            else:
                continue
        else:
            continue

    list_result[1].imshow(image)
    plt.savefig(f'./output/{save_name}_overlay.jpg', bbox_inches='tight')
    return plate_number

# overlay_ocr_text("Test_Area/Test_Image/Image(1).jpg", "FINAL RESULT")