from machine import *
buf=bytearray(8)							#
buf1=[0x01,0x02,0x03,0x04,0x05,0x6,0x7,0x8]
tmp=I2C(1,100000)			#创建频率为100khz的I2C外设,选择要使用的外设I2C 1
tmp.read(1,0x40,buf,8,1)	#读取8个字节从从设备地址 40
tmp.write(1,0x40,buf1,8,1)	#写8个字节到从设备地址 40
tmp.read(1,0x40,buf,8,1)	#读取8个字节从从设备地址 40
buf
