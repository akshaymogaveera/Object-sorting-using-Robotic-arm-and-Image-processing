# Object-sorting-using-Robotic-arm-and-Image-processing
Abstract :- 
1.The object should be placed at a particular location in front of the camera which will be be sorted depending upon their colors.    (red,blue and green *can add more colors*) by robotic arm and place them at three different angles .The image will be processed by raspberry pi using opencv library and the robotic arm will be controlled by arduino board due to its simplicity.
2.Raspberry pi will detect the color by performing various operations on the image captured and will determine the color of the object.
3.After the color detection ,rpi will send the information to arduino using 2 bits (10,01,11),1 is high and 0 is low usimg gpio pins of raspberry pi
4.The two wires will be connected from gpio pins of rpi to two digital pins of arduino using simple jumper wires(No uart is used just two simple wires which will either high or low.
5.The robotic arm will perform operation depending upon the color.
6.Arduino will control three servo motors and motor control clamp. 

  
HARDWARES USED:
1.RASPBERRY PI 2
2.ARDUINO UNO
3,USB CAMERA
4.MOTOR CONTROL I.C. (For clamp in robotic hand)
5.3 SERVO MOTORS


SOFTWARES USED:
1.PYTHON
2.OPENCV
3.ARDUINO IDE
4.NUMPY

How to run the codes..?
1.Run classmoto.ino in arduino board which controls two servo motors and a dc motor.
2.Run colordetect.py on raspberry with a USB camera.
3.Connect two wires from rpi to arduino to send the commands and another wire for ground.

 
