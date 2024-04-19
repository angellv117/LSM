#Importacioón de las librerias
import os
import pickle
import mediapipe as mp
import cv2
import matplotlib.pyplot as plt

#Se configuran los aspexctos de mediapipe el modo en no estatico y maximas manos en 2 asi como 
# el umbral de confianza  
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.3)

#==================== PATH y nombres de los dos modelos a crear =============================#
#DATA_DIR = './2manos'
#nombrepicle ='data2.pickle'


DATA_DIR = './1mano'
nombrepicle ='data1.pickle'

#============================================================================================#

#Creacion de arreglos paralelos para alamacenar las etiquetas y las coordenaadas
data = []
labels = []
cont = 0

#ciclo for que iterara 
for dir_ in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
        #Creacióde arreglos que guardaran las coordenadas
        data_aux = []
        x_ = []
        y_ = []

        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        #por cada mano detectada extraer las coordenadas
        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    
                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

            
            data.append(data_aux)
            labels.append(dir_)

#Por cada directorio pulir los arreglos finales 42 para 1 mano y 84 para dos manos
print("Puliendo")
#Acortamos las listas
def igualar_longitud(listas, num):
    for i in range(len(listas)):
        if len(listas[i]) > num:
            listas[i] = listas[i][:num]
        elif len(listas[i]) < num:
            # Si la lista interna tiene menos de num elementos, puedes llenarla con un valor específico, como 0
            listas[i] += [0] * (num - len(listas[i]))

if (DATA_DIR == './1mano'):
    igualar_longitud(data, 42)
    print(data)
else:
    igualar_longitud(data,84)
    print(data)

#Se crea y se escibre la información en el archivo con extencion .pickle
f = open(nombrepicle, 'wb')
pickle.dump({'data': data, 'labels': labels}, f)
f.close()