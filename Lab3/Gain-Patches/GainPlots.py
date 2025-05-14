import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
from PlotStandard.PlotStandard import Plot


def findG(Ghorn, S12, f, r):


    wavelength = 3e8 / f

    G = ((4*np.pi*r)**2)/((wavelength**2)*Ghorn) * (abs(S12)**2)

    G_dB = 10*np.log10(abs(G))

    return G_dB

def getGHorn():

    S = rf.Network('DataHorn/direction0-1.29v2.s2p')
    f = S.frequency.f.squeeze()
    S12 = S.s12.s.squeeze()
    wavelength = 3e8 / f
    r = 1.29

    Ghorn = (abs(S12)*4*np.pi*r)/(wavelength)

    return f, Ghorn

if __name__ == '__main__':
    X = "Frequency (GHz)"
    Y = "Gain (dB)"
    r = 1.17

    f_horn, G_horn = getGHorn()
    #G horn had twice the number of samples. (401)
    G_horn = G_horn[::2]

    #plot the horn gain
    #Plot(f_horn,10*np.log10(G_horn),"","","Horn antenna gain")

    #Get the frequency for the patch antenna measurements.
    f = rf.Network('DataPatchArrays/Patch1.s2p').frequency.f.squeeze()


    #Get the linear S parameter measurements
    S12_Patch1 = rf.Network('DataPatchArrays/Patch1.s2p').s12.s.squeeze()

    #Get the gain of the patch
    G_Patch1 = findG(G_horn, S12_Patch1, f, r)

    #Plot the G of the patch
    Plot(f / 1e9, G_Patch1, X, Y, "Gain of a 1-element Array", Filename="Patch1", SaveFile=True)




    # S12_Patch2 = rf.Network('Data/Patch2.s2p').s12.s.squeeze()
    # Plot(f / 1e9, findG(Ghorn,S12_Patch2, f, r), X, Y, "Gain of a 2-element Array", Filename="Patch2", SaveFile=True)

    # S12_Patch4 = rf.Network('Data/Patch4.s2p').s12.s.squeeze()
    # Plot(f / 1e9, findG(Ghorn,S12_Patch4, f, r), X, Y, "Gain of a 4-element Array", Filename="Patch4", SaveFile=True)

    # S12_Patch8_A = rf.Network('Data/Patch8_A.s2p').s12.s.squeeze()
    # Plot(f / 1e9, findG(Ghorn,S12_Patch8_A , f, r), X, Y, "Gain of 8-element Array A", Filename="Patch8_A", SaveFile=True)

    # S12_Patch8_B = rf.Network('Data/Patch8_B.s2p').s12.s.squeeze()
    # Plot(f / 1e9, findG(Ghorn,S12_Patch8_B, f, r), X, Y, "Gain of 8-element Array B", Filename="Patch8_B", SaveFile=True)

    # S12_Patch8_C = rf.Network('Data/Patch8_C.s2p').s12.s.squeeze()
    # Plot(f / 1e9, findG(Ghorn,S12_Patch8_C, f, r), X, Y, "Gain of 8-element Array C", Filename="Patch8_C", SaveFile=True)

    # S12_Patch8_D = rf.Network('Data/Patch8_D.s2p').s12.s.squeeze()
    # Plot(f / 1e9, findG(Ghorn,S12_Patch8_D, f, r), X, Y, "Gain of 8-element Array D", Filename="Patch8_D", SaveFile=True)
    # Plot(f / 1e9, S12_Patch8_D, "Frequency (GHz)", "S12 dB", "S12 patch8D parameter versus frequency")
    # Plot(f / 1e9, S12_Patch2  , "Frequency (GHz)", "S12 dB", "S12 patch2 parameter versus frequency")
    # Plot(f/1e9, 20*np.log10(abs(S12_Patch1)), "Frequency (GHz)", "S12 dB", "S12 parameter versus frequency")
