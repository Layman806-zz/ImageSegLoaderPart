'''
Testing the "ImageSegmenter" package from this file  
'''
import cv2
from ImageSegmenter import Segmenter as Seg


S = Seg.Segmenter('SegmentationTest2.png')
segments = S.segment()

for s in segments:
    cv2.imshow('segment', s)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
