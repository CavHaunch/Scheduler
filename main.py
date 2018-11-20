import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sched, time

s = sched.scheduler(time.time, time.sleep)

def do_something(sc): 
    print("Doing stuff...")
    # do your stuff
    s.enter(1, 1, do_something, (sc,))


#Output Image Path
Image_Filename = "numpy/Sines/test.png"

#Plot parameters 
T_Min = 0
T_Max = 4*3.141159*2.0/3.0
Fs = 10

#Signal Lengths
Input_Length = int((T_Max-T_Min)*Fs)

#Initialize data structures
Index_Vector = np.zeros(Input_Length)
r = np.zeros(Input_Length)
g = np.zeros(Input_Length)
b = np.zeros(Input_Length)
P = np.zeros(Input_Length)

# Data for plotting
t = np.linspace( T_Min, T_Max, Input_Length )

r = 0.5 + (0.5 * np.sin(t) )
g =  0.5 + (0.5 *np.sin(t+(2*3.141/3)))
b =  0.5 + (0.5 *np.sin(t-(2*3.141/3)))
P = r**2 + g**2 + b**2

fig, ax = plt.subplots()
ax.plot(t,r)
ax.plot(t,g)
ax.plot(t,b)
ax.plot(t,P)
ax.plot()


ax.set(xlabel='time (t)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid(True)

# fig.tight_layout()
# fig.savefig(Image_Filename)
s.enter(60, 1, do_something, (s,))
s.run()
plt.show()