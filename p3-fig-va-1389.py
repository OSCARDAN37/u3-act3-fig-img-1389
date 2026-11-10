import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
# Oscar Flores NC = 1389
print("Oscar Flores NC = 1389")
print("UIII Act3 colocar puntos a una imagen  en blanco y negro VA")
mi_imagen = cv2.imread('elmichi.jpg')
plt.imshow(mi_imagen)
plt.title("jackson y Oscar Flores 1389")
plt.show()
print("-+-+-+- Puntos en la imagen 1389 -+-+-+-")
plt.imshow(mi_imagen)
x = [100,100,300,177]
y = [100,400,500,301]
plt.scatter(x, y, s=20,c='blue')
plt.show()