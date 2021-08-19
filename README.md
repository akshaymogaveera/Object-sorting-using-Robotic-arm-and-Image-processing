# **Object Sorting Using Robotic arm and Image processing**

## Watch the <a href="https://youtu.be/t3t1tSswEEQ">Video</a> of the Robotic arm in action !!

## Overview : 


1. The object should be placed *(as shown in the video)* in **between the clamp in front of the camera which will be sorted depending upon the color of the object. The robotic arm will place them at three different angles at 90,180 and 270 degrees**. The USB camera which is connected to the Raspberry PI continuously scans the live feed for a colored object.


2. Raspberry Pi will detect the color of the object using Image Processing. The colors used in this project are Red, Green and Yellow. Colors can be added by modifying the code.


3. RPI is connected to an Arduino Uno board using two Jumper wires which will send the information to arduino board using 2 bit communication method. The color is represented by binary numbers.
For Eg:- Red is represent as 10, Green as 01 and Blue as 11 where 1 is **HIGH (5 volt)** and 0 is **LOW (0 volt)**.

4. The two wires will be connected from GPIO pins (11 and 13) of Rpi to two digital pins of arduino (6 and 7) using simple jumper wires.

5. The robotic arm will perform operation depending upon the color.


6. Arduino will control three servo motors and motor control clamp. 



  
**HARDWARES USED:**


1. RASPBERRY PI 2


2. ARDUINO UNO


3. USB CAMERA


4. MOTOR CONTROL I.C. (For clamp in robotic hand)


5. Three SERVO MOTORS




**SOFTWARES USED:**


1. PYTHON


2. OPENCV


3. ARDUINO


4. NUMPY


**How to run the robot..?**


1. Ensure the two jumper cables are connected to desired pins by referring the source code.

2. Connect a 5V DC supply to power the motors.

3. Run **classmoto.ino** on Arduino board which controls three servo motors and a dc motor.

4. Run **colordetect.py** on Raspberry pi which is connected with a USB camera.





 
