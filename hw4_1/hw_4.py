import cv2
import numpy as np




counter = 0
points = np.zeros((4,2), np.uint8)
img = cv2.imread('/home/timur/robot/hw4/cards.jpeg')


    
    
    
def mouse_callback(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        if counter >= 4: 
            exit() 
        points[counter] = x, y
        counter += 1




while True:
    if cv2.waitKey(1) & 0xFF == 27:
        break
    if counter == 4:
        width, height = 250, 350
        pts1 = np.float32([points[0], points[1], points[2], points[3]])
        pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        new_img = cv2.warpPerspective(img, matrix, (width, height))

        cv2.imshow('new image', new_img)
        
        

    for i in range(4):
        cv2.circle(img, (points[i][0], points[i][1]), 5, (25, 25, 25), cv2.FILLED)
        
        
        
    cv2.imshow('old image', img)
    cv2.setMouseCallback('old image', mouse_callback)
    cv2.waitKey(1)
    
cv2.destroyAllWindows()

