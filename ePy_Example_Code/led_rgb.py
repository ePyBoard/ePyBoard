from machine import LED
l=LED(LED.RGB)				#创建RGB LED
print('show render')
for i in range(0,256,1):	#RGB渐亮渐灭变化
    for j in range(1,6,1):
        l.rgb_write(j,i,0,0) 
for i in range(0,256,1):
    for j in range(1,6,1):
        l.rgb_write(j,255,i,0)
for i in range(0,256,1):
    for j in range(1,6,1):
        l.rgb_write(j,255,255,i)
times = 0
while times < 10 :
    for i in range(255,1,-1):
        for j in range(1,6,1):
            l.rgb_write(j,i,i,i)
    for i in range(0,256,1):
        for j in range(1,6,1):
            l.rgb_write(j,i,i,i)
    times = times +1
for i in range(255,1,-1):
    for j in range(1,6,1):
        l.rgb_write(j,i,i,i)