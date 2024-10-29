import cv2 # Importo la biblioteca OpenCV para procesamiento de imagenes
import numpy as np #Importo numpy para manipulacion de matrices
import matplotlib.pyplot as plt #Importo matplotlib para las imagenes
#Cargo la imagen en escala de grises
nombre_imagen = 'Imagenn 1 Dragon Ball Z' #Nombre de la imagen en la misma carpeta que el archivo python
imagen_original = "F:\\Elias Uriel Cortez 5°C TM 2024\\Programacion\\Imagenn 1 Dragon Ball Z.jpeg"
cv2.imread(nombre_imagen,cv2.IMREAD_GRAYSCALE) #Esta leyendo la imagen en escala de grises
#Verifico si la imagen se cargo bien
if imagen_original is None: #Compruebo que la imagen se cargue
    print("Error al cargar la imagen. Verifica qu el archivo de imagen este en la misma carpeta.")
else:
    #Muestro la imagen original
    plt.figure(figsize=(10, 5)) #Voy a configurar el tamaño de la figura para mostrar ambas imagenes
    plt.subplot(1, 2, 1) #Defino la primera posicion en el espacio para la imagen original
    plt.imshow(imagen_original, cmap='gray') #Muestro la imagen original en escala de grises
    plt.title("imagen original") #Le pongo el titulo de la imagen original
    plt.axis('off') #Voy a ocultar los ejes para una mejor visualizacion
    #Ahora volteo horizontalmente la imagen
    imagen_volteada = np.fliplr(imagen_original) #Ahora voy a voltear la imagen de izquierda a derecha usando np.fliplr()
    #Ahora que muestre la imagen volteada
    plt.subplot(1, 2, 2) #Le pongo la segunda posicion en el espacio para la imagen volteada
    plt.title("imagen volteada horizontalmente") #Titulo de la imagen volteada
    plt.axis('off') #Oculto los ejes de nuevo para que se vea piola
    #Y ahora muestro las imagenes en pantalla
    plt.show() #y la figura completa con ambas imagenes
    
    
#¿QUE ES?
#1. plt.figure(): Crea una nueva figura para la visualización.

# 2. plt.subplot(): Divide la figura en una cuadrícula y selecciona una celda para dibujar un gráfico.

# 3. plt.imshow(): Muestra una imagen en una ventana de gráficos.

# 4. plt.title(): Añade un título a la figura o al gráfico.

# 5. plt.axis(): Controla y personaliza los ejes del gráfico.

# 6. plt.show(): Renderiza y muestra todas las figuras abiertas en pantalla.

# ¿PARA QUE SIRVE?

# 1. plt.figure(): Sirve para iniciar una nueva ventana de visualización donde se pueden dibujar gráficos.

# 2. plt.subplot(): Sirve para crear una disposición de múltiples gráficos dentro de una sola figura, permitiendo mostrar varios gráficos en diferentes secciones.

# 3. plt.imshow(): Sirve para visualizar imágenes o matrices de datos, permitiendo representar datos en forma de imágenes.

# 4. plt.title(): Sirve para proporcionar contexto al gráfico, facilitando la comprensión de lo que se está visualizando.

# 5. plt.axis(): Sirve para personalizar la apariencia y los límites de los ejes del gráfico, lo que ayuda a mejorar la legibilidad.

# 6. plt.show(): Sirve para mostrar las figuras y gráficos creados en pantalla, permitiendo al usuario ver el resultado de la visualización.



    
    
    