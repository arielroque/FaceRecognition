#Face Recognition
#Created by Ariel Roque

from tkinter import *
import sqlite3
from subprocess import call
import os

DATABASE_NAME = "database.db"


#-------------------------------------------
#          Call Recording Face script
#-------------------------------------------

def record_face():
	call(["python", "./record_face.py"])


#-------------------------------------------
#                  Database
#-------------------------------------------

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

record_face = Button(gui,text = "    Record Face    ",command = record_face)
record_face.place(x = 50,y = 40)

recognize_face = Button(gui,text = "   Recognize Face  ")
recognize_face.place(x = 50,y = 80)

improve_recognition = Button(gui,text = "Improve Recognition")
improve_recognition.place(x = 50, y = 120)

prepare_database()

gui.mainloop()
#-------------------------------------------
