import RPi.GPIO as GPIO
#CONNECT THESE TWO PINS TO ARDUINO PINS
pin=11
pin1=13
#GPIO PINS TO SEND TWO BINARY DATA TO ARDUINO 10,01 OR 11 DEPENDING ON COLOR
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pin,GPIO.OUT)
GPIO.setup(pin1,GPIO.OUT)

a=0
import cv2
import numpy as np
import time
cap = cv2.VideoCapture(0)
while True:
    cr=0
    cb=0
    cg=0
    ret,im = cap.read() #READ FRAMES
    hsv = cv2.cvtColor(im,cv2.COLOR_BGR2HSV) #CONVERT FRAMES FROM COLOR TO HSV
   #lower mask red (IF YOU WANT TO ADD RED COLOR TO THIS PROGROM UNCOMMENT IT)
    '''
    THE PIXELS IN THE IMAGE IN THE RANGE IN cv2.inRange() will be converted to white pixels and rest black
    
    
    
    lower_red = np.array([0,50,50])
    upper_red = np.array([20,255,255])
    mask0 = cv2.inRange(hsv, lower_red ,upper_red)
   
     #upper mask red
    lower_red = np.array([170,50,50])
    upper_red = np.array([180,255,255])
    mask1 = cv2.inRange(hsv, lower_red ,upper_red)
    mask=mask0+mask1'''
    #yellow
    lowyellow=np.array([20,50,100],dtype=np.uint8)
    highyellow=np.array([42,255,255],dtype=np.uint8)
    mask = cv2.inRange(hsv, lowyellow,highyellow)
    #blue
    lowblue=np.array([110,130,50],dtype=np.uint8)
    highblue=np.array([130,255,255],dtype=np.uint8)
    maskb = cv2.inRange(hsv, lowblue,highblue)
    #green
    lowgreen=np.array([44,54,63],dtype=np.uint8)
    highgreen=np.array([90,255,255],dtype=np.uint8)
    maskg = cv2.inRange(hsv, lowgreen,highgreen)
    
    cv2.imshow('mask red',mask)
    #cv2.imshow('mask blue',maskb)
    #cv2.imshow('mask green',maskg)
    cr=cv2.countNonZero(mask) #COUNTS THE WHITE PIXELS IN IMAGE THAT CONTAINS WHITE AND BLACK PIXELS
    cb=cv2.countNonZero(maskb)
    cg=cv2.countNonZero(maskg)
    if(cb>4000):
        print 'blue' #SEND 1 0 TO ARDUINO
        GPIO.output(pin,GPIO.HIGH)
        GPIO.output(pin1,GPIO.LOW)
        time.sleep(1)
        GPIO.output(pin,GPIO.LOW)
        GPIO.output(pin1,GPIO.LOW)
    elif(cg>4000):
        print 'green'#SEND 0 1 TO ARDUINO
        GPIO.output(pin,GPIO.LOW)
        GPIO.output(pin1,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pin,GPIO.LOW)
        GPIO.output(pin1,GPIO.LOW)
    elif(cr>8000):
        print 'yellow' #SEND 1 1 TO ARDUINO
        GPIO.output(pin,GPIO.HIGH)
        GPIO.output(pin1,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pin,GPIO.LOW)
        GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin,GPIO.LOW)
    GPIO.output(pin1,GPIO.LOW)
        
    #print ('red=',cr)
    #print ('blue',cb)
    #print ('green',cg)
    if cv2.waitKey(1) & 0xff==ord('q'):      
        break    
#cv2.waitKey()
cap.release()
cv2.destroyAllWindows()
    

