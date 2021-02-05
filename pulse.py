from gpiozero import LED
from time import sleep

led = LED(2)

print('Beginning never-ending loop to "pulse" LED; press Control + C to cancel program.')
while True: # this is a "forever" loop; pressing Control+C while it's running will stop it, though
	led.on()
	sleep(1)
	led.off()
	sleep(1.0) # this is actually the same thing as above;
				# this just demonstrates that 1 is the same as 1.0, as far as the sleep function cares
