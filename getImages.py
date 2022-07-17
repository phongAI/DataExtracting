import cv2
import argparse
from datetime import datetime
import platform
import os
import variable

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

#Check current os for feeding frame
pf = platform.uname()
if pf.system == 'Linux':
    vid = cv2.VideoCapture(int(camNumber))
elif pf.system == "Windows":
    vid = cv2.VideoCapture(int(camNumber),cv2.CAP_DSHOW)
#Autofocus mode
if variable.focus != "auto":
    vid.set(28,int(variable.focus))
vid.set(cv2.CAP_PROP_FRAME_WIDTH,width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

#Folder name
saveFolderName = "Images"

def main():
    #Create new folder if not existed
    os.makedirs(saveFolderName,exist_ok=True)

    #Loop
    while True:
        ret,frame = vid.read()
        if ret:
            cv2.imshow("Main Windows",frame)
            key = cv2.waitKey(50)
            if key ==  ord("q"):
                print("Program exit!")
                break
            elif key == ord("s"):
                now = datetime.now()
                currentTime = now.strftime("%H%M%S")
                fileName  = f"Image_{currentTime}.PNG"
                filePath = f"{saveFolderName}/{fileName}"
                try:
                    cv2.imwrite(filePath,frame)
                    print(f"Saving {fileName} to disk!")
                except:
                    print("Too fast!")
                    raise Exception("File is overlapped")
        # else:
        #     raise Exception("No found camera!")

    cv2.destroyAllWindows()
    vid.release()

if __name__ == "__main__":
    main()