# This file has been written to your home directory for convenience. It is
# saved as "/home/pi/humidity-2021-04-06-10-33-54.py"

from sense_emu import SenseHat

sense = SenseHat()

green = (0, 255, 0)
white = (255, 255, 255)

while True:
    while True:
        acceleration = sense.get_accelerometer_raw()
        compass = sense.get_compass_raw()
        
        pressure = sense.get_pressure()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x=round(x, 0)
        y=round(y, 0)
        z=round(z, 0)

        print("Acceleraion: x={0}, y={1}, z={2}".format(x, y, z))
        print("Pressure ={0}, magnetic={1} ".format(pressure,str(compass)))
