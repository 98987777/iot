#Practical 4
#Controlling LED using Telegram App

Steps: -
1.	Click on Raspberry Icon > Programming > Thonny Python IDE

2.	On the Right Side Click on the Switch to regular mode > Close and reopen Thonny

3.	From the upper tab click on Tools > Manage Packages > Search telepot and Install
OR Use Below Steps
In the raspberry pi PC open Terminal and type 
pip3 install telepot 
 
If not getting install or connection error go to File explorer > /etc > dhcpcd.conf file 
Edit the IP address earlier it was – 192.168.0.1   Change to 192.168.2.1
 





| LED Terminal         | Pin Number        | GPIO Number |
|---------------------|------------------|-------------|
| Red Positive        | Pin 15 (LED 1)   | GPIO 22     |
| Blue Positive     | Pin 16 (LED 2)   | GPIO 23     |
| Ground for LED 1    | Pin 9            | GND         |
| Ground for LED 2    | Pin 6            | GND         |


4.	Install Telegram app in phone.

5.	Search BotFather and Add

6.	Click on Open > create a bot > name the bot and username

7.	Copy the bot link for the further coding.
 
Code: -
import telepot
from telepot.loop import MessageLoop
from datetime import datetime
import RPi.GPIO as GPIO
from time import sleep

red = 22
yellow = 23

now = datetime.now()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(red, GPIO.OUT)
GPIO.output(red, 0)

GPIO.setup(yellow, GPIO.OUT)
GPIO.output(yellow, 0)

def action(msg):
    chat_id = msg["chat"]["id"]
    command = msg["text"]
    print("Recieved: " + command)

    if "on" in command.casefold():
        message = "on "
        if "red" in command.casefold():
            message = message + "red"
            GPIO.output(red, 1)
        elif "yellow" in command.casefold():
            message = message + " yellow"
            GPIO.output(yellow, 1)

        message = message + " light(s)"
        telegram_bot.sendMessage(chat_id, message)

    if "off" in command.casefold():
        message = "off "
        if "red" in command.casefold():
            message = message + " red"
            GPIO.output(red, 0)
        elif "yellow" in command.casefold():
            message = message + " yellow"
            GPIO.output(yellow, 0)

        message = message + " light(s)"
        telegram_bot.sendMessage(chat_id, message)

telegram_bot = telepot.Bot("8293210490:AAGfJLjRkgsJTE3DbbAuY_pHtWl1sOMSrLA")
print(telegram_bot.getMe())
MessageLoop(telegram_bot, action).run_as_thread()

try:
    while True:
        sleep(10)

finally:
    GPIO.output(red, 0)
    GPIO.output(yellow, 0)
    GPIO.cleanup()




8.	In Telegram Search BotFather > Open the chats 

9.	Message /mybots
 
10.	Then choose the mybots and click on the @username

11.	Also Run the python code

12.	Message -  /start
On red
On yellow
On red and yellow



  






For Viva-

# 📘 Viva Questions – LED Control using Telegram Bot (IoT)

## 🔹 1. IoT & Communication Basics

**Q1. What is IoT (Internet of Things)?**
**Ans:** IoT is a network of physical devices connected to the internet that can collect, send, and act on data.

**Q2. How does IoT enable remote control of devices?**
**Ans:** Devices communicate over the internet using protocols and APIs, allowing users to control them from anywhere.

---

## 🔹 2. Telegram Bot Concept

**Q3. What is Telegram Bot?**
**Ans:** A Telegram Bot is an automated program that interacts with users via messages and performs tasks.

**Q4. What is the role of BotFather?**
**Ans:** BotFather is used to create and manage Telegram bots and generate API tokens.

**Q5. What is a bot token?**
**Ans:** A unique authentication key used to connect your program with the Telegram bot.

---

## 🔹 3. Python & Telepot Library

**Q6. What is Python used for in this project?**
**Ans:** Python is used to write the program that connects Telegram commands to hardware control.

**Q7. What is the telepot library?**
**Ans:** Telepot is a Python library used to interact with the Telegram Bot API.

**Q8. What does MessageLoop do?**
**Ans:** It continuously listens for incoming messages from Telegram and triggers actions.

---

## 🔹 4. GPIO & Hardware Control

**Q9. What is GPIO?**
**Ans:** GPIO pins allow Raspberry Pi to interact with external devices like LEDs.

**Q10. How is LED controlled in this project?**
**Ans:** By sending HIGH or LOW signals to GPIO pins through Python code.

**Q11. Why are multiple GPIO pins used?**
**Ans:** To control multiple LEDs independently.

---

## 🔹 5. Program Logic & Working

**Q12. How does the system respond to Telegram messages?**
**Ans:** The bot reads the message, processes keywords (like "on" or "off"), and performs corresponding actions.

**Q13. What is the role of string processing in this code?**
**Ans:** It helps identify commands like “on red” or “off yellow”.

**Q14. Why is casefold() used?**
**Ans:** To make command checking case-insensitive.

---

## 🔹 6. Networking & API Concepts

**Q15. What is an API?**
**Ans:** API (Application Programming Interface) allows communication between different software systems.

**Q16. How does Telegram communicate with Raspberry Pi?**
**Ans:** Through the internet using Telegram Bot API.

---

## 🔹 7. Real-Time Processing

**Q17. What is real-time communication in IoT?**
**Ans:** Instant data exchange between user and device without delay.

**Q18. Why is continuous loop required in the program?**
**Ans:** To keep the system running and listening for new commands.

---

## 🔹 8. Security Concepts

**Q19. Why should bot tokens be kept secret?**
**Ans:** Anyone with the token can control your bot and connected devices.

**Q20. What are risks in IoT remote control systems?**
**Ans:** Unauthorized access, hacking, and data breaches.

---

## 🔹 9. Application-Based Questions

**Q21. What are real-life applications of this project?**
**Ans:**

* Smart home automation
* Remote lighting control
* Industrial automation

**Q22. How can this system be improved?**
**Ans:**

* Add sensors
* Use voice commands
* Integrate with cloud platforms

---

## 🔹 10. Troubleshooting & Understanding

**Q23. Why might the bot not respond?**
**Ans:**

* Internet issue
* Wrong token
* Code not running

**Q24. Why might LED not turn ON/OFF?**
**Ans:**

* Incorrect wiring
* Wrong GPIO pin
* Code error

---

## 🔹 11. Advanced Concepts

**Q25. What is automation in IoT?**
**Ans:** Automatic control of devices without manual intervention.

**Q26. What is event-driven programming?**
**Ans:** Execution of code based on events (like receiving a message).

---

## 🔹 12. Integration & Future Scope

**Q27. How can this project be integrated with AI?**
**Ans:** By adding voice assistants or smart decision-making systems.

**Q28. Can this system control other devices?**
**Ans:** Yes, motors, fans, relays, sensors, etc.

---

## 🔹 13. Conceptual Understanding

**Q29. What is embedded system programming?**
**Ans:** Programming hardware devices to perform specific tasks.

**Q30. Why is Raspberry Pi suitable for IoT automation?**
**Ans:**

* Supports internet connectivity
* GPIO pins available
* Easy integration with APIs
* Supports multiple programming languages

---
