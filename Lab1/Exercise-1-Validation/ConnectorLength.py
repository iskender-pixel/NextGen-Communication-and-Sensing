import skrf as rf
import numpy as np
import matplotlib.pyplot as plt

thru = rf.Network('Data/CalibrationThru1.s2p')

S = thru.frequency.f

plt.figure(figsize=(8,5))
plt.plot(thru.frequency.f.squeeze()/1e9, np.angle(thru.s12.s.squeeze(), deg=True))
# plt.title('Phase of S12 vs Frequency')
plt.xlabel('Frequency (GHz)')
plt.ylabel('Phase (S1,2) (Degrees)')
plt.grid(True)
plt.xticks(np.linspace(0,10,11))
plt.yticks(np.linspace(-180,180,10))
# plt.xlim(thru.frequency.f.min()/1e9, thru.frequency.f.max()/1e9)
plt.savefig("PhaseThru.svg")
plt.show()