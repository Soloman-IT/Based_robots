import cv2
import matplotlib.pyplot as plt



def changed(columns, rows, dividers, original, lst):
    for i in range(0, rows):
        for j in range(0, columns):
            dx = dividers[0]
            dy = dividers[1]
            hx0 = dx * j
            hx1 = dx * (j + 1)
            hy0 = dy * i
            hy1 = dy * (i + 1)
            img = original[hy0:hy1, hx0:hx1]
            
            
            lst[i][j] = img
    return lst


def show(columns, rows, lst):
    fig, ax = plt.subplots(nrows=rows, ncols=columns)
    for i in range(0, rows):
        for j in range(0, columns):
            img = lst[i][j]
            ax[i,j].imshow(img)
            ax[i,j].axis('off')


    plt.tight_layout()
    plt.show()

def main():
    imgPath = "putin.jpg"
    original = cv2.imread(imgPath)

    size = original.shape

    columns = 3 
    rows = 2 
    dividers = (int(size[1]/columns), int(size[0]/rows)) 

    lst = [[0, 0, 0], [0, 0, 0]]
    
    res = changed(columns, rows, dividers, original, lst)
    show(columns, rows, res)
    

if __name__ == "__main__":
    main()