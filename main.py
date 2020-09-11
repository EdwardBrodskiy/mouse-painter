import cv2
from converter import *

image_name = "space-invader.jpg"  # input('Enter file name: ')

image_cv2 = cv2.imread(f'imgs/{image_name}')

convert(image_cv2, size=50)

# cv2.imshow("Result display", image_cv2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
