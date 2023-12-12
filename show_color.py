import cv2

img = cv2.imread("flower.jpg")
points = []

def mouseevent(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(img[x,y])
        print(x,y)
        cv2.putText(img, text, (x+2,y), font, 0.6, (255, 255, 255), 2)
        cv2.circle(img, (x,y), 5, (255,255,255,), -1) 
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img,points[-1],points[-2],(0,255,255),2)
        cv2.imshow('image', img)
        print(points)


cv2.imshow('image', img)

cv2.setMouseCallback('image', mouseevent)

cv2.waitKey(0)
cv2.destroyAllWindows()
