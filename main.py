import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sched, time

s = sched.scheduler(time.time, time.sleep)

def do_something(sc,I): 
    print(I)
    I+=1
    s.enter(1, 1, do_something, (sc,I))


x = np.zeros(100)
y = np.zeros(100)
i=0
print(i)
fig, ax = plt.subplots()
# red = np.linspace(0,2,100)
# ax.plot(red,red)
# plt.show()

# I'd like to pass red and ax into do_something and
# change red to np.linspace(0,2,100) then plot it 
# on ax
s.enter(1, 1, do_something, (s,i))
s.run()
