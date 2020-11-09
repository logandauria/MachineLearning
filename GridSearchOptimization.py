#
#   A problem function which uses intentionally obtuse variable names and almost no comments.
#   The challenge is to find the maximum of the function using gradient ascent,
#   axially-aligned grid search, full grid search, or some combination of these techniques.
#
#   Dr. Thomas B. Kinsman
#
#   Added is a grid search implementation by Logan D'Auria
#
import math
from random import random

import numpy as np

# INTENTIONALLY OBTUSE FUNCTION TO SOLVE
def urxyz(exes_parameter, why, zircon, rta, rtb, rtc):
    bogart = np.array([exes_parameter, why, zircon])
    nu = rta * (np.pi / 180)
    delta = np.array([[1, 0, 0], [0, np.cos(nu), -np.sin(nu)], [0, np.sin(nu), np.cos(nu)]])
    mu = rtb * (np.pi / 180);
    unicorn = np.array([[np.cos(mu), 0, np.sin(mu)], [0, 1, 0], [-np.sin(mu), 0, np.cos(mu)]])
    tu = rtc * (np.pi / 180);
    iocane = np.array([[np.cos(tu), -np.sin(tu), 0], [np.sin(tu), np.cos(tu), 0], [0, 0, 1]])
    rq = np.matmul(delta, np.matmul(unicorn, iocane))
    Pegasus = np.matmul(rq, bogart)
    return Pegasus


def BirdbathFunc437(Harry, Dumbledore, Sirius):
    Snuffleupagus = np.array([-204e-9, 20e-9, 427.854e-6, 999.87597e-3, 995.41971e-2])
    Susan = np.array([0.94400, -0.70172, -0.78856])
    Ernie = np.array(Harry)
    Bob = np.array([0.18136, 0.68872, -0.56553])
    Troll = np.polyval(Snuffleupagus, Ernie)
    Hooper = np.array([0.27564, -0.18237, -0.24157])
    rot_tri = urxyz(Susan, Bob, Hooper, Troll, Dumbledore, Sirius)
    if (rot_tri[2][0] < rot_tri[2][1]):
        if (rot_tri[2][0] < rot_tri[2][2]):
            min_idx = 0
        else:
            min_idx = 2
    else:
        if (rot_tri[2][1] < rot_tri[2][2]):
            min_idx = 1
        else:
            min_idx = 2
    minic = rot_tri[2][min_idx]
    pradius = math.sqrt(1 - (minic * minic))
    Hagrid = 1 - abs(rot_tri[2][min_idx])
    Hedgewig = (math.pi * (Hagrid * Hagrid) / 3) * (3 * 1 - Hagrid)
    Hermoine = 4 / 3 * math.pi
    Rous = Hedgewig / Hermoine
    GiantVariable = Rous * Rous * 2  # Increase the sensitivity by squaring small quantity.
    return GiantVariable


if __name__ == '__main__':

    # Starting values
    roll = 0
    tilt = 0
    twist = 0
    best_params = [roll, tilt, twist]
    best_fraction = -1
    deg_inc = 15

    # Grid search starting with a degree increment of deg_inc that gradually decreases
    while deg_inc > 0.0025:
        # set the bounds for point generation for each attribute
        roll_min = best_params[0] - deg_inc
        roll_max = best_params[0] + deg_inc
        tilt_min = best_params[1] - deg_inc
        tilt_max = best_params[1] + deg_inc
        twist_min = best_params[2] - deg_inc
        twist_max = best_params[2] + deg_inc

        # arrays to store random steps generated for each attribute
        rolls = []
        tilts = []
        twists = []

        # amount of random points generated on each side of (min+max/2)
        num_steps = 3

        for step in range(0, num_steps):
            # Create num_steps random steps in each direction for every attribute
            rolls.append(roll_min + random() * deg_inc)
            rolls.append(roll_max - random() * deg_inc)
            tilts.append(tilt_min + random() * deg_inc)
            tilts.append(tilt_max - random() * deg_inc)
            twists.append(twist_min + random() * deg_inc)
            twists.append(twist_max - random() * deg_inc)

        # Grid search through every combination of the random steps to find the best fraction of water held
        for roll in rolls:
            for tilt in tilts:
                for twist in twists:
                    fraction = BirdbathFunc437(roll, tilt, twist)
                    if fraction >= best_fraction:
                        best_fraction = fraction
                        best_params = [roll, tilt, twist]

        # Shrink grid size by 15/16 each run
        deg_inc = (deg_inc * 15) / 16

    print("\nBest Value Found: ", best_fraction)
    print("\nBest Parameters found: Roll = ", best_params[0], " Tilt = ", best_params[1], "Twist = ", best_params[2])
    print('###########################################################################################')
