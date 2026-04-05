Practical 7
Using Temperature & Humidity Sensor with Raspberry Pi

To interface a DHT11 Temperature & Humidity Sensor with Raspberry Pi 3 and display the temperature and humidity values using Python.

Theory about Temperature & Humidity sensor DHT11 

The DHT11 is a basic, low-cost digital temperature and humidity sensor. It uses a capacitive humidity sensor and a thermistor to measure the surrounding air, and spits out a digital signal on the data pin (no analog input pins needed). It's fairly simple to use, but requires careful timing to grab data.


Components Required
•	Raspberry Pi 3
•	DHT11 Temperature & Humidity Sensor (module preferred)
•	Jumper wires (Male–Female)
•	Breadboard (optional)
•	Micro-SD card with Raspberry Pi OS
•	Internet connection (for library installation)





Pin connections

| DHT11 Pins  | Raspberry Pi Pins | GPIO Numbering |
|-------------|-------------------|----------------|
| VCC (+)     | Pin 1             | 3.3V           |
| Data (Out)  | Pin 7             | GPIO 4         |
| GND (-)     | Pin 6             | Ground         |




Install Required Libraries

Directly install the libray using Thonny > Manage Packages > Search for Adafruit_DHT > Install
•	sudo apt install python3-pip  (if already installed need not install again)
•	pip3 install Adafruit_DHT

Digital Temperature and Humidity Sensor
 
Version :- DHT11
 
 
 





Code: -
'''
To interface a DHT11 Temperature & Humidity Sensor with Raspberry Pi 3
and display the temperature and humidity values using Python.
'''

import Adafruit_DHT
import time

# Sensor type
sensor = Adafruit_DHT.DHT11

# GPIO pin where DATA is connected
gpio_pin = 4

while True:
    humidity, temperature = Adafruit_DHT.read(sensor, gpio_pin)

    if humidity is not None and temperature is not None:
        print("Temperature = {:.1f}°C".format(temperature))
        print("Humidity = {:.1f}%".format(humidity))
        print("------------------------------")
    else:
        print("Failed to retrieve data from sensor")

    time.sleep(2)



 





For Viva-

# 📘 Viva Questions – DHT11 Temperature & Humidity Sensor (IoT)

## 🔹 1. Basics of Sensor

**Q1. What is a DHT11 sensor?**
**Ans:** DHT11 is a low-cost digital sensor used to measure temperature and humidity of the surrounding environment.

**Q2. What parameters does DHT11 measure?**
**Ans:** Temperature (°C) and humidity (%).

**Q3. What type of sensor is DHT11?**
**Ans:** It is a digital sensor.

---

## 🔹 2. Working Principle

**Q4. How does DHT11 measure humidity?**
**Ans:** It uses a capacitive humidity sensor that changes capacitance based on moisture in the air.

**Q5. How does it measure temperature?**
**Ans:** It uses a thermistor whose resistance varies with temperature.

**Q6. Why does DHT11 give digital output instead of analog?**
**Ans:** It has an internal ADC that converts signals into digital form.

---

## 🔹 3. Raspberry Pi & GPIO

**Q7. What is Raspberry Pi 3 used for here?**
**Ans:** It reads sensor data and displays temperature and humidity.

**Q8. What is GPIO?**
**Ans:** Pins used to connect and communicate with external devices.

**Q9. Why is only one data pin used in DHT11?**
**Ans:** Because it uses a single-wire digital communication protocol.

---

## 🔹 4. Python & Libraries

**Q10. What is Python used for?**
**Ans:** To write programs that read and display sensor data.

**Q11. What is Adafruit_DHT library?**
**Ans:** A Python library used to interface DHT sensors with Raspberry Pi.

**Q12. What does Adafruit_DHT.read() do?**
**Ans:** It reads temperature and humidity values from the sensor.

---

## 🔹 5. Data Handling & Output

**Q13. Why do we check if values are not None?**
**Ans:** Because sensor readings may fail due to timing issues.

**Q14. Why is delay required between readings?**
**Ans:** DHT11 needs time to stabilize before next reading.

---

## 🔹 6. Sensor Characteristics

**Q15. What is the accuracy of DHT11?**
**Ans:**

* Temperature: ±2°C
* Humidity: ±5%

**Q16. What is the range of DHT11?**
**Ans:**

* Temperature: 0°C to 50°C
* Humidity: 20% to 90%

---

## 🔹 7. IoT Applications

**Q17. Where is DHT11 used in real life?**
**Ans:**

* Weather monitoring
* Smart homes
* HVAC systems
* Agriculture

**Q18. How is this useful in IoT?**
**Ans:** It helps monitor environmental conditions remotely.

---

## 🔹 8. Comparison Questions

**Q19. Difference between DHT11 and DHT22?**
**Ans:**

* DHT11 → Low cost, less accurate
* DHT22 → Higher accuracy, wider range

**Q20. Difference between analog and digital sensors?**
**Ans:**

* Analog → Continuous values
* Digital → Discrete values (0/1)

---

## 🔹 9. Troubleshooting

**Q21. Why might the sensor fail to give readings?**
**Ans:**

* Wiring issue
* Timing problem
* Power supply issue

**Q22. Why is stable power important?**
**Ans:** Sensor requires consistent voltage for accurate readings.

---

## 🔹 10. Advanced Concepts

**Q23. What is calibration in sensors?**
**Ans:** Adjusting sensor output to match accurate values.

**Q24. What is sampling rate?**
**Ans:** Frequency at which sensor readings are taken.

---

## 🔹 11. Integration & Expansion

**Q25. How can this project be extended?**
**Ans:**

* Send data to cloud
* Display on mobile app
* Add alerts for high temperature

**Q26. Can this sensor be used with other controllers?**
**Ans:** Yes, with Arduino, ESP8266, etc.

---

## 🔹 12. Conceptual Understanding

**Q27. What is embedded system?**
**Ans:** A system where software controls hardware devices.

**Q28. Why is Raspberry Pi suitable for IoT sensing?**
**Ans:**

* Supports sensors
* Easy programming
* Internet connectivity
* Real-time data processing

---

## 🔹 13. Real-World Thinking

**Q29. Why is monitoring temperature and humidity important?**
**Ans:**

* For comfort
* For industrial processes
* For agriculture

**Q30. How does this project help in smart environment systems?**
**Ans:** It enables automatic control based on environmental data.

---
