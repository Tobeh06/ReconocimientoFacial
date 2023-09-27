import cv2
import os
import numpy as np

dataPath = 'C:/Users/VICTUS/Desktop/UPDS/INTELIGENCIA ARTIFICIAL - ING. ZAMBRANA/ReconocimientoFacial/Data' #Cambia a la ruta donde hayas almacenado Data
peopleList = os.listdir(dataPath)
print('Lista de personas: ', peopleList )

labels = []
facesData = []
label = 0

for nameDir in peopleList:
    personPath = dataPath + '/' + nameDir
    print('leyendo las imagenes...')

    for fileName in os.listdir(personPath):
        print('Rostros: ', nameDir + '/' + fileName)
        labels.append(label)
        facesData.append(cv2.imread(personPath+'/'+fileName,0))
        image = cv2.imread(personPath+'/'+fileName,0)
        #cv2.imshow('image',image)
        #cv2.waitKey(10)
    label = label + 1 





face_recognizer = cv2.face.EigenFaceRecognizer_create()


print("Entrenando...")
face_recognizer.train(facesData, np.array(labels))


face_recognizer.write('modeloEigenFace.xml')
print("Entrenamiento finalizado")