import cv2
import numpy as np
img = cv2.imread("flower.jpg", 1)

print(img.shape)
arr = np.asarray(img,np.uint8)
print(arr)


# for i in arr:
#     if i == [3,14,245]:
#         i = [255,176,5]

while True:
    re = [3,14,245]
    out = [255,176,5]
    if re in img:
        for i in range(2):
            re[0] = out[0]
            re[1] = out[1]
            re[2] = out[2]

    cv2.imshow('image', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


