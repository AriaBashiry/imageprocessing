import cv2

img = cv2.imread("drop.png", 0)
print(img)
cv2.imshow('rain_drop',img)

key = cv2.waitKey(0) & 0xFF

if key == ord('q'):
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('drop_copy.png', img)