#Face Recognition
#Created by Ariel Roque

from tkinter import *
from subprocess import call
import tkinter.messagebox
import cv2
import sqlite3
import os

DATABASE_NAME = "database.db"
DATASET_PATH = "dataset"
TRAIN_FACE_PATH =  "features/trainer.py"
FACE_CASCADE_PATH = "cascade/haarcascade_frontalface_default.xml"

def get_last_photo_number(id_user):
	files = os.listdir(DATASET_PATH)
	
	last_number = 0
	
	for i in files:
		p = i.split(".")[1]
		
		if (int(p) == id_user):
			last_number+=1
	
	return last_number
	

def search_user(name):
	
	name = name.lower()
	
	conn = sqlite3.connect(DATABASE_NAME)
	c = conn.cursor()
	
	c.execute("SELECT id FROM users WHERE name = (?);",(name,))
	
	result = c.fetchall()
	
	conn.commit()
	c.close()
	
	print(result)
	
	if (len(result) == 0):
		return -1
		
	return result[0][0]
	

def record_face(last_photo_number):

	face_cascade = cv2.CascadeClassifier(FACE_CASCADE_PATH)
		
	user_id = search_user(name.get())
		
	webcam = cv2.VideoCapture(0)
			
	sample_number = last_photo_number + 1
	
	gui.destroy()
		
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
			
		if ((sample_number - last_photo_number) > 25):
			break
		
	webcam.release()
	cv2.destroyAllWindows()
		
	call(["python",TRAIN_FACE_PATH])

def improve_recognition():
	user_id = search_user(name.get())
	
	if (user_id == -1):
		tkinter.messagebox.showerror("Error", "This user is not registered, try again!!")
	else:
		last_photo_number = get_last_photo_number(user_id)
		
		record_face(last_photo_number)
			
#-------------------------------------------
#             Graphic Interface
#-------------------------------------------
gui = Tk()
gui.title("User Name")
gui.geometry("300x50")

name = Entry(gui,width = 30)
name.place(x = 10,y = 13)

bt = Button(gui,text= "Ok",command = improve_recognition)
bt.place(x = 230, y = 10)

gui.mainloop()
	
#-------------------------------------------

