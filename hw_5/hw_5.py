import cv2
import numpy as np

img = cv2.imread('/home/timur/PythonProjects/robotics/hw_5/maps.png')
points = []

def mouse_callback(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])

while True:
    if cv2.waitKey(1) & 0xFF == 27:
        break

    for i in range(len(points)):
        cv2.circle(img, (points[i][0], points[i][1]), 5, (227, 126, 255), cv2.FILLED)

    for i in range(len(points)):
        if i < len(points) - 1:
            cv2.line(img, (points[i][0], points[i][1]), (points[i+1][0], points[i+1][1]), (0, 126, 255), 4)
    cv2.imshow('maps', img)
    cv2.setMouseCallback('maps', mouse_callback)
    cv2.waitKey(1)
cv2.destroyAllWindows()