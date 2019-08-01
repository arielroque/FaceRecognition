#Face Recognition
#Created by Ariel Roque

from tkinter import *
import sqlite3
import cv2
import os
from subprocess import call

DATABASE_NAME = "database.db"
DATASET_PATH = "dataset"
FACE_CASCADE_PATH = "cascade/haarcascade_frontalface_default.xml"
TRAIN_FACE_PATH =  "features/trainer.py"

def get_user_id(name):
	conn = sqlite3.connect(DATABASE_NAME)
	
	c = conn.cursor()
	c.execute("INSERT INTO users (name) VALUES (?)", (name,))
	user_id = c.lastrowid
	
	conn.commit()
	c.close()
	
	return user_id	


def record_face():
	global name
	if ((name.get().strip()) != ""):
		
		if (not os.path.exists(DATASET_PATH)):
			  os.makedirs(DATASET_PATH)
		
		face_cascade = cv2.CascadeClassifier(FACE_CASCADE_PATH)
		
		user_id = get_user_id(name.get())
		
		webcam = cv2.VideoCapture(0)
		
		gui.destroy()
		
		sample_number = 0
		
		while(True):
			r,video = webcam.read()
			gray = cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
			faces = face_cascade.detectMultiScale(gray,1.3,5) #video|scaleFactor|neighbors
		
			for (x,y,w,h) in faces:
				sample_number+=1
				
				cv2.imwrite("dataset/User."+str(user_id)+"."+str(sample_number)+".jpg",gray[y:y+h,x:x+w])
				cv2.rectangle(video,(x,y),(x+w,y+w),(0,255,0),2)
				
			cv2.imshow("Capturing Face",video)
			cv2.waitKey(1)
			
			if (sample_number > 25):
				break
		
		webcam.release()
		cv2.destroyAllWindows()
		
		call(["python",TRAIN_FACE_PATH])
		
#-------------------------------------------
#             Graphic Interface
#-------------------------------------------
gui = Tk()
gui.title("User Name")
gui.geometry("300x50")

name = Entry(gui,width = 30)
name.place(x = 10,y = 13)

bt = Button(gui,text= "Ok",command = record_face)
bt.place(x = 230, y = 10)

gui.mainloop()
	
#-------------------------------------------
