import cv2
import argparse
import os
from datetime import datetime
import variable
import platform

"""Parameter"""
fps = variable.fps
#Folder name
folderName = "RecordedVideos"

#Check camera
def camNumberCheck(camid):
    if int(camid) == 0:
        print(f"Start with camera number {camid}")
    elif int(camid) == 1:
        print(f"Start with camera number {camid}")
    else:
        raise Exception("Over camera allowance!")

#Choose quality
def cameraQuality(quality):
    if quality == "sd":
        print(f"Quality Video is SD")
        return 480,640
    elif quality == "hd":
        print(f"Quality Video is HD")
        return 720,960
    elif quality == "fhd":
        print(f"Quality Video is Full HD")
        return 1080,1920
    else:
        raise Exception("Over camera allowance!")
#Argparse
ap = argparse.ArgumentParser()
ap.add_argument("-camid","--camid",default=0,help="Camera number")
ap.add_argument("-q","--quality",default="sd",help="Camera number")
AgrPar = ap.parse_args()
camNumber = AgrPar.camid
camNumberCheck(camNumber)
height,width = cameraQuality(AgrPar.quality)

#Camera setting
pf = platform.uname()
if pf.system == 'Linux':
    vid = cv2.VideoCapture(int(camNumber))
elif pf.system == "Windows":
    vid = cv2.VideoCapture(int(camNumber),cv2.CAP_DSHOW)
vid.set(cv2.CAP_PROP_FRAME_WIDTH,width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

#Video Writer object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# Create datetime
now = datetime.now()
time = now.strftime("%H%M%S")

def main():
    #Create new folder
    os.makedirs(folderName,exist_ok=True)
    videoName = f"Video_{time}.avi"
    videoPath = os.path.join(folderName, videoName)
    writer = cv2.VideoWriter(videoPath, fourcc, fps, (width,height))

    while True:
        ret, frame = vid.read()
        if ret:
            #Show image
            writer.write(frame)
            cv2.imshow("Video", frame)
            #Wait for user
            key = cv2.waitKey(50)
            if key == ord("q"):
                print("Exit program and save video")
                break
        else:
            raise Exception("No found camera!")
            
    cv2.destroyAllWindows()
    vid.release()
    writer.release()
if __name__ == "__main__":
    main()
