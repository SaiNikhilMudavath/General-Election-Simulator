import cv2

image = cv2.imread('templates/collage2.jpg')

cv2.imshow('Image', image)
points = []

def select_points(event, x, y, flags, param):
    global points

    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow('Image', image)

cv2.setMouseCallback('Image', select_points)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Coordinates of the selected points:", points)
