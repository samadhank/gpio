import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
try:
    while(1):
        input_status=GPIO.input(16)
        if input_status==True:
            GPIO.output(18,1)
            time.sleep(.2)
            print('Hello World...')
        else:
            GPIO.output(18,0)
except:
    GPIO.cleanup()

    
