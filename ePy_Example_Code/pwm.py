from machine import Timer
skip_test = 0
go_test = 1
test_list=[[skip_test,skip_test,skip_test],
[go_test,go_test,go_test],
[go_test,go_test,go_test],
[go_test,go_test,go_test],
[skip_test,skip_test,skip_test],
[skip_test,skip_test,skip_test],
[go_test,go_test,go_test],
[go_test,go_test,go_test]]
total_timer_num=8
max_channel_num=3
cur_ch=0
timer_id = 1
while timer_id < total_timer_num:
    while cur_ch < max_channel_num:
        if test_list[timer_id][cur_ch] != go_test:
            print('skip timer '+str(timer_id)+' pwm_'+str(cur_ch))
            cur_ch+=1
            continue
        tim = Timer(timer_id, mode=Timer.PWM)	#创建Timer为PWM信号输出
        print(tim)
        pwm = tim.channel(cur_ch, freq=1, duty_cycle=5055) #PWM输出频率1Hz, 占空比50.55%.
        cur_ch+=1
        print(pwm)
        tim.deinit()
    cur_ch=0
    timer_id+=1
