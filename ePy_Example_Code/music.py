from machine import Music
note=['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
note_str = note[0]
note_num = 0
octave = 0
b=Music()			#创建Music来播放Tone音乐
while octave <9:
    while note_num < 12:
        note_str = note[note_num] + str(octave)+':2'
        print(note_str)
        b.play(str(note_str),loop=0,wait=1)	#从蜂鸣器播放音乐
        note_num=note_num+1
    octave = octave+1
    note_num = 0

notes = ["C4:4", "D", "E", "C", "C", "D", "E", "C", "E", "F", "G:8", "E:4", "F", "G:8"]
b.play(notes,loop=0,wait=1)
b.deinit()