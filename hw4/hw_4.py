import cv2
import numpy as np
import time
counter = 0
edges = np.zeros((4,2), np.uint8)
img = cv2.imread('/home/timur/PythonProjects/robotics/hw4/cards.jpeg')


    
    
    
def mouse_callback(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        if counter >= 4: 
            exit() 
        edges[counter] = x, y
        counter += 1




while True:
    if cv2.waitKey(1) & 0xFF == 27:
        break
    if counter == 4:
        width, height = 250, 350
        pts1 = np.float32([edges[0], edges[1], edges[2], edges[3]])
        pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (width, height))

        cv2.imshow('warped image', imgOutput)
        
        

    for i in range(4):
        cv2.circle(img, (edges[i][0], edges[i][1]), 5, (0, 255,0), cv2.FILLED)
        
        
        
    cv2.imshow('original image', img)
    cv2.setMouseCallback('original image', mouse_callback)
    cv2.waitKey(1)
    
cv2.destroyAllWindows()


def main():
    counter = 0
    edges = np.zeros((4,2), np.uint8)
    img = cv2.imread('/home/timur/PythonProjects/robotics/hw4/cards.jpeg')
    
    

if __name__ == "__main__":
    main()