from numpy import *
import matplotlib.pyplot as plt
from argparse import ArgumentParser


def draw_julia(dimy, dimx):
    A = zeros([dimy,dimx])
    for x in range(dimx):
        for y in range(dimy):
            zx=1.5*(x-dimx/2)/(0.5*1*dimx)
            zy=1.0*(y-dimy/2)/(0.5*1*dimy)
            i=255
            t=True
            while t==True:
                if zx*zx+zy*zy>=4:
                    t=False
                if i<=1:
                    t=False
                a=zx*zx-zy*zy-0.7
                zy=2.0*zx*zy+0.27015
                zx=a
                i=i-1
            A[y][x]=i
    plt.imshow(A)
    plt.show()
    plt.savefig('julia.png')


if __name__ == "__main__":

    parser = ArgumentParser(description="fuckingJulia")
    
    parser.add_argument('Dimx', 
                        help= "max dim x")
    parser.add_argument('Dimy', 
                        help= "max dim y")
#    parser.add_argument('angle', 
#                        help= "Angle of separation between branches")
#    parser.add_argument('decrease_size', 
#                        help= "Decrease the size of the branches in following forks")
#    parser.add_argument('--no_plot', '-p', action="store_true", 
#                        help= "Add this argument if you do not want a plot of the tree" )


    arguments = parser.parse_args()
    
    Dimx = int(arguments.Dimx)
    Dimy = int(arguments.Dimy)
#    branch_size = float(arguments.branch_size)
#    angle = float(arguments.angle)
#    decrease_size = float(arguments.decrease_size)
    
    draw_julia(Dimy, Dimx)