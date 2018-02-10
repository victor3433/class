#how o make a mission with python
#first we new to connect to apm with cmd or terminal using the next commands.
	#this command is to make the drone house insede the campus #dronekit-sitl copter --home=20.7377382,-103.4570051,1357,180
	#then we need to make the connection with #mavproxy.py --master tcp:127.0.0.1:5760 --out udp:127.0.0.1:14551 --out udp:10.43.14.246:14550
#this is a group of codes that are already givven by dronekit in this case
from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

def arm_and_takeoff(TargetAltitude):
#Vehicle connection
	print ("Executing Takeoff")
#At this part our drone is not ready to arm. we give him the order to don't armed yet.
	while not drone.is_armable:
		print ("Vehicle is not armable, waiting...")
		time.sleep(1)
#When the drone is also ready he is going to tell us that is ready to arm and start the guided mode that is guided by coordenates.
	print("Ready to arm")
	drone.mode = VehicleMode("GUIDED")
	drone.armed = True
#Sometimes the drone take more time to be ready. So in line 21-24 our drone will tell us he is taking more time to be ready to arm
	while not drone.armed:
		print("waiting for arming...")
		time.sleep(1)
#note:time.sleep(x) is the time in seconds that the program is going to stop.
#When the drone finished all the steps before he is going to tell us. The drone will start to fly at this point and he is going to reach an altitude that we decide to.
	print("Ready for takeoff, taking off...")
	drone.simple_takeoff(TargetAltitude)
#here the drone will tell us the altitude he has 
	while True: 
		Altitude = drone.location.global_relative_frame.alt
		print("Altitude ", Altitude)
		time.sleep(1)
#This command is to make the drone stop trying to be on the exact altitude we choice, so we multiply by 95
		if Altitude >= TargetAltitude * 0.95:
			print("Altitude reached")
			break





#this is the vehicle connection with the terminal as you can see are the same numbers that you use on the terminal.
#Vehicle connection
drone = connect('127.0.0.1:14551', wait_ready=True)
#We define the target altitude in this case 20 meters
arm_and_takeoff(20)
#we define the speed of our drone in this case is at 10 m/s
drone.airspeed = 10

#here are the location of our mission. We have to define each coordenate.
A_point = LocationGlobalRelative (20.735513, -103.457498, 20)
B_point = LocationGlobalRelative (20.736369, -103.457426, 20)
C_point = LocationGlobalRelative (20.736331, -103.456801, 20)
D_point = LocationGlobalRelative (20.735380, -103.456863, 20)
A_point = LocationGlobalRelative (20.735513, -103.457498, 20)

#We finished to define all we need now we need to ejecute the actions with drone.simple_goto("location")
#also we are telling to the drone to tell us about where he is going with print("message")
print("going to location A")
drone.simple_goto(A_point)
time.sleep(20)
print("location reached")
print("going to location B")

print("location reached")
drone.simple_goto(B_point)
time.sleep(50)
print("going to location C")

print("location reached")
drone.simple_goto(C_point)
time.sleep(25)
print("going to location D")

drone.simple_goto(D_point)
time.sleep(50)
print("going home")

drone.simple_goto(A_point)
time.sleep(25)
print("mission accomplished")
#When the drone finished his task, will dropped on the screen the drone's battery in voltage
DroneBattery = drone.battery.voltage
print("drone battery", DroneBattery, "v")
