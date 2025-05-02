import skrf as rf
import numpy as np
import matplotlib.pyplot as plt


def getArray(Directory):
    network = rf.Network(f"{Directory}/direction0.s2p")
    array = np.array(network.frequency.f.squeeze())
    print(array)

    for i in range(-20,20):
        j = 2*i
        network = rf.Network(f"{Directory}/direction{j}.s2p")
        S12 = abs(network.s12.s.squeeze())

        print(array.shape)
        # np.append(array, S12)

    return array

if __name__ == '__main__':

    array = getArray("Data")
    # print(array.shape)
    # angles = np.linspace(-40,40,41)
    # print(array)
    # plt.figure(figsize=(8, 5))
    # plt.rcParams['font.size'] = '16'
    # plt.plot(angles , 20*np.log10(array[0,1:]))
    # plt.xlabel('Angle (deg)', fontsize=15)
    # plt.ylabel('Normalized power', fontsize=15)
    # plt.tick_params(axis='both', labelsize=15)
    # plt.grid(True)
    #
    # # plt.xticks(np.linspace(0, 10, 11))
    # # plt.yticks(np.linspace(-180, 180, 10))
    # # plt.xlim(thru.frequency.f.min()/1e9, thru.frequency.f.max()/1e9)
    # # plt.savefig("radiatedpowerPlot.svg")
    # plt.show()