import RPi.GPIO as GPIO
import time 

colors = [0xFF0000, 0x0000FF]
pins = {'pin_R':11, 'pin_B':13}

# Make the pins to be based on physical location
GPIO.setmode(GPIO.BOARD)

for i in pins:
    GPIO.setup(pins[i], GPIO.OUT)
    # Produce output when input voltage is low
    GPIO.output(pins[i], GPIO.LOW)

p_R = GPIO.PWM(pins['pin_R'], 2000)
p_B = GPIO.PWM(pins['pin_B'], 5000)

# Make the leds start off
p_R.start(100)
p_B.start(100)

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def setColor(col):
    R_val = (col & 0x00FFFF)
    B_val = (col & 0xFFFF00)

    R_va = map(R_val, 0, 255, 0, 100)
    B_va = map(B_val, 0, 255, 0, 100)

    # set conditions for the leds to turn on when duty cycle is 0 and to turn off when duty cycle is 100
    if R_va == 100:
        p_R.ChangeDutyCycle(100)
    if R_va == 0:
        p_R.ChangeDutyCycle(0)
        time.sleep(1)
        p_R.ChangeDutyCycle(100)
        time.sleep(0.5)
    
    if B_va == 100:
        p_B.ChangeDutyCycle(100)
    if B_va == 0:
        p_B.ChangeDutyCycle(0)
        time.sleep(2)
        p_B.ChangeDutyCycle(100)
        time.sleep(0.5)
def main():
    try:
        while True:
            # Morse code for T
            setColor(colors[1])
            p_B.ChangeDutyCycle(100)
            time.sleep(4)
            # Morse code for E
            setColor(colors[0])
            p_R.ChangeDutyCycle(100)
            time.sleep(3.5)
            # Morse code for S
            setColor(colors[0])
            setColor(colors[0])
            setColor(colors[0])
            p_R.ChangeDutyCycle(100)
            time.sleep(3.5)
            # Morse code for T
            setColor(colors[1])
            p_B.ChangeDutyCycle(100)
            time.sleep(3.5)
            # Morse code for 1
            setColor(colors[0])
            setColor(colors[1])
            setColor(colors[1])
            setColor(colors[1])
            setColor(colors[1])
            p_B.ChangeDutyCycle(100)
            time.sleep(3.5)
            # Morse code for 2
            setColor(colors[0])
            setColor(colors[0])
            setColor(colors[1])
            setColor(colors[1])
            setColor(colors[1])
            p_B.ChangeDutyCycle(100)
            time.sleep(3.5)
            # Morse code for 3
            setColor(colors[0])
            setColor(colors[0])
            setColor(colors[0])
            setColor(colors[1])
            setColor(colors[1])
            p_B.ChangeDutyCycle(100)
            time.sleep(10)
            
           

            
    except KeyboardInterrupt:
        p_R.stop()
        p_B.stop()
        for i in pins:
            GPIO.output(pins[i], GPIO.HIGH)
        GPIO.cleanup()

if __name__=="__main__":
    main()