from machine import RTC
from machine import LED

rtc=RTC(datetime=(2019, 4, 25, 9, 0, 0))  #创建RTC对象, 设定时间为2019/4/25 9:00:00
print(rtc.now())						  #获取当前日期时间
rtc.alarm(time=(2019, 4, 25, 9, 1, 30),repeat=False)	#设置RTC警报为2019/4/25 9:01:30

l = LED(1)			 #创建LED1为输出对象,

def alarm_handler(t):
	l.on()							#时钟警报触发时,P21输出为高

rtc.irq(trigger=RTC.ALARM0, handler=alarm_handler)	#创建由系统时钟警报触发的中断对象