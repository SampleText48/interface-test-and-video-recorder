        ##defining a few interface related variables

status = False
filename = ''

def clicked():
    global status
    global e
    ##global cap
    global fileName
    if not status:
        fileName = e.get()
        if fileName == '': fileName = 'recording'
        fileName = fileName + '.mp4'
        ##labelStatus.configure(text=f'{fileName} is being recorded, press Q to stop', bg='#ffbf00')
        

        cap = cv.VideoCapture(0,cv.CAP_DSHOW)
        if not cap.isOpened():
	        print('can not open')
	        exit()

        #frame_width = int(cap.get(3))
        #frame_height = int(cap.get(4))
        frame_width = int(1920)
        frame_height = int(1080)
        cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
        cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
        size = (frame_width, frame_height)
        fourcc = cv.VideoWriter_fourcc(*'DIVX')
        result = cv.VideoWriter(fileName, 
                   #0x7634706d ,
                   fourcc,
                   20.0, size)

        while True:
            ret, frame = cap.read()
            if not ret:
                print('can not read frame')
                break

		            ##exits program if q is pressed
            if cv.waitKey(1) == ord('q'):
                labelStatus.configure(text=f'{fileName} has been recorded', bg="#FFFFFF")
                cv.destroyAllWindows()
                break
		            ##records frames into file created earlier
            result.write(frame)
	
		            ##video output
            finalFrame = cv.putText(frame, 'Recording, press Q to stop', (0, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv.LINE_AA)
            cv.imshow('current recording', finalFrame)
            
        cap.release()
        status = True
    else:
        labelStatus.configure(text=f'recording complete', bg="#FFFFFF")
        status = False
 
        ##imports things for video capture and interface
from tkinter import *
from skimage.metrics import structural_similarity
import numpy as np
import cv2 as cv
import imutils
import time
root = Tk()

root.title('Name')

        ##defines interface elements
e = Entry(root)
e.pack()
e.focus_set()

label1 = Label(root)
label1.pack(side='bottom')

labelStatus = Label(root, text='Type in name of file', pady=20, bg='#FFFFFF')
labelStatus.pack()

custom_button = Button(root, text="Proceed", command=clicked)
custom_button.pack(side='bottom')

	    ##captures the webcam (webcam 1 is the built-in one, 0 is the usb)
##cap = cv.VideoCapture(0)
##if not cap.isOpened():
	##print('can not open')
	##exit()

    	##continuously reads frames from the cam
##while status:
    ##frame_width = int(cap.get(3))
    ##frame_height = int(cap.get(4))
    ##size = (frame_width, frame_height)
    ##result = cv.VideoWriter(fileName, 
                   ##cv.VideoWriter_fourcc(*'MJPG'),
                   ##30, size)
    ##while True:
	    ##ret, frame = cap.read()
	    ##if not ret:
		    ##print('can not read frame')
		    ##break

		##exits program if q is pressed
	    ##if cv.waitKey(1) == ord('q'):
		    ##break
	
		##records frames into file created earlier
	    ##result.write(frame)
	
		##video output
	    ##cv.imshow('current recording', frame)

##cap.release()
##cv.destroyAllWindows() why are you not pushing aaaaaaaaaa
root.mainloop()
