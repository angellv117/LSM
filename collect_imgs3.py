# importación de las librerias
import os
import cv2
import mediapipe as mp

# path de los directorios en los que se guararan las señas
DATA_DIR = './1mano'
#DATA_DIR = './2manos'

# Creación de la carpeta si no existe
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Varibales de número de señas a detectar, número de fotos y número de carpeta
number_of_classes = 2
dataset_size = 50
cont = 0

# Se declara la cámara a capturar
cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.3)

# Obtenemos el ancho de la pantalla
screen_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

# Creamos las carpetas en donde se guardarán las señas
for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(cont))):
        os.makedirs(os.path.join(DATA_DIR, str(cont)))

    print('Collecting data for class {}'.format(j))

    done = False
    while True:
        ret, frame = cap.read()
        
        frame_with_connections = frame.copy()  # Copia del frame original para mostrar las conexiones
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame_with_connections,  # image to draw
                    hand_landmarks,  # model output
                    mp_hands.HAND_CONNECTIONS,  # hand connections
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
        
        cv2.putText(frame_with_connections, 'Presiona "Q" para capturar ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 3, cv2.LINE_AA)
        
        # Muestra las ventanas una al lado de la otra
        cv2.imshow('frame Guia', frame_with_connections)
        cv2.moveWindow('frame Guia', 0, 0)
        
        cv2.imshow('frame Captura', frame)
        cv2.moveWindow('frame Captura', int((screen_width/2)+350), 0)
        
        # Al presionar 'q' se procederá a tomar las señas
        if cv2.waitKey(25) == ord('q'):
            cv2.destroyAllWindows()
            break

    counter = 0
    # Ciclo en donde se tomarán las señas de 0 a dataset_size-1
    while counter < dataset_size:
        ret, frame = cap.read()

        frame2 = frame.copy()  # Copia del frame original para mostrar las conexiones
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,  # image to draw
                    hand_landmarks,  # model output
                    mp_hands.HAND_CONNECTIONS,  # hand connections
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
                
        cv2.putText(frame, 'Capturando   :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 3, cv2.LINE_AA)
        
        cv2.imshow('frame Guia', frame)
        cv2.moveWindow('frame Guia', 0,0)
        
        cv2.imshow('frame Captura', frame2)
        cv2.moveWindow('frame Captura', int((screen_width/2)+350), 0)
        
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(cont), '{}.jpg'.format(counter)), frame2)
        counter += 1
    cont += 1
    cv2.destroyAllWindows()

cap.release()
cv2.destroyAllWindows()
