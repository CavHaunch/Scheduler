import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sched, time

s = sched.scheduler(time.time, time.sleep)

def do_something(sc,X,Y,I,axes): 
    X = np.linspace(0,2,100)
    Y = np.linspace(0,2,100)+I
    I = I+1.0
    axes.plot(X,np.sin(Y))
    plt.show()
    s.enter(1, 1, do_something, (sc,X,Y,I,axes))


x = np.zeros(100)
y = np.zeros(100)
i=0.0
fig, ax = plt.subplots()

s.enter(1, 1, do_something, (s,x,y,i,ax))
s.run()
