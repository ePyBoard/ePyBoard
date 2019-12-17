from machine import UART
ser=UART(1,115200)		# 构建UART1对象，设置波特率为115200
uartStr=b''
while True:
	if ser.any() :		#计算可以读取而不阻塞的字符数
		uartStr+=ser.read(1)  #读取1位元字符
	if '\n' in  uartStr :
		print("receive:"+bytes.decode(uartStr))
		uartStr=b''



