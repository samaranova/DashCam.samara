import os
from cv2 import cv2

#start recording
#stop recording and save
#if new date, make a directory for that day
#if starting new recording on same day, save video to same file

filename = 'video.mp4' #avi
frames = 20.0 #set the frame rate
resolut = '720p' #set the resolution


def change_res(recording, width, height):
    recording.set(3, width)
    recording.set(4, height)

#Dictionary of possible video dimensions
STD_DIMENSIONS = {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p:": (1920, 1080),
    "4k": (3840, 2160),
}

def getDims(recording, res='1080p'):
    width, height = STD_DIMENSIONS['480p']
    if res in STD_DIMENSIONS:
        width, height = STD_DIMENSIONS[res]
    change_res(recording, width, height)
    return width, height

//Codecc, mp4 will throw a warning, but still works
VIDEO_TYPE = {
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
}

def getVidType(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return VIDEO_TYPE[ext]
    return VIDEO_TYPE['mp4']



recording = cv2.VideoCapture(0) #value '0' means camera is recording from default computer camera
dims = getDims(recording, res=resolut)
vidType = getVidType(filename)

out = cv2.VideoWriter(filename, vidType, frames, dims) #(width, height)
#Opens the window that shows the recording
while(True):
    ret, frame = recording.read()
    out.write(frame)
    #Displays the frame
    cv2.imshow('frame', frame)

    #How to stop the recording manually
    if cv2.waitKey(20) & 0xFF == ord('q'): #to stop recording press q
        break

recording.release()
out.release()
cv2.destroyAllWindows()

