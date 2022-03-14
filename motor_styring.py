from machine import Pin, PWM, ADC
import time

pwm_r = PWM(Pin(25, Pin.OUT))
pwm_l = PWM(Pin(26, Pin.OUT))

pwm_r.freq(1000)
pwm_l.freq(1000)

pot_pin = ADC(Pin(35))
pot_pin.atten(ADC.ATTN_11DB)
pot_pin.width(ADC.WIDTH_10BIT)

while True:
    pot_val = pot_pin.read()
    
    if pot_val < 560 and pot_val > 490:
        motor_val_l = 0
        motor_val_r = 0
        pwm_l.duty(motor_val_l)
        pwm_r.duty(motor_val_r)
        
    elif pot_val >= 560:
        motor_val_l = 0
        motor_val_r = (pot_val - 512) / 2
        pwm_l.duty(int(motor_val_l*4))
        pwm_r.duty(int(motor_val_r*4))
    
    elif pot_val <= 490:
        motor_val_l = (512 - pot_val) / 2
        motor_val_r = 0
        pwm_l.duty(int(motor_val_l*4))
        pwm_r.duty(int(motor_val_r*4))
    
    print(pot_pin.read())
    print(motor_val_l, 'motor venstre')
    print(motor_val_r, 'motor høyre')
    print('')
    time.sleep_ms(25)