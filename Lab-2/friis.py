import skrf as rf
import numpy as np
import matplotlib.pyplot as plt

def getR(S12, f, G):    #Calculates the distance between the horns based on Friis equation
    S12 = abs(S12)  #Absolute value is relevant for power transfer

    wavelength = 2.997e8/f
    r = (wavelength*G)/(4*np.pi*S12)

    return r

def getG(S12, f, r):
    S12 = abs(S12)  # Absolute value is relevant for power transfer

    wavelength = 3e8 / f

    G = (4*S12*np.pi*r)/(wavelength)

    return G

if __name__ == '__main__':

    net129cm = rf.Network('direction0-1.29v2.s2p')
    net50cm = rf.Network('direction0-0.5mv2.s2p')
    net100cm = rf.Network('direction0-1mv2.s2p')

    f = net129cm.frequency.f[int(len(net129cm.s12.s) / 2)]
    tot_f = net129cm.frequency.f
    tot_S12_129cm = net129cm.s12.s.squeeze()
    S12_129cm = net129cm.s12.s.squeeze()[int(len(net129cm.s12.s) / 2)]
    S12_100cm = net100cm.s12.s.squeeze()[int(len(net129cm.s12.s) / 2)]
    S12_50cm = net50cm.s12.s.squeeze()[int(len(net129cm.s12.s) / 2)]

    Gtot = getG(tot_S12_129cm, tot_f, 1.29)
    print(Gtot.shape)
    G = getG(S12_129cm, f, 1.29)
    R2 = getR(S12_50cm, f, G)
    R3 = getR(S12_100cm, f, G)

    #print(f"Estimated range for 50cm:\n{round(R2,3)} m \nfor 1m: \n{round(R3,3)} m")
    #
    plt.figure(figsize=(8, 5))
    plt.rcParams['font.size'] = '16'
    plt.plot(tot_f/ 1e9 , 10*np.log10(Gtot))
    plt.xlabel('Frequency (GHz)', fontsize=15)
    plt.ylabel('Gain (dB)', fontsize=15)
    plt.tick_params(axis='both', labelsize=15)
    plt.grid(True)

    # plt.xticks(np.linspace(0, 10, 11))
    # plt.yticks(np.linspace(-180, 180, 10))
    # plt.xlim(thru.frequency.f.min()/1e9, thru.frequency.f.max()/1e9)
    # plt.savefig("radiatedpowerPlot.svg")
    plt.show()