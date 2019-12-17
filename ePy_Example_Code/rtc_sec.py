from machine import RTC
from machine import LED

rtc=RTC()				#创建RTC对象
print(rtc.now())		#获取当前日期时间
rtc.alarm(time=10,repeat=True) #设置RTC 10秒警报, 並且重复设置

l = LED(1)	 #创建LED1为输出对象

irq_count = 0
def alarm_handler(t):			#时钟警报回调函数
	global irq_count
	if (irq_count%2) == 0:
		l.on()
	else :
		l.off()
	irq_count += 1

rtc.irq(trigger=RTC.ALARM0, handler=alarm_handler)  #创建由系统时钟警报触发的中断对象