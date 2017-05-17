'''
This file was mainly created to just implement ideas as is, and test quickly.
The final product is the package called "ImageSegmenter", which contains the class "Segmenter"
'''

from PIL import Image
import numpy as np
import cv2
'''

# this code can be used for basic reading and writing,
# like only for training images 

img = Image.open("zero.png") #input image
arr = np.array(img)              #converting image to array using numpy array function

a = arr.flatten()
print(a[10000:10300])
'''

im_gray = cv2.imread('SegmentationTest2.png', 0)
# im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# smooth the image to avoid noises
im_gray = cv2.medianBlur(im_gray, 5)

# ret, thresh = cv2.threshold(im_gray, 127, 255, 0)
# Apply adaptive threshold with binary_inv
thresh = cv2.adaptiveThreshold(im_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

cv2.imshow('thresh', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# apply some dilation and erosion to join the gaps
thresh = cv2.dilate(thresh, None, iterations=3)
thresh = cv2.erode(thresh, None, iterations=2)

im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# hierarchy = hierarchy[0]  # inner list of hierarchy

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
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    # storing centroid tuple and cropped image in dictionary
    cropped[(cx, cy)] = im_gray[y:y+h, x:x+w]
    # inserting centroid tuples to a list
    centroids.append((cx, cy))

# since (0, 0) was only a placeholder
del cropped[(0, 0)]
centroids.remove((0, 0))

# sorting the centroid list
centroids.sort()

for m in centroids:
    cv2.imshow('cropped', cropped[m])
    cv2.waitKey(0)
cv2.destroyAllWindows()

'''
cv2.imshow('bounds', im_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()  # NOTE: this destroys all existing windows
'''
