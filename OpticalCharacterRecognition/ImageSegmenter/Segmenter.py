'''
This is the final package.
Import this file by: from ImageSegmenter import Segmenter as Seg
then calling the constructor as Seg.Segmenter('filename.png')

e.g.: S = Seg.Segmenter('test2.png')
'''

import numpy as np
import cv2


class Segmenter:
    def __init__(self, filename='input.png'):
        '''
        Constructor
        '''
        self.im_gray = cv2.imread(filename, 0)

    def segment(self):
        self.im_gray = cv2.medianBlur(self.im_gray, 5)
        # Apply adaptive threshold with binary_inv
        thresh = cv2.adaptiveThreshold(self.im_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
        # apply some dilation and erosion to join the gaps
        thresh = cv2.dilate(thresh, None, iterations=3)
        thresh = cv2.erode(thresh, None, iterations=2)
        # finding contours
        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        '''
        cropped is a dictionary with (cx, cy) centroid tuples as keys, and cropped images as values
        centroids is a list of the same centroid tuples, (cx, cy)
            - This was done because it was not possible to sort the dictionary directly using tuples as keys using the sort(dict)
              function.
            - Instead, (cx, cy) was stored in the centroids list, and the list in turn was sorted using centroids.sort().
            - The list is then iterated upon to get tuples in order...
            - Each tuple iterated upon acts as a key for the dictionary, fetching the cropped images in order

        '''
        cropped = {(0, 0): '0'}
        centroids = [(0, 0)]

        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            # finding centroid coordinates, so that it can be the basis of sorting cropped images
            M = cv2.moments(cnt)
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            # storing centroid tuple and cropped image in dictionary
            cropped[(cx, cy)] = self.im_gray[y:y + h, x:x + w]
            # inserting centroid tuples to a list
            centroids.append((cx, cy))

        # since (0, 0) was only a placeholder
        del cropped[(0, 0)]
        centroids.remove((0, 0))

        # sorting the centroid list
        centroids.sort()

        segments = []
        for c in centroids:
            segments.append(cropped[c])
        return segments
