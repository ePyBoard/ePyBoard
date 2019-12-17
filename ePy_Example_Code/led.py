from machine import LED
total_pin = 4					
pin_num=1

while pin_num < (total_pin+1): 
 led_test=LED(int(pin_num))		#LED1~4循序亮灭
 print(led_test)
 led_test.on()
 for j in range(0,5000,1):
  continue
 led_test.off()
 for j in range(0,5000,1):
  continue
 led_test.toggle()
 for j in range(0,5000,1):
  continue
 led_test.toggle()
 for j in range(0,5000,1):
  continue
 pin_num=pin_num+1