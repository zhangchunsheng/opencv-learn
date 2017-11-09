import numpy
import cv2

img = cv2.imread('001.jpg', 0);
cv2.imshow('image', img)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('001.png', img)
    cv2.destroyAllWindows()
