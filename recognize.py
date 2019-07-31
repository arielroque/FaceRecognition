#Face Recognition
#Created by Ariel Roque

import sqlite3
import cv2
import os
import tkinter.messagebox

DATABASE_NAME = "database.db"
TRAIN_DATA_PATH = "recognizer/trainingData.yml"
FACE_CASCADE_PATH = "cascade/haarcascade_frontalface_default.xml"

conn = sqlite3.connect(DATABASE_NAME)
c = conn.cursor()

if (not os.path.isfile(TRAIN_DATA_PATH)):
	tkinter.messagebox.showerror("Error", "Please record face before using this function")
	exit(0)

face_cascade = cv2.CascadeClassifier(FACE_CASCADE_PATH)

webcam  = cv2.VideoCapture(0)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(TRAIN_DATA_PATH)

while(True):
	
	r, video = webcam.read()
	gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
	
	faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.3,minNeighbors = 10, minSize = (30,30), maxSize = (400,400))
	
	for (x,y,w,h) in faces:
		cv2.rectangle(video,(x,y),(x+w,y+h),(0,255,0),2) # video | top left coordinate | bottom right coordinate | color | thickness
		ID,conf = recognizer.predict(gray[y:y+h,x:x+w])
		
		c.execute("SELECT name FROM users WHERE id = (?);",(ID,))
		
		result = c.fetchall()
		
		name = result[0][0]
		
		if (conf < 50):
			cv2.putText(video, name , (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX,1,(150,255,0),2) # video , text , cordinate , font , scale, color, thickness
		else:
			cv2.putText(video, "No match", (x+2, y+h-5),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255,2))
	
	cv2.imshow("Face Recognize", video)
	
	#Exit press "q"
	if (cv2.waitKey(1000 // 12) & 0xff == ord("q")):
		break

webcam.release()
cv2.destroyAllWindows()

		
		
	




	
	
