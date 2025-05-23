Fs = 1000;
s = 2;
t = linspace(0,s, s*Fs);
f = 5;
omega = 2*pi*f;
x = cos(omega*t);

X = fft(x);
figure
fr = linspace(0, Fs/2, s*Fs/2);
plot(fr, abs(X));
