#Face Recognition
#Created by Ariel Roque

from tkinter import *
import sqlite3
from subprocess import call
import os

DATABASE_NAME = "database.db"
RECORD_FACE_PATH = "./record_face.py"
RECOGNIZE_FACE_PATH = "./recognize.py"

def call_record_face():
	global RECORD_FACE_PATH
	call(["python", RECORD_FACE_PATH])

def call_recognize_face():
	global RECOGNIZE_FACE_PATH
	call(["python",RECOGNIZE_FACE_PATH])


def prepare_database():
	folders = os.listdir()
	
	if(DATABASE_NAME not in folders):
		conn = sqlite3.connect(DATABASE_NAME)
		c = conn.cursor()
		
		sql = """CREATE TABLE users(
		          id integer unique primary key autoincrement,
		           name text)
		      """
		c.executescript(sql)
		conn.commit()
		conn.close()

#-------------------------------------------
#             Graphic Interface
#-------------------------------------------
gui = Tk()
gui.title("Face Recognition")
gui.geometry("250x250")
gui.resizable(width=False,height=False)

record_face = Button(gui,text = "    Record Face    ",command = call_record_face)
record_face.place(x = 50,y = 40)

recognize_face = Button(gui,text = "   Recognize Face  ", command = call_recognize_face)
recognize_face.place(x = 50,y = 80)

improve_recognition = Button(gui,text = "Improve Recognition")
improve_recognition.place(x = 50, y = 120)

prepare_database()

gui.mainloop()
#-------------------------------------------
