from matplotlib import pyplot as plt
from argparse import ArgumentParser
import numpy as np

def grow_tree_np(x, y, branch_size, angle, angle_array):
    right_angle= angle_array + angle 
    left_angle= angle_array - angle
    angle_array = np.hstack((right_angle,left_angle))
    xx= np.hstack((x,x))
    yy = np.hstack((y,y))
    x = xx + branch_size*np.sin(angle_array)
    y = yy + branch_size*np.cos(angle_array)
    return [x, y, xx, yy, angle_array]



def the_tree_np(number_of_forks, branch_size, angle, decrease_size, no_plot): 
    angle_array = np.array(0)        
    x = np.array(0)
    y = np.array(1)
    plt.plot([0,0],[0,1])
    for i in range(number_of_forks):
        [x, y, xx, yy, angle_array] = grow_tree_np(x, y, branch_size, angle, angle_array)
        branch_size*= decrease_size
        if no_plot == False:
            plt.plot([xx, x], [yy, y])
    if no_plot == False:       
        plt.savefig('tree_np.png')


if __name__ == "__main__":

    parser = ArgumentParser(description="Growing colorful trees")
    
    parser.add_argument('number_of_forks', 
                        help= "Number of forks in total that you want your tree to grow")
    parser.add_argument('branch_size', 
                        help= "Initial branch size")
    parser.add_argument('angle', 
                        help= "Angle of separation between branches")
    parser.add_argument('decrease_size', 
                        help= "Decrease the size of the branches in following forks")
    parser.add_argument('--no_plot', '-p', action="store_true", 
                        help= "Add this argument if you do not want a plot of the tree" )

    arguments = parser.parse_args()
    
    number_of_forks = int(arguments.number_of_forks)
    branch_size = float(arguments.branch_size)
    angle = float(arguments.angle)
    decrease_size = float(arguments.decrease_size)
    
    the_tree_np(number_of_forks, branch_size, angle, decrease_size, arguments.no_plot)