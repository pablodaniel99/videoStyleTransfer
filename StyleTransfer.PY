# Importamos las bibliotecas necesarias para el transfer de estilo, la captura de video y el manejo del tiempo
import tensorflow as tf
import cv2
import time

# Creamos una instancia de la cámara
captura = cv2.VideoCapture(0)

# Creamos una lista con los diferentes estilos que queremos aplicar
estilos = ["ruta/del/estilo1.jpg", "ruta/del/estilo2.jpg", "ruta/del/estilo3.jpg"]

# Creamos una variable para almacenar el tiempo de inicio del bucle
inicio = time.time()

# Creamos un bucle para capturar y procesar cada fotograma del video
while(True):
    # Leemos un fotograma del video
    ret, frame = captura.read()

    # Si no hay más fotogramas, terminamos el bucle
    if not ret:
        break

    # Si han pasado más de 30 segundos desde el inicio del bucle, cambiamos de estilo
    if time.time() - inicio > 30:
        # Reiniciamos el contador de tiempo
        inicio = time.time()

        # Cargamos el siguiente estilo de la lista
        estilo = tf.keras.preprocessing.image.load_img(estilos[i % len(estilos)])
        i += 1

    # Generamos una representación en tensor del fotograma
    frame_tensor = tf.keras.applications.vgg19.preprocess_input(tf.keras.preprocessing.image.img_to_array(frame))

    # Aplicamos el transfer de estilo al fotograma
    frame_procesado = modelo.predict(frame_tensor)

    # Mostramos el fotograma original y el fotograma con el transfer de estilo aplicado
    cv2.imshow("Original", frame)
    cv2.imshow("Transfer de estilo", frame_procesado)

    # Si se pulsa la tecla 'q', terminamos el bucle
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Liberamos la cámara y cerramos las ventanas de video
captura.release()
cv2.destroyAllWindows()