from dronekit import connect, VehicleMode, LocationGlobalRelative
import time 
import cv2
import numpy as np

def arm_and_takeoff(TargetAltitude):
	print('Executing takeoff')

	while not drone.is_armable:
		print('Vehicle is not armable, waiting...')
		time.sleep(1)
#Here the drone is ready to be armed and changes his mode to GUIDED
	print('Ready to arm')
	drone.mode = VehicleMode('GUIDED')
	drone.armed = True

	while not drone.armed:
		print('Waiting for arming...')
		time.sleep(1)

	print('Ready for takeoff, taking off...')
	drone.simple_takeoff(TargetAltitude)
#With this code the drone can know the altitude it haves
	while True:
		Altitude = drone.location.global_relative_frame.alt 
		print("Altitude: ", Altitude)
		time.sleep(1)

		if Altitude >= TargetAltitude * 0.95:
			print('Altitude reached')
			break


#Here we connect the drone to the APM planner 
drone = connect('127.0.0.1:14551', wait_ready=True)
arm_and_takeoff(20)
#Here is the speed of the drone
drone.airspeed = 5
  

#location 
a = LocationGlobalRelative(20.736806, -103.454347, 3) #0
b = LocationGlobalRelative(20.736806, -103.454434, 3)
c = LocationGlobalRelative(20.736753, -103.454434, 3)
d = LocationGlobalRelative(20.736753, -103.454347, 3)
e = LocationGlobalRelative(20.736759, -103.454431, 3)
f = LocationGlobalRelative(20.736759, -103.454431, 3)
g = LocationGlobalRelative(20.736799, -103.454431, 3)
h = LocationGlobalRelative(20.736799, -103.454347, 3)
i = LocationGlobalRelative(20.736766, -103.454347, 3)
j = LocationGlobalRelative(20.736766, -103.454428, 3)
k = LocationGlobalRelative(20.736793, -103.454428, 3)
m = LocationGlobalRelative(20.736793, -103.454352, 3)
n = LocationGlobalRelative(20.736772, -103.454352, 3)
l = LocationGlobalRelative(20.736772, -103.454324, 3)
o = LocationGlobalRelative(20.736787, -103.454424, 3)
p = LocationGlobalRelative(20.736787, -103.454356, 3)
q = LocationGlobalRelative(20.736779, -103.454356, 3)
r = LocationGlobalRelative(20.736779, -103.454420, 3)


print('Going to point A')
drone.simple_goto(a)
time.sleep(10)

print('Going to point B')
drone.simple_goto(b)
time.sleep(10)

print('Going to point C')
drone.simple_goto(c)
time.sleep(10)

print('Going to point D')
drone.simple_goto(d)
time.sleep(10)

print('Returning to point E')
drone.simple_goto(e)
time.sleep(10)

print('Going to point F')
drone.simple_goto(f)
time.sleep(10)

print('Going to point G')
drone.simple_goto(g)
time.sleep(10)

print('Going to point H')
drone.simple_goto(h)
time.sleep(10)

print('Going to point I')
drone.simple_goto(i)
time.sleep(10)

print('Returning to point J')
drone.simple_goto(j)
time.sleep(10)

print('Going to point K')
drone.simple_goto(k)
time.sleep(10)

print('Going to point M')
drone.simple_goto(m)
time.sleep(10)

print('Going to point N')
drone.simple_goto(n)
time.sleep(10)

print('Going to point O')
drone.simple_goto(o)
time.sleep(10)

print('Going to point P')
drone.simple_goto(p)
time.sleep(10)

print('Going to point Q')
drone.simple_goto(q)
time.sleep(10)

print('Going to point R')
drone.simple_goto(r)
time.sleep(10)


#open

import cv2
import numpy as np
 
captura = cv2.VideoCapture(0)

while(1):
   _, imagen = captura.read()
 
   hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
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
 
if:
include <Servo.h>

	int pin = 9;
	int pos = 0;

	Servo servo;

	void setup() {
	  Serial.begin (9600);
	  servo.attach(pin);
	}

	void loop() {
	  if (pos == 0) {
	    delay(1000);
	  }
	  pos = (pos+1) % 90;
	  servo.write(pos);
	  Serial.println(pos);
	}



cv2.destroyAllWindows()
