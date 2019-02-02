from psonic import *
from threading import Thread

play(60)

#use_bpm(120)
pause = 1
n = 1
#while n < 10:
#    play(60)
#    sleep(pause)
#    play(62)
#    play(65)
#    play(73)
#    n += 1

def loop():
    play(65)
    sleep(1)
    play(70)

def looper():
    while True:
        loop()

looper_thread = Thread(name='looper', target=looper)

looper_thread.start()
input("Press Enter to continue...")

