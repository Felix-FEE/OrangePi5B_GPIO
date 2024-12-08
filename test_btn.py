from OrangePi5B_GPIO import class_WOP5B
import time
btn5 = class_WOP5B(5)
btn5.set_Pin("in")
while (1):
    state = btn5.gpio_Read_Pin()
    if state == '0':
        print("Nút nhấn")
    else:
        print("Nút nhả")
    time.sleep(1)