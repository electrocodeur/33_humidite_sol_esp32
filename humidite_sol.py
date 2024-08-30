from machine import ADC,Pin
import time

moisture = ADC(Pin(35, Pin.IN))

moisture.atten(moisture.ATTN_11DB)

while True:
    value = moisture.read()
    print(value)
    time.sleep_ms(50)
