import cv2

def take_snapshot():
    video_capture_object = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = video_capture_object.read()
        cv2.imwrite("new picture.jpg",frame)
        result = False
    video_capture_object.release()
    cv2.destroyAllWindows()

take_snapshot()