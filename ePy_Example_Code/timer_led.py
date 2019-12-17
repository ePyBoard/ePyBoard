from machine import Timer
from machine import LED

tim = Timer(1, mode=Timer.PERIODIC)		#创建Timer 1为一个频率定期运行对象
tim_a = tim.channel(Timer.CH_0,freq=1)		#创建Timer A其频率为1Hz

l = LED(1)

led_off = 2
led_on = 3
irq_count = 0
def toggle(t):					#中断回调函数
	global irq_count
	if irq_count < led_off:
		l.off()
	else :
		l.on()
	if irq_count < (led_off+led_on-1):
		irq_count = irq_count+1
	else :
		irq_count = 0

tim_a.irq(trigger=Timer.TIMEOUT,handler=toggle)	#回调函数将使用设置的频率定期执行中断