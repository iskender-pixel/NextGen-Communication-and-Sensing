import skrf as rf
import numpy as np
import matplotlib.pyplot as plt
from pyasn1_modules.rfc5990 import sha512


def getR(S12, f, G):

    wavelength = 3e8/f
    r = np.sqrt((wavelength**2*G**2)/(4**2*np.pi**2*S12**2))

    return r

def getG(S12, f, r):

    wavelength = 3e8 / f

    G = (S12*4*np.pi*r)/(wavelength)

    return G

if __name__ == '__main__':

    one_nineteen_meter = rf.Network('Data2/direction0-1.29v2.s2p')
    half_meter = rf.Network('Data2/direction0-0.5m.s2p')
    one_meter = rf.Network('Data2/direction0-1m.s2p')
    s12_half = half_meter.s12.s.squeeze()
    s12_meter = 1
    # extra_measurement = rf.Network('Data2/.s2p')

    f = one_nineteen_meter.frequency.f

    print(len(one_nineteen_meter.s12.s)/2)

    print(f)


    G = getG(abs(one_nineteen_meter.s12.s.squeeze()), f, 1.29)
    # print(G)

    figure = plt.figure(figsize=(8, 5))
    plt.plot(f / 1e9, 10*np.log10(G))

    # plt.title('Phase of S12 vs Frequency')
    plt.xlabel('Frequency (GHz)')
    plt.ylabel('Gain (dB)')
    plt.grid(True)
    # plt.xticks(np.linspace(0, 10, 11))
    # plt.yticks(np.linspace(-180, 180, 10))
    # plt.xlim(thru.frequency.f.min()/1e9, thru.frequency.f.max()/1e9)
    # plt.savefig("PhaseThru.svg")
    plt.show()
    #
    # print(G)
    # R2 = getR(Shalf, f, G)
    # R3 = getR(Sone, f, G)
    # print(f"Estimated range for 50cm:\n{round(R2,3)} m \nfor 1m: \n{round(R3,3)} m")