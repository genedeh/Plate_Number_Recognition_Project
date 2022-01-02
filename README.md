# PLATE NUMBER RECOGNITION PROJECT.
## ABOUT
  This is an ocr project that detects and gets the text of a plate number image and validate it 

  you can find further results in ./result.png and in ./output/FINAL RESULT_overlay.jpg
## PACKAGES USED
  This project includes the usage of some modules and packages they are

  1) cv2
  2) os
  3) imutils
  4) easyocr
  5) matplotlib
## DEPENDENCIES
  This project need you to download the above packages to use and needs you to create a directory named "output" in your working directory.
## HOW TO USE
  ```
    from number_plate_detection import plate_number_detection
    plate_number_detection("Test_Area/Test_Image/Image(1).jpg")
    >>> ....GETTING TEXT....
     >>> Using CPU. Note: This module is much faster with a GPU.
      >>> Final plate Number: LSR 542GE
  ```
  if you want to get only the plate number run 
  ```
   from number_plate_detection import plate_number_detection
   result = plate_number_detection("Test_Area/Test_Image/Image(1).jpg") 
   >>> ....GETTING TEXT....
    >>> Using CPU. Note: This module is much faster with a GPU.
     >>> LSR 542GE 
  ```
  or you may get
  ```
   from number_plate_detection import plate_number_detection
   result = plate_number_detection("Test_Area/Test_Image/Image(4).png") 
   >>> ....GETTING TEXT....
    >>> Using CPU. Note: This module is much faster with a GPU.
     >>> NO PLATE_NUMBER DETECTED
  ```