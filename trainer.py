#Face Recognition
#Created by Ariel Roque

import os
import cv2
import numpy as np
from PIL import Image

def getImagesWithID(path):
	images_path = [os.path.join(path,i) for i in os.listdir(path)]
	
	faces = []
	IDs = [] 
	
	for image_path in images_path:
		img  = Image.open(image_path).convert("L")
		
		face_array = np.array(img,"uint8")
		
		ID = int(os.path.split(image_path)[-1].split(".")[1])
		
		faces.append(face_array)
		IDs.append(ID)
		
		cv2.imshow("Training",face_array)
		cv2.waitKey(10)
		
	return np.array(IDs),faces
		
recognizer = cv2.face.LBPHFaceRecognizer_create()

if(not os.path.exists("recognizer")):
	os.makedirs("./recognizer")

PATH = "dataset"

IDs, faces = getImagesWithID(PATH)

recognizer.train(faces,IDs)
recognizer.save("recognizer/trainingData.yml")

cv2.destroyAllWindows()
	
	
	
	
