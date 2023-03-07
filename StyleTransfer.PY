# We import needed libraries for style transfer, video deploying on screen and time management 
import tensorflow as tf
import cv2
import time

# Create a new camera instance
captura = cv2.VideoCapture(0)

# Here we insert the file rute to the style images we are about to use
estilos = ["ruta/del/estilo1.jpg", "ruta/del/estilo2.jpg", "ruta/del/estilo3.jpg"]

# We create a new instance  Creamos una variable para almacenar el tiempo de inicio del bucle
inicio = time.time()

# Loop for capturing and process each photogram
while(True):
    # We 'read' each photogram
    ret, frame = captura.read()

    # If there is no photograms reamaining, the loop if finished
    if not ret:
        break

    # After 30 seconds, the style is change
    if time.time() - inicio > 30:
        # Restart the time count
        inicio = time.time()

        # We get the next style from the list above
        estilo = tf.keras.preprocessing.image.load_img(estilos[i % len(estilos)])
        i += 1

    # Generating a representation on the tensor of the photogram
    frame_tensor = tf.keras.applications.vgg19.preprocess_input(tf.keras.preprocessing.image.img_to_array(frame))

    # The style is applied to the photogram
    frame_procesado = modelo.predict(frame_tensor)

    # The original photogram and the one with the style applied is showed
    cv2.imshow("Original", frame)
    cv2.imshow("Transfer de estilo", frame_procesado)

    # If the key 'q' is pressed, the script is finished 
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# The camera instance is deleted and then the window is closed
captura.release()
cv2.destroyAllWindows()
