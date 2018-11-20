import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sched, time

s = sched.scheduler(time.time, time.sleep)

def do_something(sc,I): 
    print(I)
    I+=1
    s.enter(1, 1, do_something, (sc,I))

i=0

s.enter(1, 1, do_something, (s,i))
s.run()
