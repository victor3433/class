import cv2
import numpy as np
 
captura = cv2.VideoCapture(0)

while(1):
   _, imagen = captura.read()
 
   hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
   155-017-030	inferior
   254-000-000	superior
rojo_bajos = np.array([155,017,030])
rojo_altos = np.array([254, 000, 000])
moments = cv2.moments(mask)
area = moments['m00']
if(area > 2000000):
   #Buscamos los centros
   x = int(moments['m10']/moments['m00'])
   y = int(moments['m01']/moments['m00'])
 
   #Escribimos el valor de los centros
   print "x = ", x
   print "y = ", y
 
   #Dibujamos el centro con un rectangulo
   cv2.rectangle(imagen, (x, y), (x+2, y+2),(0,0,255), 2)

cv2.imshow('mask', mask)
cv2.imshow('Camara', imagen)
#Se sale con ESC
   tecla = cv2.waitKey(5) & 0xFF
   if tecla == 27:
      break
 
cv2.destroyAllWindows()
