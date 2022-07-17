import cv2
import os
import variable
extractFolderName = "ExtractedImages"
videoExtension = ['.avi','.mp4']
extractedPath = ""
fileName = ""

def main():
    #Check video file if exist
    currentDir = os.getcwd()
    for file in os.listdir(currentDir):
        if os.path.splitext(file)[1] in videoExtension:
            extractedPath = os.path.join(extractFolderName,file)
            fileName = file
            break
        
    #Make dir
    os.makedirs(extractedPath,exist_ok=True)
    #Check video path
    if os.path.exists(extractedPath):
        print("Reading video:...")
        vid = cv2.VideoCapture(fileName)
        count = 0
        while True:
            ret,frame = vid.read()
            count += 1
            if ret:
                #Get file name
                imageName = f"Images_{count}.PNG"
                imagePath = os.path.join(extractedPath,imageName)

                #Write to disk
                cv2.imwrite(imagePath,frame)
                print(f"Extracting file: {imageName} to disk")
                if cv2.waitKey(30) & 0xFF == ord("q"):
                    break
            else:
                print("Reach the last frame of video")
                print(f"File count: {count}")
                break
    else:
        raise Exception("Path is not existed!")
    cv2.destroyAllWindows()
    vid.release()
if __name__ == "__main__":
    main()