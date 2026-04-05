Practical 10
Using Smoke Sensors with Raspberry Pi

To detect smoke/gas using an MQ-series smoke sensor module with Raspberry Pi 3 and display the status using LED + buzzer (optional), and print readings on the terminal.

Smoke Sensor
A Smoke Sensor (MQ-series) is used to detect smoke and harmful gases in the air. Sensors like MQ-2 and MQ-135 work by sensing changes in resistance when gas or smoke is present.
When clean air is present, the sensor gives normal output. When smoke or gas is detected, the output changes, which can be read by the Raspberry Pi through the digital (DO) pin.
Smoke sensors are widely used in fire detection systems, gas leakage detection, and air quality monitoring to ensure safety and prevent accidents.

Components Required
•	Raspberry Pi 3 + SD card + RPi OS
•	MQ-2 or MQ-135 gas/smoke sensor module (with AO + DO pins)
•	LED + 330Ω resistor
•	(Optional) Buzzer
•	Jumper wires + Breadboard



Pin Connections

| Smoke Sensor Pin | Raspberry Pi Physical Pin | GPIO Numbering |
|------------------|--------------------------|----------------|
| VCC              | Pin 2 / 4                | 5V             |
| GND              | Pin 6                    | Ground         |
| DO               | Pin 11                   | GPIO17         |



LED

| LED / Buzzer                  | Raspberry Pi Pin | GPIO Numbering |
|-------------------------------|------------------|----------------|
| Long leg / + terminal         | Pin 13           | GPIO27         |
| Short leg / - terminal        | Pin 14           | Ground         |
 
 

#Code: -

import RPi.GPIO as GPIO
import time

SMOKE_DO = 17      # MQ module DO pin connected to GPIO17
LED_PIN = 27       # LED connected to GPIO27
#BUZZER_PIN = 22   # Optional buzzer

GPIO.setmode(GPIO.BCM)
GPIO.setup(SMOKE_DO, GPIO.IN)      # Digital output from sensor
GPIO.setup(LED_PIN, GPIO.OUT)
#GPIO.setup(BUZZER_PIN, GPIO.OUT)

print("Smoke Sensor (MQ) is warming up... Please wait 20 seconds")
GPIO.output(LED_PIN, GPIO.LOW)
#GPIO.output(BUZZER_PIN, GPIO.LOW)
time.sleep(20)

print("System Ready")
print("Monitoring smoke/gas... (Press CTRL+C to exit)")

try:
    while True:
        # DO = 0 when smoke/gas is detected
        smoke_detected = (GPIO.input(SMOKE_DO) == 0)

        if smoke_detected:
            print("SMOKE/GAS DETECTED!")
            GPIO.output(LED_PIN, GPIO.HIGH)
            #GPIO.output(BUZZER_PIN, GPIO.HIGH)
        else:
            print("Air is clean")
            GPIO.output(LED_PIN, GPIO.LOW)
            #GPIO.output(BUZZER_PIN, GPIO.LOW)

        time.sleep(1)

except KeyboardInterrupt:
    print("\nExiting... Cleaning up GPIO")
    GPIO.cleanup()


 
   






For Viva-
---

# 📘 Viva Questions – Smoke Sensor (MQ Series) with Raspberry Pi

## 🔹 1. Basics of Smoke Sensor

**Q1. What is an MQ sensor?**
**Ans:** MQ sensors are gas detection sensors used to detect smoke and harmful gases like LPG, methane, and carbon monoxide.

**Q2. What are common types of MQ sensors?**
**Ans:** MQ-2, MQ-3, MQ-5, MQ-135, etc.

**Q3. What does a smoke sensor detect?**
**Ans:** Presence of smoke or harmful gases in the environment.

---

## 🔹 2. Working Principle

**Q4. How does an MQ sensor work?**
**Ans:** It detects gas by measuring changes in resistance of a sensing material when exposed to gases.

**Q5. Why does resistance change in presence of gas?**
**Ans:** Gas molecules interact with the sensor material, altering its conductivity.

**Q6. What is the role of the heater inside MQ sensor?**
**Ans:** It heats the sensing element to improve sensitivity and accuracy.

---

## 🔹 3. Output & Signal

**Q7. What are DO and AO pins in MQ sensor?**
**Ans:**

* DO (Digital Output) → Gives HIGH/LOW signal
* AO (Analog Output) → Gives varying voltage based on gas concentration

**Q8. What does LOW signal from DO indicate?**
**Ans:** Smoke or gas detected.

**Q9. What type of signal is used in this project?**
**Ans:** Digital signal (0 or 1).

---

## 🔹 4. Raspberry Pi & GPIO

**Q10. What is Raspberry Pi 3 used for?**
**Ans:** To read sensor output and control LED/buzzer.

**Q11. What is GPIO?**
**Ans:** Pins used to interface sensors and output devices.

**Q12. Why is GPIO set as input for sensor?**
**Ans:** To read signals from the sensor.

---

## 🔹 5. Python Programming

**Q13. What is Python used for?**
**Ans:** To process sensor data and control output devices.

**Q14. What does GPIO.input() do?**
**Ans:** Reads the sensor value.

**Q15. What does GPIO.output() do?**
**Ans:** Controls LED or buzzer.

---

## 🔹 6. Sensor Behavior & Calibration

**Q16. Why is warm-up time required for MQ sensor?**
**Ans:** To stabilize the sensor and get accurate readings.

**Q17. What is calibration in MQ sensors?**
**Ans:** Adjusting sensor readings to match accurate gas concentration.

---

## 🔹 7. Alert System

**Q18. Why is LED or buzzer used?**
**Ans:** To alert users when smoke or gas is detected.

**Q19. What is a safety monitoring system?**
**Ans:** A system that detects hazards and alerts users.

---

## 🔹 8. IoT Applications

**Q20. Where are smoke sensors used?**
**Ans:**

* Fire detection systems
* Gas leakage detection
* Smart homes
* Industrial safety

**Q21. How is this useful in IoT?**
**Ans:** Enables remote monitoring and automatic alerts.

---

## 🔹 9. Comparison & Understanding

**Q22. Difference between MQ sensor and flame sensor?**
**Ans:**

* MQ sensor → Detects gases/smoke
* Flame sensor → Detects fire (IR light)

---

## 🔹 10. Troubleshooting

**Q23. Why might sensor give false readings?**
**Ans:**

* Improper calibration
* Environmental conditions
* Interference

**Q24. Why might LED not turn ON?**
**Ans:**

* Wrong wiring
* Incorrect GPIO pin
* Code error

---

## 🔹 11. Advanced Concepts

**Q25. What is sensitivity in sensors?**
**Ans:** Ability to detect small changes in gas concentration.

**Q26. What is threshold level?**
**Ans:** The level at which sensor triggers detection.

---

## 🔹 12. Integration & Expansion

**Q27. How can this project be improved?**
**Ans:**

* Send alerts to mobile
* Integrate with cloud
* Add automatic ventilation system

**Q28. Can MQ sensor detect multiple gases?**
**Ans:** Yes, but sensitivity varies for different gases.

---

## 🔹 13. Safety & Importance

**Q29. Why are smoke sensors important?**
**Ans:** They help prevent accidents and ensure safety.

---

## 🔹 14. Conceptual Understanding

**Q30. What is embedded system?**
**Ans:** A system where software controls hardware devices.

**Q31. Why is Raspberry Pi suitable for safety systems?**
**Ans:**

* Real-time processing
* Easy sensor integration
* Internet connectivity

---

## 🔹 15. Higher-Level Thinking

**Q32. How can this system be used in industries?**
**Ans:** For monitoring gas leaks and triggering automatic shutdown systems.

---
