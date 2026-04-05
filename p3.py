Controlling an Led with Python Program & Node Red

Steps: -
1.	Take out the Mouse, Keyboard and Monitor wires from the CPU

2.	And then connect those to the Raspberry Pi

3.	Insert the Memory card keeping the yellow lines circuit downside

4.	Connect the Charger to the plug and to the raspberry pi

5.	Take the bread board and the 330 ohm resistor (color sequence – Orange – Orange- Brown - Golden)

6.	Take Jumper Wires
    

Upper – Even pins
Lower – Odd pins
 
7.	In the Other PC Open the VNC Viewer then connect to the Raspberry Pi PC. (If not connected then in Raspberry Pi PC in terminal type the command ifconfig

8.	In the raspberry pi - physical pin 15 and for ground pin 6, connect the female side pin to the raspberry pi GPIO Headers as given 

9.	Now on the Bread Board the 15 no. pin put that on the red line (right side outer section) and 

10.	the 6 no. pin on the Blue line (left side inner section)

11.	Now aside to the 15 pin put the resistor’s one end and the other end in the right side inner section of the bread board          

12.	Then the LED’s Long leg put aside (baju me)the resistor and the other short leg on the other side of the divider of the bread board 

13.	The 6 pin put it aside the other side of the divider aside to the short leg of LED 

14.	Hindi Explanation Below - 

15 no. pin pe jumper wire (white wire) – woh connect hoga outer part of right side
White wire ke baju me resistor ka ek pin and uska dusra end jayega right side ke inner part me 
Resistor ka dusra part ke niche LED ka longer leg – and shorter leg on inner part of left side
6 no. pin pe jumper wire (red wire) – woh connect hoga LED ke shorter leg ke niche
 
15.	In the Raspberry Pi PC, Go to the Raspberry Pi icon > Programming > Thonny Python IDE
 



16.	Write the Program for the LED.
# Blinking LED Program
# Connect the LED to GPIO22 (i.e. Physical Pin 15)

import RPi.GPIO as GPIO
from time import sleep

# Set the pin numbering mode
GPIO.setmode(GPIO.BCM)  #Or use this GPIO.setmode(GPIO.BOARD)

# Define LED pin (GPIO22 = Physical Pin 15)
ledPin = 22  #ledPin = 15

# Set up the LED pin as output
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, False)

try:
    while True:
        GPIO.output(ledPin, True)   # LED ON
        sleep(1)                    # wait for 1 second
        GPIO.output(ledPin, False)  # LED OFF
        sleep(1)                    # wait for 1 second

finally:
    GPIO.output(ledPin, False)
    GPIO.cleanup()                  # reset the GPIO pins







PART B
1.	In Raspberry Pi PC, Click on Raspberry Pi icon then in > Programming > Node Red > open and Copy the below link from there
http://192.168.2.47:1880

2.	Paste that in the Internet Explorer, Node RED Application will start.

3.	Drag the 2 Inject from Input from the Left Panel and Drag rpi gpio out from the Raspberry Pi.
  
4.	Double click on the node and then in Payload select True and name as it on then click on done.

5.	Then for the other node (below one node) double click and then in Payload select False and name it as  off then click on done.

6.	Then Double click on the rpi gpio out and select the 15 pin and click on done.

7.	Then Click on the Deploy if options given choose Full Deploy
  
8.	Then click on the on node and the LED will glow and click on the off node and the LED will turn off.











For Viva-
---

# 📘 Viva Questions – LED Control using Python & Node-RED

## 🔹 1. Basics of GPIO & LED

**Q1. What is GPIO?**
**Ans:** GPIO pins are programmable pins on Raspberry Pi used to connect and control external devices like LEDs, sensors, etc.

**Q2. Why is GPIO important in IoT?**
**Ans:** It allows interaction between software and physical hardware components.

**Q3. What is an LED?**
**Ans:** LED (Light Emitting Diode) is a semiconductor device that emits light when current flows through it.

**Q4. Why do we use a resistor with LED?**
**Ans:** To limit current and prevent the LED from burning out.

---

## 🔹 2. Pin Configuration Concepts

**Q5. What is the difference between BCM and BOARD mode?**
**Ans:**

* BCM → Uses GPIO numbering (software-based)
* BOARD → Uses physical pin numbering

**Q6. Why is correct pin configuration important?**
**Ans:** Incorrect configuration may damage components or cause wrong output.

---

## 🔹 3. Python & GPIO Programming

**Q7. What is Python used for in this practical?**
**Ans:** Python is used to write code that controls GPIO pins to turn the LED ON/OFF.

**Q8. What is the role of RPi.GPIO library?**
**Ans:** It allows Python programs to control GPIO pins.

**Q9. What does GPIO.setup() do?**
**Ans:** It configures a pin as input or output.

**Q10. What does GPIO.output() do?**
**Ans:** It sends HIGH or LOW signal to a pin.

**Q11. What is the purpose of GPIO.cleanup()?**
**Ans:** It resets all GPIO pins to safe state after program execution.

---

## 🔹 4. Logic & Signal Concepts

**Q12. What is HIGH and LOW in GPIO?**
**Ans:**

* HIGH → 3.3V (LED ON)
* LOW → 0V (LED OFF)

**Q13. What is a digital signal?**
**Ans:** A signal with only two states: ON (1) or OFF (0).

---

## 🔹 5. Node-RED Concepts

**Q14. What is Node-RED?**
**Ans:** Node-RED is a visual tool used to connect hardware, APIs, and services using flow-based programming.

**Q15. Why is Node-RED used in IoT?**
**Ans:** It simplifies IoT development using drag-and-drop nodes instead of coding.

**Q16. What is an Inject node?**
**Ans:** It sends input signals (like True/False) to trigger actions.

**Q17. What is rpi-gpio out node?**
**Ans:** It is used to control Raspberry Pi GPIO pins from Node-RED.

---

## 🔹 6. Python vs Node-RED

**Q18. Difference between Python control and Node-RED control?**
**Ans:**

* Python → Code-based control
* Node-RED → Visual flow-based control

**Q19. Which is better for beginners and why?**
**Ans:** Node-RED, because it is easier and does not require coding knowledge.

---

## 🔹 7. IoT Application-Based Questions

**Q20. How is LED control useful in real-world IoT?**
**Ans:**

* Smart home lighting
* Status indicators
* Alert systems

**Q21. How can this concept be extended?**
**Ans:**

* Control appliances
* Connect sensors
* Automate systems

---

## 🔹 8. Troubleshooting & Practical Understanding

**Q22. Why might the LED not glow?**
**Ans:**

* Wrong wiring
* Incorrect GPIO pin
* Missing resistor
* Code error

**Q23. What happens if resistor is not used?**
**Ans:** LED may burn due to excess current.

---

## 🔹 9. Advanced Concepts

**Q24. What is PWM (Pulse Width Modulation)?**
**Ans:** Technique to control brightness of LED by varying signal width.

**Q25. Can Raspberry Pi handle analog signals?**
**Ans:** No, it only supports digital signals (needs ADC for analog).

---

## 🔹 10. Integration Concepts

**Q26. How can Node-RED be used with cloud services?**
**Ans:** It can connect to APIs, MQTT, and cloud platforms.

**Q27. What is MQTT in IoT?**
**Ans:** A lightweight messaging protocol used for communication between devices.

---

## 🔹 11. Security & Best Practices

**Q28. Why is safe shutdown of GPIO important?**
**Ans:** To prevent damage to hardware and incorrect states.

---

## 🔹 12. Conceptual Understanding

**Q29. What is embedded programming?**
**Ans:** Writing software to control hardware devices.

**Q30. Why is Raspberry Pi suitable for IoT projects?**
**Ans:**

* Supports networking
* GPIO pins available
* Runs full OS
* Easy programming

