from machine import Accel	
import utime

accel = Accel()					#创建3轴G-Sensor

try:
	while True:
		print('x:',accel.x())	#读取X轴数值
		print('y:',accel.y())	#读取Y轴数值
		print('z:',accel.z())	#读取Z轴数值
		utime.sleep(1)			#延迟1秒

finally:
	accel.deinit()				#关闭G-sensor