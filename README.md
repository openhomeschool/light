# The "LIGHT" project
## openhome.school Computer Class

This project will shed some light on things.  After lighting an LED with a battery and a resistor,
you will use python code to turn the LED on and off through a GPIO pin.

** An LED is a Light Emitting Diode - it emits light when a voltage is applied to it. **

## A Handful

First, connect the "F" end (with a hole in it) of an MF wire to a 220-Ohm resistor, both provided
by your instructor.
Then, connect the "F" (hole) end of another MF wire to the **short** leg of a red/orange/yellow LED.
Then, try to hold two batteries together, button-top-to-flat-bottom, and put the "M" (pointy wire)
end of the resistor-assembly wire against the bump ("+") top of the top battery.
Then, try to hold the "M" (pointy wire) end of the LED-assembly wire against the flat ("-") bottom of
the bottom battery.
Finally, get a friend to hold the long-leg of the LED against the remaining leg of the resistor,
completing the circuit.  The final assembly should look like this:

Watch the LED light up.

## A Breadboard

Time to use a tool to make this simpler.  Connect the resistor and LED as shown here:

Note that the long-leg of the LED is in the same "row" as one end of the resistor.  Now we'll
connect leads to the "top" of the circuit (the resistor end) and the "bottom" of the circuit
(the LED end).  The "top" lead, leading to the resistor, should be held to the button-top of the top
of the top battery ("+" end) and the "bottom" lead, from the LED, should be held to the bottom of the 
bottom battery ("-" end).  Watch the LED light up.

## A Computer

Finally, rather than using a pair of batteries as the power source, let's use the Raspberry Pi.
In fact, let's write a small program that lights the LED and then turns it off again!

Your instructor should have pre-attached a couple of MF jumper wires to your GPIO pins on your Pi.

** GPIO pins are General Purpose In/Out pins, to which wires can be attached, to control electronic
circuits.**  These pins can be controlled via code running on the computer.

Connect the "signal" jumper to the "top" of your circuit, where you connected the battery "+"
terminal earlier -- the "resistor end" of the circuit.  Connect the "ground" jumper to the "bottom"
of your circuit, where you connected the battery "-" terminal earlier -- the "LED end" of the
circuit.  Your instructor will teach you about voltage, current, and resistance later.

Note that your LED **might** light up.  Or it might not.  Whether that signal pin has voltage or
not is unknown.  Soon, you will tell it to turn on or off.

Open a terminal, according to your instructor's guidance, and type:

```sh
cd ohs
cd light
```

Then type the following lines; watch what happens to the LED each time:

```sh
python light_on.py
python light_off.py
```

Let's look at those files.  Open your file editor, according to your instructor's guidance, and
consider the code in light_on.py and light_off.py.  Now, back in your terminal, try:

```sh
python light_pulse.py
```

Inspect this code in your editor.  Try to change the "sleep" time values to see what effect it has.
Consider values like 0.5, 0.1, 0.05, and 0.01.

## More

For more investigation...

[reading resistor color codes](https://eepower.com/resistor-guide/resistor-standards-and-codes/resistor-color-code/)
[basic Ohm's Law video](https://www.khanacademy.org/science/high-school-physics/dc-circuits/electric-current-resistivity-and-ohms-law/v/circuits-part-1)
[more on current fundamentals](https://www.khanacademy.org/science/electrical-engineering/introduction-to-ee/intro-to-ee/v/ee-current)
[circuit logic introduction](https://www.khanacademy.org/computing/code-org/computers-and-the-internet/how-computers-work/v/khan-academy-and-codeorg-circuits-logic)

