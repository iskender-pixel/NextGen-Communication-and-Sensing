import skrf as rf
import numpy as np
import matplotlib.pyplot as plt



def getR(S12, f, G):

    wavelength = 3e8/f
    r = np.sqrt((wavelength**2*G**2)/(4**2*np.pi**2*S12**2))

    return r

def getG(S12, f, r):

    wavelength = 3e8 / f

    G = (abs(S12)*4*np.pi*r)/(wavelength)

    return G

def Aeff(f,G):

    wavelength = 3e8 / f
    A = (wavelength**2)*G/(4*np.pi)

    return A
def Ghorn():
    S = rf.Network('Data2/direction0-1.29v2.s2p')
    f = S.frequency.f.squeeze()
    s12 = S.s12.s.squeeze()

    Ghorn = getG(s12, f, 1.29)

    return f, Ghorn


if __name__ == '__main__':

    # S = rf.Network('../Data2/direction0-1.29v2.s2p')
    # # half_meter = rf.Network('Data2/direction0-0.5m.s2p')
    # # one_meter = rf.Network('Data2/direction0-1m.s2p')
    # s12 = S.s12.s.squeeze()
    #
    # # extra_measurement = rf.Network('Data2/.s2p')
    #
    # f = S.frequency.f.squeeze()
    #
    #
    # G = getG(s12, f, 1.29)

    f, Ghorn = Ghorn()
    # print(G)

    figure = plt.figure(figsize=(8, 5))
    plt.plot(f / 1e9, 10*np.log10(Ghorn))

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