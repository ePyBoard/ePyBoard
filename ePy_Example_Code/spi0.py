from machine import SPI
import utime

txbuf = ['0123456789abcdef','1qaz2wsx3edc4rfv','5tgb6yhn7ujm8ikl']
fail = 0
for i in range(0,3) :
	for j in txbuf :
		print('Master Tx: ',j)
		spi0.write(j)			#SPI 0写入数据到buf
		rxbuf=spi1.read(16)		#SPI 1读取16位元
		print('Slave Rx: ',rxbuf)
		if j != rxbuf.decode("utf-8") :
			fail=fail+1
			print('rx fail')
		print('================')
	utime.sleep(1)				#延迟1秒
	
#for i in range(0,3) :
#	for j in txbuf :
#		print('Master Tx: ',j+j)
#		spi0.write(j+j)
#		rxbuf=spi1.read(32)
#		print('Slave Rx: ',rxbuf)
#		if j+j != rxbuf.decode("utf-8") :
#			fail=fail+1
#			print('rx fail')
#		print('================')
#	utime.sleep(1)
print('Total fail: ',fail)