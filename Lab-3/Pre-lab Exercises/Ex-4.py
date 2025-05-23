import skrf as rf
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.fft import fft, fftshift
import matplotlib.pyplot as plt


N = 4
samples = np.linspace(0,3,4)

coeff  = signal.windows.chebwin(N, 20)
print(coeff)


plt.plot(samples, coeff)

plt.show()

theta = np.linspace(-np.pi,np.pi,5)

