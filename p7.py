Practical 8
Using Flame Sensor and glow and LED

To interface a Flame Sensor module with Raspberry Pi 3 and detect fire/flame. When flame is detected, turn LED/Buzzer ON and display a message on the terminal.

Flame Sensor: -
 A flame sensor is a device used to detect the presence of a flame or fire by sensing light, heat, or ionized gases produced by combustion. It converts this detection into an electrical signal that can be used for monitoring, control, or safety systems.


Components Required: -
•	Raspberry Pi 3 + SD card + power
•	Flame Sensor module (commonly KY-026 / IR flame sensor)
•	LED + 330Ω resistor (or Buzzer)\
•	Breadboard + Jumper wires



Pin Connection :-

| Flame Sensor | Raspberry Pi | GPIO Numbering |
|--------------|--------------|----------------|
| VCC (+)      | Pin 1        | 3.3V           |
| GND          | Pin 6        | Ground         |
| DO / AO      | Pin 11       | GPIO 17        |





LED / BUZZER: -

| LED / Buzzer                | Raspberry Pi | GPIO Numbering |
|----------------------------|--------------|----------------|
| Long Leg / + Terminal      | Pin 12       | GPIO 18        |
| Short Leg / - Terminal     | Pin 14       | Ground         |
 
    



Code: -
"""
To interface a Flame Sensor module with Raspberry Pi 3 and detect fire/flame.
When flame is detected, turn LED/Buzzer ON and display a message on the terminal.
"""

import RPi.GPIO as GPIO
import time

# GPIO pin definitions
FLAME_DO = 17   # GPIO17 (Pin 11) - Flame Sensor Digital Output
ALERT = 18      # GPIO18 (Pin 12) - LED/Buzzer

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLAME_DO, GPIO.IN)
GPIO.setup(ALERT, GPIO.OUT)

GPIO.output(ALERT, False)

print("Flame Sensor Ready... (Press CTRL+C to stop)")

try:
    while True:
        value = GPIO.input(FLAME_DO)
        print("Sensor Output (DO) =", value)

        # Many flame sensors are ACTIVE-LOW
        if value == 0:
            GPIO.output(ALERT, True)
            print("Flame Detected! ALERT ON")
        else:
            GPIO.output(ALERT, False)
            print("No flame detected. ALERT OFF")

        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nExiting program...")

finally:
    GPIO.cleanup()








For Viva-


# 📘 Viva Questions – Flame Sensor with Raspberry Pi (IoT)

## 🔹 1. Basics of Flame Sensor

**Q1. What is a Flame Sensor?**
**Ans:** A flame sensor is a device that detects fire or flame by sensing infrared light or radiation emitted during combustion.

**Q2. On what principle does a flame sensor work?**
**Ans:** It works by detecting infrared (IR) radiation emitted by flames.

**Q3. What type of sensor is a flame sensor?**
**Ans:** It is an IR-based digital (and sometimes analog) sensor.

---

## 🔹 2. Sensor Output & Logic

**Q4. What is meant by active-low sensor?**
**Ans:** A sensor where output becomes LOW (0) when an event (like flame detection) occurs.

**Q5. What does HIGH output indicate?**
**Ans:** No flame detected.

**Q6. What type of signal does the flame sensor give?**
**Ans:** Digital signal (0 or 1), and sometimes analog output.

---

## 🔹 3. Raspberry Pi & GPIO

**Q7. What is Raspberry Pi 3 used for in this project?**
**Ans:** It reads sensor data and controls alert devices like LED or buzzer.

**Q8. What is GPIO?**
**Ans:** Pins used to connect sensors and actuators with Raspberry Pi.

**Q9. Why is one GPIO set as input and another as output?**
**Ans:**

* Input → Read sensor value
* Output → Control LED/Buzzer

---

## 🔹 4. Python Programming Concepts

**Q10. What is Python used for here?**
**Ans:** To process sensor input and control output devices.

**Q11. What does GPIO.input() do?**
**Ans:** Reads data from the sensor.

**Q12. What does GPIO.output() do?**
**Ans:** Sends signal to LED or buzzer.

**Q13. Why is time delay used?**
**Ans:** To control reading frequency and avoid rapid fluctuations.

---

## 🔹 5. Alert System Concept

**Q14. Why is LED or buzzer used in this project?**
**Ans:** To provide visual or audible alert when flame is detected.

**Q15. What is an alert system?**
**Ans:** A system that notifies users about abnormal conditions like fire.

---

## 🔹 6. IoT & Real-Time Monitoring

**Q16. What is real-time detection?**
**Ans:** Immediate detection and response to events like fire.

**Q17. How is this project useful in IoT?**
**Ans:** It enables remote fire monitoring and safety automation.

---

## 🔹 7. Applications

**Q18. Where are flame sensors used?**
**Ans:**

* Fire alarm systems
* Industrial safety
* Gas detection systems
* Smart homes

**Q19. How can this be used in smart cities?**
**Ans:** For automated fire detection and emergency alerts.

---

## 🔹 8. Comparison & Understanding

**Q20. Difference between flame sensor and smoke sensor?**
**Ans:**

* Flame sensor → Detects fire light/IR
* Smoke sensor → Detects smoke particles

---

## 🔹 9. Troubleshooting

**Q21. Why might the sensor give false detection?**
**Ans:**

* Sunlight interference
* Heat sources
* Electrical noise

**Q22. Why might LED/Buzzer not work?**
**Ans:**

* Wrong wiring
* Incorrect GPIO pin
* Code error

---

## 🔹 10. Advanced Concepts

**Q23. What is sensor sensitivity?**
**Ans:** Ability of sensor to detect small changes.

**Q24. What is threshold in sensors?**
**Ans:** Minimum value at which sensor triggers output.

---

## 🔹 11. Integration & Expansion

**Q25. How can this project be improved?**
**Ans:**

* Send alerts to mobile
* Connect to cloud
* Add water sprinkler system

**Q26. Can this system be automated?**
**Ans:** Yes, it can automatically trigger alarms or safety mechanisms.

---

## 🔹 12. Security & Safety

**Q27. Why is fire detection important?**
**Ans:** To prevent damage, save lives, and ensure safety.

---

## 🔹 13. Conceptual Understanding

**Q28. What is an embedded system?**
**Ans:** A system where software controls hardware devices.

**Q29. Why is Raspberry Pi suitable for safety systems?**
**Ans:**

* Real-time processing
* Easy sensor integration
* Internet connectivity

---

## 🔹 14. Higher-Level Thinking

**Q30. How can this system be used in industrial automation?**
**Ans:** For automatic shutdown of machines during fire detection.

---

