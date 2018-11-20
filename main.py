import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sched, time

s = sched.scheduler(time.time, time.sleep)

def do_something(sc): 
    print("Doing stuff...")
    # do your stuff
    s.enter(1, 1, do_something, (sc,))


red = np.linspace(0,2,100)
fig, ax = plt.subplots()

#I'd like to pass red and ax into do_something
s.enter(60, 1, do_something, (s,))
s.run()
