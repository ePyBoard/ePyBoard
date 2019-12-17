from machine import SPI
import utime

txbuf = ['0123456789abcdef','1qaz2wsx3edc4rfv','5tgb6yhn7ujm8ikl']
dummy = '0000000000000000'
rxbuf = bytearray(16)
fail = 0
for i in range(0,3) :
	for j in txbuf :
		print('Slave Tx: ',j)
		spi1.write(j)				#SPI 1写入数据到buf
		spi0.write_readinto(dummy,rxbuf)	#SPI 0在读取到rxbuf时, 写入来自dummy的字节
		print('Master Rx: ',rxbuf)
		if j != (bytes(rxbuf)).decode("utf-8") :
			fail=fail+1
			print('rx fail')
		print('================')
	utime.sleep(1)
	
#rxbuf = bytearray(32)
#for i in range(0,3) :
#	for j in txbuf :
#		print('Slave Tx: ',j+j)
#		spi1.write(j+j)
#		spi0.write_readinto(dummy+dummy,rxbuf)
#		print('Master Rx: ',rxbuf)
#		if j+j != (bytes(rxbuf)).decode("utf-8") :
#			fail=fail+1
#			print('rx fail')
#		print('================')
#	utime.sleep(1)
print('Total fail: ',fail)	