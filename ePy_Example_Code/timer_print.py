from machine import Timer
from machine import PIN

tim = Timer(1, mode=Timer.PERIODIC)	#创建Timer 1为一个频率定期运行对象
tim_a = tim.channel(Timer.A,freq=1)	#创建Timer A其频率为1Hz

p = PIN('P21', mode=PIN.OUT)

print_sec = 3
irq_count = 0
print_count = 0
def toggle(t):
	global irq_count
	global print_count
	if (irq_count%print_sec) == 0:
		print(print_count)
		print_count=print_count+1
	irq_count=irq_count+1

tim_a.irq(trigger=Timer.TIMEOUT,handler=toggle)	#回调函数将使用设置的频率定期执行中断