#Linux Commands - Exploring Raspbian Operating System



1. Basic File & Directory Commands
1. man
Description: Shows manual/help for any command.
Example: man ls
 
________________________________________
2. ls
Description: Lists files in the current directory.
Examples:
ls
ls -l → detailed list
ls -a → show hidden files
 
________________________________________
3. cd
Description: Changes directory.
Examples:
cd Desktop
cd ..
cd /home/pi

 
________________________________________
4. pwd
Description: Shows current directory path.
Example: pwd

 
________________________________________
5. mkdir
Description: Creates a new folder.
Example: mkdir project

 
 
________________________________________
6. rmdir
Description: Removes empty directory.
Example: rmdir myfolder

________________________________________
7. rm
Description: Deletes files or folders.
Examples:
rm file.txt
rm -r foldername

 
________________________________________
8. cp
Description: Copies files or directories.
Examples:
cp a.txt b.txt
cp -r folder1 folder2

 
 
 
 
________________________________________
9. mv
Description: Moves or renames files.
Examples:
mv old.txt new.txt
mv file.txt /home/pi/Desktop

   
________________________________________
10. touch
Description: Creates an empty file.
Example: touch notes.txt

   
________________________________________
11. cat
Description: Displays file content.
Example: cat file.txt

 
________________________________________
12. head
Description: Shows first 10 lines of a file.
Example: head logfile.txt

 
________________________________________
13. tail
Description: Shows last 10 lines of a file.
Examples:
tail logfile.txt
tail -f logfile.txt

   
________________________________________
14. chmod
Description: Changes file permissions.
Example: chmod +x script.sh

 








________________________________________
________________________________________
2. SSH & System Commands
________________________________________
15. ssh
Description: Connects to another machine.
Example: ssh pi@192.168.1.10

 
________________________________________
16. df
Description: Shows disk usage.
Example: df -h

 ________________________________________
17. dd
Description: Copy disks/USB/SD card.
Example: dd if=/dev/sda of=backup.img

 ________________________________________
18. tree
Description: Shows folder structure.
Example: tree

 
________________________________________
19. zip
Description: Compress files.
Example:
zip files.zip file1 file2
zip -r folder.zip foldername

 
________________________________________
20. unzip
Description: Extract zip files.
Example: unzip files.zip

 
________________________________________
21. tar
Description: Create or extract tar files.
Create: tar -czvf backup.tar.gz folder/
Extract: tar -xzvf backup.tar.gz

 







 
________________________________________
________________________________________
3. Searching Commands
________________________________________
22. grep
Description: Search text inside files.
Example: grep "error" logfile.txt

 
________________________________________
23. awk
Description: Processes text line-by-line.
Example: awk '{print $1}' data.txt

 
________________________________________
24. find
Description: Search for files by name.
Examples:
find . -name "*.txt"
find / -type f -size +10M

 ________________________________________
25. whereis
Description: Shows location of commands.
Example: whereis python3

 







 

________________________________________
4. Networking Commands
________________________________________
26. ping
Description: Checks if a device is reachable.
Example: ping google.com

 
________________________________________
27. hostname
Description: Shows device name.
Example: hostname

 
________________________________________
28. ifconfig
Description: Shows IP & network info.
Example: ifconfig

 







For Viva-
---

# 📘 Viva Questions – Linux Commands (Raspberry Pi / Raspbian)

## 🔹 1. Basics of Linux & Raspbian

**Q1. What is Linux?**
**Ans:** Linux is an open-source operating system kernel used to build various OS distributions.

**Q2. What is Raspberry Pi OS?**
**Ans:** It is a Debian-based Linux OS designed specifically for Raspberry Pi hardware.

**Q3. What is a command-line interface (CLI)?**
**Ans:** CLI allows users to interact with the system by typing commands instead of using a graphical interface.

---

## 🔹 2. File & Directory Concepts

**Q4. What is a directory in Linux?**
**Ans:** A directory is a folder used to organize files in a hierarchical structure.

**Q5. What is the difference between absolute path and relative path?**
**Ans:**

* Absolute path → Full path from root (e.g., /home/pi/Desktop)
* Relative path → Path based on current directory

**Q6. What is the root directory in Linux?**
**Ans:** It is the top-most directory represented by `/`.

---

## 🔹 3. File Management Commands

**Q7. What is the purpose of the ls command?**
**Ans:** It lists files and directories in the current location.

**Q8. Why do we use cd command?**
**Ans:** To navigate between directories.

**Q9. What is the use of mkdir and rmdir?**
**Ans:**

* mkdir → Create directory
* rmdir → Remove empty directory

**Q10. What is the difference between rm and rmdir?**
**Ans:**

* rm → Deletes files and non-empty folders
* rmdir → Deletes only empty folders

**Q11. What is the function of cp and mv commands?**
**Ans:**

* cp → Copy files
* mv → Move or rename files

**Q12. What does the touch command do?**
**Ans:** Creates an empty file.

---

## 🔹 4. File Content & Viewing

**Q13. What is the difference between cat, head, and tail?**
**Ans:**

* cat → Shows full file content
* head → Shows first lines
* tail → Shows last lines

**Q14. What is the use of tail -f?**
**Ans:** It continuously monitors a file in real-time (used for logs).

---

## 🔹 5. Permissions & Security

**Q15. What is file permission in Linux?**
**Ans:** It controls who can read, write, or execute a file.

**Q16. What does chmod do?**
**Ans:** It changes file permissions.

**Q17. What are the three types of permissions?**
**Ans:** Read (r), Write (w), Execute (x)

---

## 🔹 6. System & Disk Commands

**Q18. What is the purpose of df command?**
**Ans:** Displays disk space usage.

**Q19. What is dd command used for?**
**Ans:** Used for low-level copying of disks, backups, and creating images.

**Q20. What is tree command?**
**Ans:** Displays directory structure in a tree format.

---

## 🔹 7. Compression & Archiving

**Q21. What is file compression?**
**Ans:** Reducing file size to save storage.

**Q22. Difference between zip and tar?**
**Ans:**

* zip → Compress + archive
* tar → Archive (can compress with gzip)

---

## 🔹 8. Searching & Text Processing

**Q23. What is grep used for?**
**Ans:** To search specific text in files.

**Q24. What is awk used for?**
**Ans:** For text processing and pattern scanning.

**Q25. What is find command used for?**
**Ans:** To locate files based on name, size, or type.

**Q26. What does whereis do?**
**Ans:** Finds the location of binaries and command files.

---

## 🔹 9. Networking Concepts

**Q27. What is the purpose of ping command?**
**Ans:** To test connectivity between two devices.

**Q28. What is hostname?**
**Ans:** The name assigned to a device in a network.

**Q29. What is ifconfig used for?**
**Ans:** Displays network configuration like IP address.

---

## 🔹 10. Remote Access & IoT Relevance

**Q30. What is SSH?**
**Ans:** SSH is used for secure remote access to another machine via CLI.

**Q31. Why are Linux commands important in IoT?**
**Ans:** Because most IoT devices run on Linux-based systems and require command-line control.

---

## 🔹 11. Application-Based Questions

**Q32. How can Linux commands help in IoT projects?**
**Ans:**

* File handling for logs
* Network monitoring
* Remote device control
* Automation using scripts

**Q33. Give real-life use of grep in IoT.**
**Ans:** Searching error logs in sensor data files.

---

## 🔹 12. Advanced Understanding

**Q34. What is a shell in Linux?**
**Ans:** A program that interprets user commands and communicates with the OS.

**Q35. What is scripting in Linux?**
**Ans:** Writing a sequence of commands to automate tasks.

