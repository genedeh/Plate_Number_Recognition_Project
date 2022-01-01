import os

from Src.number_plate_detection import plate_number_detection


def test_correct_return_value():
    result = plate_number_detection("Test_Image/Image(2).jpg")
    assert "LSR 542GE" == result


def test_no_plate_number():
    result = plate_number_detection("Test_Image/Image(4).png")
    assert "NO PLATE_NUMBER DETECTED" == result


def test_result_if_saved():
    path_exists = os.path.exists("./Result.png")
    assert True == path_exists


def test_result_overlay_if_saved():
    path_exists = os.path.exists("./output/FINAL RESULT_overlay.jpg")
    assert True == path_exists
