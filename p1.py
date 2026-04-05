# Installing Software In Raspberry Pi

#Steps

1.	Take out the Mouse, Keyboard and Monitor wires from the CPU 

2.	And then connect those to the Raspberry Pi

3.	Insert the Memory card keeping the yellow lines circuit downside

4.	Connect the Charger to the plug and to the raspberry pi

5.	Click on Raspbian full

6.	Click on install icon

7.	Confirm the warning to yes

8.	It will take enough time to install

9.	Then set country, time zone, language

10.	Add a password (123) 

11.	Skip Wifi, update software and click on Restart 

12.	Take out the Ethernet cable of CPU and connect that to the Raspberry Pi

13.	Open Command Prompt and type ifconfig  check the ip address 2nd line inet 
192.168.2.91

14.	Type this in command prompt – 
ls /etc/dhcpcd.conf  --- this command is used to show the listing of the files
nano /etc/dhcpcd.conf --- this command is used to open a terminal based text editor
(For to change the below IP Address use this nano command)
to make changes in the static ip configuration

15.	Uncomment these lines
Interface eth0
Static ip_address= 192.168.2.47/24
Static routers = 192.168.0.1
And write new line under static domain_name_server_name=192.168.0.1 8.8.8.8……..
static domain_name_server_name= 8.8.8.8 
If it doesn’t changes the ip address then type 
set Static ip_address= 192.168.2.47/24
set Static routers = 192.168.0.1
set static domain_name_server_name= 8.8.8.8 

 
16.	 Then do ctrl O to save 

17.	Then enter 

18.	Then ctrl x to exit

19.	Then reboot

20.	Again check the ip address by typing ifconfig
 
21.	After rebooting check again the ip address it should be updated

22.	In another PC command prompt type – ping 192.168.2.47
Check if the packets are received 

23.	In Raspberry Pi PC go to the menu in Preferences > Raspberry Pi Configuration > Interfaces – enable the SSH and VNC

24.	For remote access of the ip address in the another machine 
download VNC viewer in another pc 
Untick the anonymously……
Don’t sign in

25.	Then Type the IP address of the Raspberry Pi (192.168.2.47) in VNC

26.	Enter and type username (pi) and password (123)
 
27.	Now Install VNC Putty from local server (192.168.2.2) soft >  
VNC Putty is for Accessing the command prompt of Raspberry Pi PC on Another PC

28.	 In that add the raspberry pi IP address (192.168.2.47)
 
29.	Then click ok and a command prompt will open there add the username (pi) and password (123)
 










For Viva-

---

# 📘 Viva Questions – Raspberry Pi Installation & Remote Access

## 🔹 1. Basics of Raspberry Pi

**Q1. What is Raspberry Pi?**
**Ans:** Raspberry Pi is a small, low-cost single-board computer used for learning programming, IoT projects, and embedded systems.

**Q2. What are the main components of Raspberry Pi?**
**Ans:** CPU, RAM, GPIO pins, USB ports, HDMI port, SD card slot, Ethernet/Wi-Fi module.

**Q3. Why is Raspberry Pi widely used in IoT?**
**Ans:** Because it is affordable, supports networking, has GPIO pins for hardware interfacing, and runs a full OS.

---

## 🔹 2. Operating System & Installation

**Q4. What is Raspberry Pi OS?**
**Ans:** It is a Linux-based operating system specifically designed for Raspberry Pi.

**Q5. Why do we need an OS for Raspberry Pi?**
**Ans:** To manage hardware, run applications, and provide a user interface.

**Q6. What is the role of an SD card in Raspberry Pi?**
**Ans:** It acts as storage for the OS and files, similar to a hard disk.

---

## 🔹 3. Networking Concepts

**Q7. What is an IP address?**
**Ans:** It is a unique numerical identifier assigned to each device on a network.

**Q8. What is the difference between static IP and dynamic IP?**
**Ans:**

* Static IP: Fixed and manually assigned
* Dynamic IP: Automatically assigned by DHCP server

**Q9. Why do we configure a static IP in Raspberry Pi?**
**Ans:** To ensure the device always has the same IP for remote access and server applications.

**Q10. What is DHCP?**
**Ans:** Dynamic Host Configuration Protocol automatically assigns IP addresses to devices.

---

## 🔹 4. Remote Access Technologies

**Q11. What is SSH?**
**Ans:** SSH is a protocol used to securely access and control a remote system via command line.
SSH stands for Secure Shell and is used for secure remote login and command execution.

**Q12. What is VNC Viewer?**
**Ans:** VNC Viewer allows graphical remote access to another computer’s desktop.

**Q13. Difference between SSH and VNC?**
**Ans:**

* SSH → Command-line access
* VNC → Graphical desktop access

**Q14. What is PuTTY?**
**Ans:** PuTTY is a client used to connect to remote systems via SSH.

---

## 🔹 5. Linux Commands & Configuration

**Q15. What is the purpose of configuration files in Linux?**
**Ans:** They store system settings and allow customization of system behavior.

**Q16. What is the role of dhcpcd.conf file?**
**Ans:** It is used to configure network settings like static IP in Raspberry Pi.

**Q17. What is a terminal-based editor?**
**Ans:** A text editor used in command line (e.g., nano, vi).

---

## 🔹 6. Connectivity & Testing

**Q18. What is the purpose of the ping command?**
**Ans:** To check connectivity between two devices on a network.

**Q19. What does packet loss indicate?**
**Ans:** Network issues or connection failure.

**Q20. Why is Ethernet preferred over Wi-Fi in some cases?**
**Ans:** It provides more stable and faster connection.

---

## 🔹 7. Security & Best Practices

**Q21. Why should default passwords be changed?**
**Ans:** To prevent unauthorized access and improve security.

**Q22. What are risks of enabling SSH?**
**Ans:** Unauthorized remote access if not secured properly.

---

## 🔹 8. Application-Based Questions

**Q23. How can Raspberry Pi be used as a server?**
**Ans:** It can host web servers, databases, or IoT services.

**Q24. Give real-life applications of Raspberry Pi in IoT.**
**Ans:**

* Home automation
* Smart surveillance
* Weather monitoring
* Smart agriculture

---

## 🔹 9. Troubleshooting Questions

**Q25. What will you do if Raspberry Pi is not connecting to network?**
**Ans:** Check cables, IP configuration, router, and network settings.

**Q26. What if VNC is not working?**
**Ans:** Ensure VNC is enabled, correct IP is used, and both devices are on same network.

---

## 🔹 10. Advanced Conceptual Questions

**Q27. What is headless mode in Raspberry Pi?**
**Ans:** Running Raspberry Pi without monitor, using remote access.

**Q28. What is port number in networking?**
**Ans:** A number used to identify specific services on a device (e.g., SSH uses port 22).

---

