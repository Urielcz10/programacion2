import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Cargar la imagen
nombre_imagen = 'C:/Users/Estudiante/Downloads/dragon-ball z'
imagen_original = Image.open(nombre_imagen)
array_imagen = np.asarray(imagen_original)

# Convertir a escala de grises usando operaciones vectorizadas
def convertir_a_gris(imagen):
    coeficientes = np.array([0.2989, 0.5870, 0.1140])
    escala_gris = np.dot(imagen[..., :3], coeficientes)
    return np.stack((escala_gris,) * 3, axis=-1)

imagen_gris = convertir_a_gris(array_imagen).astype(np.uint8)

# Mostrar la imagen en escala de grises
plt.imshow(imagen_gris, cmap='gray')
plt.axis('off')  # Ocultar ejes para una mejor presentación
plt.title('Imagen en escala de grises')
plt.show()