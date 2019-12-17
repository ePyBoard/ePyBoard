from machine import SPI
import utime

rate = [20000000,10000000,5000000]
spi0=SPI(0,mode=SPI.MASTER,baudrate=rate[0])	#创建SPI 0为"主模式", 波特率是20MHz 
print(spi0)
spi1=SPI(1,mode=SPI.SLAVE,baudrate=rate[0])		#创建SPI 1为"丛模式", 波特率是20MHz
print(spi1)