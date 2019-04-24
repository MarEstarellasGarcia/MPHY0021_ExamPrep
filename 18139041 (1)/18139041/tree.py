# %matplotlib inline
from math import sin, cos
from matplotlib import pyplot as plt
from argparse import ArgumentParser


def grow_tree(new_branch, current_branch, branch_size, angle):
    new_branch.append([current_branch[0]+branch_size*sin(current_branch[2]+angle),
                       current_branch[1]+branch_size*cos(current_branch[2]+angle),
                       current_branch[2]+angle])
    return new_branch


def plot_tree(current_branch, new_branch, direction):
    plt.plot([current_branch[0], new_branch[direction][0]],
             [current_branch[1], new_branch[direction][1]])
    

def the_tree(number_of_forks, branch_size, angle, decrease_size, no_plot):
    plt.plot([0,0],[0,1])
    current_branch=[[0,1,0]]
    right= -2
    left= -1
    
    for i in range(number_of_forks):
        new_branch=[]
        for j in range(len(current_branch)):
            grow_tree(new_branch, current_branch[j], branch_size, -angle)
            grow_tree(new_branch, current_branch[j], branch_size, angle)
            
            if no_plot == False:
                plot_tree(current_branch[j], new_branch, right)
                plot_tree(current_branch[j], new_branch, left)

        current_branch=new_branch
        branch_size*= decrease_size

    if no_plot == False:
        plt.savefig('tree.png')
        

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
    
    the_tree(number_of_forks, branch_size, angle, decrease_size, arguments.no_plot)