#importación de librerias
import pickle
import cv2
import mediapipe as mp
import numpy as np

#==================== PATH y nombres de los dos modelos creados =============================#

model_dict2 = pickle.load(open('./model2.p', 'rb'))
model2 = model_dict2['model']

model_dict1 = pickle.load(open('./model1.p', 'rb'))
model1 = model_dict1['model']

#============================================================================================#

#Se indica la camara a capturar
cap = cv2.VideoCapture(0)

#Se inicializa mediapipe para detectar y dibujar las conexiones de las manos.
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2,min_detection_confidence=0.3)

#Json de las palabras e indez de las señas a 2 manos
labels_dict2 = {
  0: "Buenos días",
  1: "Gracias",
  2: "¿Como estas?",
  3: "Blanco",
  4: "Azul",
  5: "Negro",
  6: "Verde",
  7: "Amarillo",
  8: "Trabajo",
  9: "Cine",
  10: "Salon",
  11: "Tienda",
  12: "Playa",
  13: "Hospital",
  14: "Cafetería",
  15: "Parque",
  16: "Maestro",
  17: "Hermano",
  18: "Abuelo",
  19: "Primo",
  20: "Amigo",
  21: "Vecino",
  22: "Tio",
  23: "¿como?",
  24: "¿cual?",
  25: "¿cuantos?",
  26: "¿donde?",
  27: "¿quien?",
  28: "¿por?",
  29: "Ir",
  30: "Dar",
  31: "Piña",
  32: "Platano",
  33: "Durazno",
  34: "Leche",
  35: "Tostada",
  36: "Carne",
  37: "Pan",
  38: "Tortilla",
  39: "Porfavor",
  40: "Tamales",
  41: "Arroz",
  42: "Tacos",
  43: "Esquite",
  44: "Chicharron",
  45: "Refresco",
  46: "Ganso",
  47: "Mariposa",
  48: "Caracol",
  49: "Vaca",
  50: "Burro"
}
#Json de las palabras e indez de las señas a 1 manos
labels_dict1 = {
0: "AAA",
1: "BBBBB",
2: "C",
3: "D",
4: "E",
5: "F",
6: "G",
7: "H",
8: "I",
9: "J",
10: "K",
11: "L",
12: "M",
13: "N",
14: "ENE",
15: "O",
16: "P",
17: "Q",
18: "R",
19: "S",
20: "T",
21: "U",
22: "V",
23: "W",
24: "X",
25: "Y",
26: "Z",
27: "0",
28: "1",
29: "2",
30: "3",
31: "4",
32: "5",
33: "3",
34: "7",
35: "8",
36: "9",
37: "10",
38: "Hola",
39: "Adios",
40: "De nada",
41: "Soy / Yo",
42: "Hoy",
43: "¿Que?",
44: "Feliz",
45: "Triste",
46: "Enojado",
47: "Comer",
48: "Quere",
49: "Tener",
50: "Soñar",
}

while True:

    
    #Try catch para atrapar la exepción cunado no se reconosca una seña
    try:
        #Creacióde arreglos que guardaran las coordenadas
        data_aux = []
        x_ = []
        y_ = []

        ret, frame = cap.read()

        H, W, _ = frame.shape

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.rectangle(frame, (0, 0), (120, 30), (255,255,255), -1)
        cv2.putText(frame, 'Q=salir', (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2,
                    cv2.LINE_AA)

        #por cada mano detectada extraer las coordenadas
        results = hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,  
                    hand_landmarks,  
                    mp_hands.HAND_CONNECTIONS,  
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

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

            x1 = int(min(x_) * W) - 10
            y1 = int(min(y_) * H) - 10

            x2 = int(max(x_) * W) - 10
            y2 = int(max(y_) * H) - 10

            #Cuando se identifique 1 mano se lee el modelo y Json apropiados
            if (len(results.multi_hand_landmarks)==2):
                prediction = model2.predict([np.asarray(data_aux)])
                predicted_character = labels_dict2[int(prediction[0])]
       
            #Cuando se identifique 2 mano se lee el modelo y Json apropiados
            else:
                prediction = model1.predict([np.asarray(data_aux)])
                predicted_character = labels_dict1[int(prediction[0])]
            
            print(predicted_character, len(predicted_character))
            
            #Se coloca la traducción literal en la pantalla
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
            cv2.rectangle(frame, (x1, y1-50), (x1+(len(predicted_character)*30), y1), (255, 255, 255), -1)
            cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                        cv2.LINE_AA)
    except Exception as error:
        #Si no se reconoce una seña se pone "No reconocido"
        predicted_character = "No Reconocido"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
        cv2.rectangle(frame, (x1, y1-50), (x2+len(predicted_character)*100, y1), (255, 255, 255), -1)
        cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                        cv2.LINE_AA)
    
    cv2.imshow('Frame',frame)
    #Al precionar 'q' se detiene el proceso
    if cv2.waitKey(25) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
