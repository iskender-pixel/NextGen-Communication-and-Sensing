Fs = 200e6;


plot(freqaxis, abs(Sig1))
title('FFT A')
%Sig1 is the frequency domain signal of A

nexttile
plot(t, real(Sig2))
title('Time A')
%Time domain of a chirp A

nexttile
plot(freqaxis, abs(Sig3))
title('FFT B')
%Freq domain B

plot(abs(Sig4))
title('FFT C')
%freq domain C

nexttile
plot(t, real(Sig5))
title('Time B')
%time domain B

nexttile
plot(t, Sig6)
title('Time C')
%time domain C




