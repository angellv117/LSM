# LSM 
Descripción:

SignLangTranslate es un proyecto de software desarrollado en Python que utiliza inteligencia artificial y visión por computadora para traducir en tiempo real el lenguaje de señas a texto o voz. Esta aplicación tiene como objetivo mejorar la comunicación entre personas con discapacidad auditiva y personas que no conocen el lenguaje de señas.

Características Principales:

Detección de Gestos con MediaPipe: Utiliza la biblioteca MediaPipe de Google para detectar y reconocer gestos de lenguaje de señas en tiempo real a través de la cámara de un dispositivo.
Preprocesamiento de Imágenes con OpenCV: Utiliza OpenCV para realizar preprocesamiento de imágenes, incluyendo la eliminación de ruido, la normalización y la segmentación de manos para una detección precisa de gestos.
Clasificación con Random Forest: Utiliza el algoritmo Random Forest, implementado con la biblioteca scikit-learn, para clasificar los gestos de lenguaje de señas detectados por MediaPipe en diferentes categorías correspondientes a letras, palabras o frases.
Traducción de Gestos a Texto o Voz: Una vez clasificados los gestos, la aplicación traduce la secuencia de gestos a texto o voz, permitiendo a los usuarios comunicarse con personas que no conocen el lenguaje de señas.
Interfaz de Usuario Intuitiva: Proporciona una interfaz de usuario intuitiva y fácil de usar, que muestra la traducción en tiempo real y ofrece opciones para personalizar la configuración, como el idioma de salida y la velocidad de la voz.
Tecnologías Utilizadas:

Lenguaje de Programación: Python
Bibliotecas y Frameworks:
MediaPipe para detección de gestos.
OpenCV para preprocesamiento de imágenes.
scikit-learn para implementar el algoritmo Random Forest.
Text-to-Speech (TTS) Library: pyttsx3 para la generación de voz.
Beneficios:

Facilita la comunicación entre personas con discapacidad auditiva y personas que no conocen el lenguaje de señas.
Mejora la accesibilidad y la inclusión al proporcionar una herramienta de traducción en tiempo real fácil de usar.
Promueve la conciencia sobre la comunidad de personas con discapacidad auditiva y fomenta la igualdad de oportunidades en la comunicación.
SignLangTranslate es una solución innovadora que utiliza tecnologías avanzadas para romper las barreras de comunicación y promover la inclusión de personas con discapacidad auditiva en la sociedad.
