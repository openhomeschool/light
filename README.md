# The "LIGHT" project
## openhome.school Computer Class

This project will shed some light on things.  After lighting an LED with a battery and a resistor,
you will use python code to turn the LED on and off through a GPIO pin.

**An LED is a Light Emitting Diode - it emits light when a voltage is applied to it.**

## A Handful

First, connect the "F" end (with a hole in it) of an M-F ("jumper") wire to a 220-Ohm resistor, both
provided by your instructor.
Then, connect the "F" (hole) end of another M-F wire to the **short** leg of a red, orange, or
yellow LED.
Then, try to hold two batteries together, button-top-to-flat-bottom, and put the "M" (pointy probe)
end of the resistor-assembly wire against the bump ("+") top of the top battery.
Then, try to hold the "M" (pointy probe) end of the LED-assembly wire against the flat ("-") bottom
of the bottom battery.
Finally, get a friend to hold the free **long** leg of the LED against the remaining leg of the
resistor, completing the circuit.  The final assembly should look like this:
![LED assembly](led_assembly.jpg)

Watch the LED light up!  Notice that the light goes off when you disconnect any single connection.
When you hold all of the connections together, you have a closed circuit.  When you disconnect a
wire anywhere along the circuit, you "open" the circuit; electricity is no longer able to flow, and
when no electricity flows through the LED, it does not light up.

## A Breadboard

Time to use a tool to make this easier.  Connect the resistor and LED as shown here:
![LED breadboard assembly](led_breadboard_assembly.jpg)

Note that the long-leg of the LED is in the same "row" as one end of the resistor.  Now we'll
connect leads to the "top" of the circuit (the resistor end) and the "bottom" of the circuit
(the LED end).  The "top" lead, leading to the resistor, should be held to the button-top of the top
of the top battery ("+" end) and the "bottom" lead, from the LED, should be held to the bottom of
the bottom battery ("-" end).  Watch the LED light up.

## A Computer

Finally, rather than using a pair of batteries as the power source, let's use the Raspberry Pi.
In fact, let's write a small program that lights the LED and then turns it off again!

Your instructor should have pre-attached a couple of MF jumper wires to your GPIO pins on your Pi.

**GPIO pins are General Purpose In/Out pins, to which wires can be attached, to control electronic
circuits.**  These pins can be controlled via code running on the computer.  That is, computer
code can close a switch to the pin, causing electricity to flow through it, if attached to a closed
circuit, or, the computer code can open that internal switch, keeping electricity from flowing
through your circuit even if it's otherwise complete, itself.

Connect the "signal" jumper to the "top" of your circuit, where you connected the battery "+"
terminal earlier -- the "resistor end" of the circuit.  Connect the "ground" jumper to the "bottom"
of your circuit, where you connected the battery "-" terminal earlier -- the "LED end" of the
circuit.  Your instructor will teach you about voltage, current, and resistance.

Note that your LED **might** light up.  Or it might not.  Whether that signal pin has voltage or
not is unknown.  Soon, you will tell it to turn on or off.

Open a terminal, according to your instructor's guidance.  Long ago, this was one of the the only
ways a human interacted with a computer.  Actually, there were even more primitive ways to interact
with a computer, but this was an early and significant way, and is still essential to many today.

**A terminal is a basic program that responds to the most fundamental commands available in a
computer.**  These fundamental commands are communicated by typing - no buttons, no touch-screen,
no voice-activation.

Type these two lines.  Hit the "Enter" key after each:

```sh
cd ohs
cd light
```

Then type the following line, and push Enter; watch what happens to the LED:

```sh
python on.py
```

Now type this line, and push Enter; watch what happens to the LED:

```sh
python off.py
```

Let's look at those files.  Open your file editor, according to your instructor's guidance, and
consider the code in on.py.

```python
from gpiozero import LED
```

This top line checks out code from a "library".  **In software development, a library is a bundle
of code carefully designed and written so that people can use it to simplify their work.**  This
"gpiozero" library will make our task easier than it would be if we had to pay attention to more of
the many details about the GPIO pins.  Thankfully, somebody wrote this library, with code to
represent the idea of an LED, to make our lives easier.

```python
led = LED(2)
```

This line creates something called 'led', and assigns it to a magical thing created via LED(2).
We'll learn more about that magic later.  For now, notice that this is an "assignment"; before this
line of code is run, 'led' did not exist.  After this line, 'led' exists, and is a magical thing
that we can use to turn our real LED, on our breadboard, on or off.

**A variable is a name, in code, that holds a value.** Our variable, here, 'led', could have been
assigned just to the plain "number" value of 2, like this:

```python
led = 2
```

or to a "string" (a string of letters, making a word) representing a color, like this:

```python
led = 'red'
```

but in those two cases, it wouldn't have helped us light up our LED on our breadboard.  For that,
we needed the magic of the gpiozero library and it's special LED interface.  Note that the 2 in
our LED(2) is the pin number, where we the jumper plugs into the GPIO interface.  If we'd plugged it
in one pin further from the edge, we would need to create our led via LED(3).  If we got this wrong,
our LED would not light up.  Computers are very logical - they're very picky about every detail.

Next, we see a "print" line, which prints that string to your console when it gets this far.

Finally,

```python
led.on()
```

This is where our library magic comes in handy.  Once this line of code is executed by our computer,
the LED is fed a current of electrons, flowing from the Pi's 3.3-Volt source, slowed by a 330-Ohm
resistor, so that the electrical conditions are just right for lighting up the LED.

The code then "sleeps" for 5 seconds, so that you can see the effect.  After the program terminates,
the LED may naturally go off, or it may naturally stay on - the state of a GPIO pin, when you're not
directly controlling it, is unpredictable.  It could be "on" or "off".

off.py is nearly identical - still just three lines of code.  The only difference is in the pivotal
led line:

```python
led.off()
```

Now, back in your terminal, try:

```sh
python pulse.py
```

Inspect this code in your editor.  Try to change the "sleep" time values to see what effect it has.
Consider values like 0.5, 0.1, 0.05, and 0.01.  Can you make the sleep times short enough that you
can't perceive individual ons and offs?  Can you see anything else interesting when that happens?

## More

For more investigation...

* [reading resistor color codes](https://eepower.com/resistor-guide/resistor-standards-and-codes/resistor-color-code/)
* [basic Ohm's Law video](https://www.khanacademy.org/science/high-school-physics/dc-circuits/electric-current-resistivity-and-ohms-law/v/circuits-part-1)
* [more on current fundamentals](https://www.khanacademy.org/science/electrical-engineering/introduction-to-ee/intro-to-ee/v/ee-current)
* [circuit logic introduction](https://www.khanacademy.org/computing/code-org/computers-and-the-internet/how-computers-work/v/khan-academy-and-codeorg-circuits-logic)

