from machine import KEY
from machine import PIN
from machine import LED
led=LED(LED.LED1)		#创建红灯LED1
led.on()				#红灯开启
def toggle(t):			#中断回调函数
	led.toggle()		#LED状态改变
k=KEY(KEY.KEYA)			#创建按键A
k.value()				#读取按键值
k.irq(trigger=PIN.IRQ_BOTH,handler=toggle) #按键上升缘或下降缘产生中断