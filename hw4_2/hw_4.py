import cv2 
import numpy as np


vid_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)


frame_width = int(vid_capture.get(3))
frame_height = int(vid_capture.get(4))
frame_size = (frame_width,frame_height)
fps = 20


output = cv2.VideoWriter('/home/timur/robot/hw4_2/output_video_from_file.avi.mp4', cv2.VideoWriter_fourcc('M','J','P','G'), 20, frame_size)



while(vid_capture.isOpened()):
    # vid_capture.read() methods returns a tuple, first element is a bool 
    # and the second is frame
    ret, frame = vid_capture.read()
    if ret == True:
        # Write the frame to the output files
        output.write(frame)
    else:
        print('Stream disconnected')
        break
    
vid_capture.release()
output.release()