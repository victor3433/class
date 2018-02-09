from dronekit import connect, VehicleMode, LocationGlobalRelative
import time



def arm_and_takeoff(TargetAltitude):
#Vehicle connection
	print ("Executing Takeoff")

	while not drone.is_armable:
		print ("Vehicle is not armable, waiting...")
		time.sleep(1)

	print("Ready to arm")
	drone.mode = VehicleMode("GUIDED")
	drone.armed = True

	while not drone.armed:
		print("waiting for arming...")
		time.sleep(1)

	print("Ready for takeoff, taking off...")
	drone.simple_takeoff(TargetAltitude)

	while True: 
		Altitude = drone.location.global_relative_frame.alt
		print("Altitude ", Altitude)
		time.sleep(1)

		if Altitude >= TargetAltitude * 0.95:
			print("Altitude reached")
			break





#Vehicle connection
drone = connect('127.0.0.1:14551', wait_ready=True)
arm_and_takeoff(20)
drone.airspeed = 10
A_point = LocationGlobalRelative (20.735513, -103.457498, 20)
B_point = LocationGlobalRelative (20.736369, -103.457426, 20)
C_point = LocationGlobalRelative (20.736331, -103.456801, 20)
A_point = LocationGlobalRelative (20.735513, -103.457498, 20)

print("going to location A")
drone.simple_goto(A_point)
time.sleep(30)
print("going to location B")

drone.simple_goto(B_point)
time.sleep(30)
print("going to location C")

drone.simple_goto(C_point)
time.sleep(28)
print("going home")

drone.simple_goto(A_point)
time.sleep(30)