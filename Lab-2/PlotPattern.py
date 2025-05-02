import skrf as rf
import numpy as np
import matplotlib.pyplot as plt


def getArray(Directory):

    for i in range(40):
        j = 2*i
        network = rf.Network(f"{Directory}/direction-{j}.s2p")
        frequency = network.frequency.f.()
        S12 = network.s12.s.squeeze()



    return array

if __name__ == '__main__':

    array = getArray("Data")