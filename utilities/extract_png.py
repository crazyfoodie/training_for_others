# Importing all necessary libraries 
import cv2 
import os 

# prefix,  data_save_every_n_frames are what you need to change
data_save_every_n_frames = 5
prefix = "20200619_1657_f"
# Read the video from specified path 
cam = cv2.VideoCapture(prefix+".mp4") 

try: 
# creating a folder named data 
    if not os.path.exists(prefix): 
        os.makedirs(prefix) 
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 

currentframe = 0  
while(True): 
    # reading from frame 
    ret,frame = cam.read() 
    if ret: 
        # if video is still left continue creating images 
        name = prefix + '/' +prefix+'_frame' + str(currentframe) + '.png'
        # writing the extracted images
        if currentframe % data_save_every_n_frames == 0:
            print ('Creating...' + name)
            cv2.imwrite(name, frame) 
        # increasing counter so that it will 
        # show how many frames are created 
        currentframe += 1
    else: 
        break
# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows() 