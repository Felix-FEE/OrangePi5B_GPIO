import OrangePi5B_GPIO
import time
Obj_GPIO = OrangePi5B_GPIO.GPIO_OrangePi(2)
Obj_GPIO.set_Pin("out")
while True:
    Obj_GPIO.gpio_Write_Pin("1")
    time.sleep(1)
    Obj_GPIO.gpio_Write_Pin("0")
    time.sleep(1)