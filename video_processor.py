import cv2
import time

def process_webcam(video_object):
    '''
    Return:
    check: if the video was properly opened
    frame: the current image of webcam
    '''
    check, frame = video_object.read()

    # print(check)
    print(frame)

    text = "Webcam"

    # cv2.imshow(text, frame)
    
    # key = cv2.waitKey(0)

    return check, frame, text


def draw_detection_box(img, object_name_text, probabiltiy, point_1, point_2):
    
    # TO DO: Determine color depending on the object type

    color = [255, 0, 255]
    
    box = cv2.rectangle(img, point_1, point_2, color, 4)
    
    text = object_name_text + ": {:.4f}".format(probabiltiy)

    cv2.putText(img, text, (point_1[0], point_1[1]-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    cv2.imshow(object_name_text, img)


if __name__ == "__main__":
    # Create an video object
    webcam_video = cv2.VideoCapture(2) # the parametetr needs to be changed depending on which device 
                                       # this script is running
    time = 0
    while True:
        time = time + 1

        check, frame, window_name = process_webcam(webcam_video)

        key = cv2.waitKey(1)

        if(key == ord('q')):
            webcam_video.release()
            cv2.destroyAllWindows()
            break

        if(check == True):
            draw_detection_box(frame, "Test", 0.99, (50,50), (300, 300))



print(time)
