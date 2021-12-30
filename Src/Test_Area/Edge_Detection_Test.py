from array import array

import cv2

from Src.Edge_Detection import EdgeDetection
import unittest


class EdgeDetectionTest(unittest.TestCase):
    def setUp(self):
        self.edge_detection = EdgeDetection("Test_Image/Image(3).png", (0, 255, 0), (255, 255, 0))

    def test_return_value(self):
        contours = self.edge_detection.first_edge_detection()
        self.assertEqual(type(contours), list)

    def test_full_detection_return_value(self):
        result = self.edge_detection.full_edge_detection()
        self.assertEqual(type(result), tuple)

    def test_screen_contour_return_value(self):
        result = self.edge_detection.full_edge_detection()
        self.assertEqual(result[0], None)

    def test_contours_return_value(self):
        result =  self.edge_detection.full_edge_detection()
        self.assertEqual(type(result[1]), list)

