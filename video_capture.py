import cv2
import time

def process_webcam():
    '''
    Return:
    check: if the video was properly opened
    frame: the current image of webcam
    '''

    # Create an video object
    webcam_video = cv2.VideoCapture(2) # the parametetr needs to be changed depending on which device 
                                       # this script is running


    check, frame = webcam_video.read()

    
    print(check)
    print(frame)

    
    # cv2.imshow("Video Capture!", frame)
    
    # key = cv2.waitKey(1)
        
    # Shutdown the cam
    webcam_video.release()

    cv2.destroyAllWindows

    return check, frame