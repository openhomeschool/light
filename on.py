from gpiozero import LED
from time import sleep

led = LED(2)

print("Turning pin-2 LED on...")
led.on()
print("... now 'sleeping' for 5 seconds...")
sleep(5)
print("... now exiting program (LED *might* go back off, by itself... or it might not!)")
