Practical 6
Using an IR Sensor with Raspberry Pi 3 and display the message using Python


IR Sensor
An IR (Infrared) sensor is an electronic device that detects infrared radiation to sense its surroundings, measure temperature, or detect motion. They are widely used in everyday items like TV remotes and in complex applications such as robotics and security systems.
	
  

Sr. No	Condition	Output
1	Object Detected	Low(0)
2	No object 	High(1)

Components Required
•	Raspberry Pi 3 Model B
•	IR Sensor
•	5V Buzzer (We are using LED instead)
•	330 Ohms transistor
•	Mini Breadboard
•	Connecting Wires
•	Power Supply
•	Computer

Data Pin of IR Sensor to GPIO23 (Physical Pin 16)
LED to GPIO24 (Physical Pin 18)


| Component        | Function            | GPIO Pin  | Physical Pin |
|------------------|---------------------|-----------|--------------|
| IR Sensor        | VCC                 | 5V        | Pin 2 / 4    |
| IR Sensor        | GND                 | GND       | Pin 6        |
| IR Sensor        | Data / OUT          | GPIO 23   | Pin 16       |
| LED              | Positive (Anode)    | GPIO 24   | Pin 18       |
| LED              | Ground (Cathode)    | GND       | Pin 6 / 9    |
   


#When object detected LED is solid 

Code: -
import RPi.GPIO as GPIO 
import time

sensor = 16
led = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

GPIO.output(led, False)

print ("IR Sensor Ready....")

try:
    while True:
        if GPIO.input(sensor) == 0:
            GPIO.output(led, True)
            print ("Object Detected!")
        else:
            GPIO.output(led, False)
            print ("No Object")
except KeyboardInterrupt:
    print("Program stopped by User")
finally:
    GPIO.output(led, False)
    GPIO.cleanup()




 


#When the object is detected LED blinks 

Code: -
import RPi.GPIO as GPIO 
import time

sensor = 16
led = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

GPIO.output(led, False)

print ("IR Sensor Ready....")

try:
    while True:
        if GPIO.input(sensor) == 0:
            print ("Object Detected")
            GPIO.output(led, True)
            time.sleep(0.3)
            GPIO.output(led, False)
            time.sleep(0.3)
            
        else:
            GPIO.output(led, False)
            print ("No Object")
            time.sleep(0.3)
except KeyboardInterrupt:
    print("Program stopped by User")
finally:
    GPIO.output(led, False)
    GPIO.cleanup()











For Viva-


# 📘 Viva Questions – IR Sensor with Raspberry Pi (IoT)

## 🔹 1. Basics of IR Sensor

**Q1. What is an Infrared Sensor?**
**Ans:** An IR sensor is an electronic device that detects infrared radiation to identify objects or motion in its surroundings.

**Q2. How does an IR sensor work?**
**Ans:** It emits infrared light and detects reflections from nearby objects to determine presence.

**Q3. What are the main components of an IR sensor module?**
**Ans:** IR LED (emitter), photodiode/phototransistor (receiver), and signal processing circuit.

---

## 🔹 2. Output Logic & Signals

**Q4. What type of signal does an IR sensor give?**
**Ans:** Digital output (HIGH or LOW).

**Q5. What does LOW (0) indicate in this sensor?**
**Ans:** Object detected.

**Q6. What does HIGH (1) indicate?**
**Ans:** No object detected.

**Q7. Why is this called digital sensing?**
**Ans:** Because it provides only two states (0 or 1).

---

## 🔹 3. Raspberry Pi & GPIO

**Q8. What is Raspberry Pi 3 Model B used for here?**
**Ans:** It reads sensor input and controls output devices like LEDs.

**Q9. What is GPIO?**
**Ans:** Pins used to connect and control external hardware devices.

**Q10. Why is one GPIO set as input and another as output?**
**Ans:**

* Input → Read sensor data
* Output → Control LED

---

## 🔹 4. Python Programming Concepts

**Q11. What is Python used for?**
**Ans:** To write code that reads sensor input and controls LED output.

**Q12. What does GPIO.input() do?**
**Ans:** Reads the value (HIGH/LOW) from a pin.

**Q13. What does GPIO.output() do?**
**Ans:** Sends signal to control devices like LED.

**Q14. Why is try-except used?**
**Ans:** To handle interruptions and safely stop the program.

**Q15. What is the purpose of GPIO.cleanup()?**
**Ans:** To reset GPIO pins and prevent damage.

---

## 🔹 5. Sensor Behavior & Logic

**Q16. Why does LED glow when object is detected?**
**Ans:** Because sensor sends LOW signal, triggering output action.

**Q17. What is the difference between steady ON and blinking LED?**
**Ans:**

* Steady ON → Continuous detection
* Blinking → Indication or alert signal

---

## 🔹 6. Real-Time Processing

**Q18. What is real-time monitoring?**
**Ans:** Continuous checking of sensor data without delay.

**Q19. Why is loop used in the program?**
**Ans:** To continuously monitor the sensor status.

---

## 🔹 7. IoT Applications

**Q20. Where are IR sensors used in real life?**
**Ans:**

* Obstacle detection
* Security systems
* Automatic doors
* Robot navigation

**Q21. How is this useful in IoT?**
**Ans:** It enables smart automation based on object detection.

---

## 🔹 8. Troubleshooting & Practical Understanding

**Q22. Why might the sensor not detect objects?**
**Ans:**

* Incorrect wiring
* Poor alignment
* Distance too far

**Q23. Why might LED not glow?**
**Ans:**

* Wrong GPIO pin
* Code error
* Faulty LED

---

## 🔹 9. Advanced Concepts

**Q24. What is the difference between IR sensor and ultrasonic sensor?**
**Ans:**

* IR → Uses infrared light
* Ultrasonic → Uses sound waves

**Q25. What are limitations of IR sensors?**
**Ans:**

* Affected by sunlight
* Limited range
* Poor detection for transparent objects

---

## 🔹 10. Integration Concepts

**Q26. How can this system be extended?**
**Ans:**

* Add buzzer for alarm
* Connect to cloud
* Use with camera systems

**Q27. Can IR sensors detect temperature?**
**Ans:** Some advanced IR sensors can measure temperature (thermal sensors).

---

## 🔹 11. Security & Automation

**Q28. How is IR sensor used in security systems?**
**Ans:** Detects motion and triggers alarms.

---

## 🔹 12. Conceptual Understanding

**Q29. What is embedded system?**
**Ans:** A system where software controls hardware devices.

**Q30. Why is Raspberry Pi suitable for sensor-based projects?**
**Ans:**

* GPIO support
* Easy programming
* Real-time processing
* Network connectivity

---
