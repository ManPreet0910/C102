import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    video_capture_object = cv2.VideoCapture(0)
    result = True
    number = random.randint(0 - 100)

    while(result):
        ret,frame = video_capture_object.read()
        image_name = "image" + str(number) + ".png"
        cv2.imwrite(image_name, frame)
        result = False

    return image_name
    video_capture_object.release()
    cv2.destroyAllWindows()

def upload_file(image_name):
    acess_token = "sl.BqgdO_PGkLavEnUvjgx87J4QWj6ia9T6GjM4vuuODLxY49bhR5oL1utU0CotF_otEYptXbMC1UILZxOsJzdKi6a2luThC-Cc5dOGeeukIiXlrdDcVLRt3gnPA47GlVHQWPXMZa-H4lnT"
    file = image_name
    file_from = file
    file_to = "/test folder/" + (image_name)
    dbx = dropbox.Dropbox(acess_token)
    with open(file_from, "rb") as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("Files uploaded")

def main():
    while(True):
        if ((time.time() - start_time) >= 300):
            name = take_snapshot()
            upload_file(name)
main()