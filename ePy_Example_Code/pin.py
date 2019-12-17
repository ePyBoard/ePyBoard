from machine import PIN
from machine import LED
total_pin = 35
pin_title='P'
pin_num=0
failNum=0
led=LED(1)
led.on()
led.off()
irq_count = 0
def count(t):
	global irq_count
	if irq_count < 5:
		irq_count = irq_count+1
	else :
		irq_count = 0

while pin_num < total_pin:
    if pin_num == 17 or pin_num == 18:
        pin_num += 1
        continue
    gpio_set=pin_title+str(pin_num)
    p_test=PIN(gpio_set)				#创建I/O
    p_test.mode(PIN.OUT)				#设置引脚模式为输出
    p_test.drive(PIN.LOW_POWER)			#设置引脚驱动强度
    p_test.value(1)						#设置引脚的值
    print(p_test)
    cmp_str = "Pin('" + gpio_set + "', mode=Pin.OUT, pull=Pin.INACTIVE, drive=Pin.LOW_POWER, alt=0)"
    if str(p_test) != cmp_str and p_test.value() != 1:
        failNum+=1
        break
    p_test.irq(trigger=PIN.IRQ_BOTH,handler=count)	#调用中断处理程序
    p_test.value(0)
    p_test.value(1)
    if irq_count!=2:
        failNum+=1
        break
    p_test.deinit()
    pin_num=pin_num+1
    irq_count=0
if failNum==0:
    print('test all pass!')
else:
    print('test fail num',failNum)