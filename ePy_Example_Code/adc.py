from machine import ADC
import utime
tmp = ADC(0)		#创建ADC物件
tmp.init(4)			#启动ADC通道4
tmp.init(5)			#启动ADC通道5
tmp.channel(4)		#创建ADC引脚 偵測光亮
adc_buff=0
for y in range(0,9):
	adc_buff = tmp.read() #读取ADC数据
	print(adc_buff)		#打印ADC值
	utime.sleep_ms(100)
tmp.channel(5)		#创建ADC引脚
adc_buff=0
for y in range(0,9):
	adc_buff = tmp.read()#读取ADC数据 偵測聲音
	print(adc_buff)		#打印ADC值
	utime.sleep_ms(100)