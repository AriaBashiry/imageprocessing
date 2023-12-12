import random

import cv2
import numpy as np

img = np.zeros([400,600, 3], np.uint8)

for i in range(1,400):
    for a in range(1, 600):
        r1 = random.randint(1,255)
        r2 = random.randint(1,255)
        r3 = random.randint(1,255)
        img[i,a] = [r1,r2,r3]

print(img)

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()