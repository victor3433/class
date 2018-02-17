#first we new to connect to apm with cmd or terminal using the next commands.
	#this command is to make the drone house insede the campus #dronekit-sitl copter --home=20.7377382,-103.4570051,1357,180
	#then we need to make the connection with #mavproxy.py --master tcp:127.0.0.1:5760 --out udp:127.0.0.1:14551 --out udp:10.43.14.246:14550
#this is a group of codes that are already givven by dronekit in this case
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative 
from pymavlink import mavutil
import Tkinter as tk
import dronekit_sitl

sitl = dronekit_sitl.start_default(20.735892,-103.457091)
connection_string = sitl.connection_string

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

#change the drone to x, y, z
def set_velocity_body(vehicle, vx, vy, vz):
	msg = vehicle.message_factory.set_position_target_local_ned_encode(
			0,
			0, 0,
			mavutil.mavlink.MAV_FRAME_BODY_NED,
			0b0000111111000111,
			0, 0, 0,
			vx, vy, vz,
			0, 0, 0,
			0, 0)
	vehicle.send_mavlink(msg)
	vehicle.flush()


#this read the keys you press
def key(event):
	if event.char == event.keysym:
		if event.keysym == 'r':
			drone.mode = VehicleMode("RTL")
#this are the specification for the moves and speed will take.
	else:
		if event.keysym == 'Up':
			set_velocity_body(drone,5,0,0)
		elif event.keysym == 'Down':
			set_velocity_body(drone,-5,0,0)
		elif event.keysym == 'Left':
			set_velocity_body(drone,0,-5,0)
		elif event.keysym == 'Right':
			set_velocity_body(drone,0,5,0)

#the drone connect to that udp and take off in an altittude of 10 meters
drone = connect('udp:127.0.0.1:14551', wait_ready=True)
arm_and_takeoff(10)
#start reading the code and the movement.with the tkinter.
root = tk.Tk()
print (">>Control the drone with the arrow keys. press key r to activate RTL mode")
root.bind_all('<key>', key)
root.mainloop()
self.tk(call(bind_all, cmd))

DroneBattery = drone.battery.voltage
print ('Drone battery:', DroneBattery, 'V')

#finish and exit the code

drone.close()
sitl.stop()
