import subprocess
class class_WOP5B:
    def __init__(self, wiring_pin):
        self.wiring_pin = wiring_pin
    
    def check_Pin(self):
        if self.wiring_pin < 0 or self.wiring_pin > 16:
            return "Wiring_pin must in (0 -> 16)"
        else:
            return True
        
    def set_Pin(self, mode_in_out):
        '''
        wiring_pin: You can check wiring_pin: run terminal: gpio readall
        wiring_pin: 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
        mode: in, out
        '''
        if self.check_Pin() == True:
           
            mode_in_out = str(mode_in_out)
            if mode_in_out != "in" and mode_in_out != "out":
                return "Mode must (in or out)"
            else:
                command_setPin = ["gpio", "mode", f'{self.wiring_pin}', mode_in_out]
                subprocess.run(command_setPin, check=True)
                return True
        else:
            print ("Wiring_pin must in (0 -> 16)")
            return False
        
    def gpio_Write_Pin(self, output_level):
        if self.check_Pin():
            if output_level != 1 and output_level != 0:
                print("Level must 0 or 1")
                return False
            else:
                cmd_output = ["gpio", "write", f'{self.wiring_pin}', f'{output_level}']
                subprocess.run(cmd_output, check=True)
                return True
        else:
            return None
        
    def gpio_Read_Pin(self):
        
        if self.check_Pin():
            if self.wiring_pin not in [5,7,8,10]:
                print("Read Pin Input Only (Wiring Pin 5,7,8,10)")
                return None
            else:
                cmd_Read_Pin = ["gpio", "read", f'{self.wiring_pin}']
                result = subprocess.run(cmd_Read_Pin, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                logic_level = result.stdout.decode().strip()  # Chuyển đổi kết quả từ bytes sang string
                print("Logic: ", logic_level)
                return logic_level
        else:
            print ("Wiring_pin must in (0 -> 16)")
            return None
        
    
    
    

             