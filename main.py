import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sched, time

s = sched.scheduler(time.time, time.sleep)


phase = 0.0
x = np.linspace(0, 6*np.pi, 100)

# You probably won't need this if you're embedding things in a tkinter plot...
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, np.sin(x), 'r-') # Returns a tuple of line objects, thus the comma

line1.set_ydata(np.sin(x))
fig.canvas.draw()
fig.canvas.flush_events()

def do_something(sc,X,Phase,Line,Fig):
    Phase = Phase + 0.3
    X = np.linspace(0+Phase,6*np.pi+Phase,100)

    Line.set_xdata(X)
    Line.set_ydata(np.sin(X))
    Fig.canvas.draw()
    Fig.canvas.flush_events()

    if Phase < 6*np.pi:
           s.enter(0.005, 1, do_something, (sc,X,Phase,Line,Fig))

s.enter(1, 1, do_something, (s,x,phase,line1,fig))
s.run()
