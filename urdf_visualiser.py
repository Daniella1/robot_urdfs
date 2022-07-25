# For visualiztion of urdf file
from urdfpy import URDF


if __name__ == '__main__':

    filename = 'universal-robots/ur5e/ur5e.urdf' # change filename to the urdf you want to visualise

    robot = URDF.load(filename)

    robot.show(use_collision=False)             # static visualisation
    # robot.animate()                           # dynamic visualisation with movement of joints