import skrf as rf
import numpy as np
import matplotlib.pyplot as plt

def getR(S12, f, G):

    wavelength = 3e8/f
    r = np.sqrt((wavelength**2*G**2)/(4*np.pi**2*S12))

    return r

def getG(S12, f, r):

    wavelength = 3e8 / f

    G = np.sqrt((S12*4*np.pi**2*r**2)/(wavelength**2))

    return G

if __name__ == '__main__':

    one_nineteen_meter = rf.Network('Data2/direction0.s2p')
    half_meter = rf.Network('Data2/direction0-0.5m.s2p')
    one_meter = rf.Network('Data2/direction0-1m.s2p')

    f = one_nineteen_meter.frequency.f[int(len(one_nineteen_meter.s12.s)/2)]
    Svalid = one_nineteen_meter.s12.s.squeeze()[int(len(one_nineteen_meter.s12.s)/2)]
    Sone = abs(one_meter.s12.s.squeeze()[int(len(one_nineteen_meter.s12.s)/2)])
    Shalf = abs(half_meter.s12.s.squeeze()[int(len(one_nineteen_meter.s12.s)/2)])
    print(len(one_nineteen_meter.s12.s)/2)

    print(f)

    print(abs(Svalid))

    G = getG(abs(Svalid), f, 1.19)


    print(G)
    R2 = getR(Shalf, f, G)
    R3 = getR(Sone, f, G)
    print(f"Estimated range for 50cm:\n{round(R2,3)} m \nfor 1m: \n{round(R3,3)} m")