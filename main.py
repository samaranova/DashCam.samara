from multiprocessing import Process
from cv2 import cv2
import numpy as np
import time
import threading


def face_scan(cam_name, cam_num):
    cv2.namedWindow(cam_name)
    camera = cv2.VideoCapture(cam_num)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    if camera is None or not camera.isOpened():
        cv2.destroyWindow(cam_name)
        print(f"{cam_name} is not functioning")
        return

    while True:
        success, image = camera.read()
        # delete line under this if not testing, this flips image 180
        image = cv2.flip(image, 0)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(image_gray, 1.1, 4)

        for (x, y, w, h) in faces:
            target = int((x + x + w) / 2)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.imshow(cam_name, image)

        if cv2.waitKey(2) == ord("q"):
            cv2.destroyWindow(cam_name)
            break

class scan_thread(threading.Thread):
    def __init__(self, cam_name, cam_num):
        threading.Thread.__init__(self)
        self.cam_name = cam_name
        self.cam_num = cam_num
    def run(self):
        print(f"Starting Cam #{self.cam_num}\n")
        face_scan(self.cam_name, self.cam_num)


if __name__ == '__main__':
    #Process(target = face_scan(0)).start()
    #Process(target = face_scan(1)).start()
    thread1 = scan_thread("Street Cam", 0)
    thread2 = scan_thread("Face Cam", 1)
    
    thread1.start()
    thread2.start()
    
    print("Active threads", threading.activeCount())
