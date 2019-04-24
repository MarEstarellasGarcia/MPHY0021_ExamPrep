from matplotlib import pyplot as plt
from tree import the_tree
from tree_np import the_three_np
import time

branch_size =1
angle= 0.1
decrease_size= 0.6
tiempo= []
tiempo2=[]
iterations= range(1,25,1)

for number_of_forks in iterations:
    t = time.time()
    the_tree(number_of_forks, branch_size, angle, decrease_size, True)
    elapsed = time.time() - t
    tiempo.append([elapsed])
    print(number_of_forks)
    
    t2 = time.time()
    the_tree_np(number_of_forks, branch_size, angle, decrease_size, True)
    elapsed2 = time.time() - t2
    tiempo2.append([elapsed2])
    

plt.figure()
plt.plot(iterations, tiempo)
plt.plot(iterations, tiempo2)
plt.xlabel('Number of forks')
plt.ylabel('Time')
plt.savefig('perf_plot.png')   
