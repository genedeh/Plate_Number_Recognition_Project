from Src.number_plate_detection import plate_number_detection


def test_correct_return_value():
    result = plate_number_detection("Test_Image/Image(2).jpg")
    assert "LSR 542GE" == result
