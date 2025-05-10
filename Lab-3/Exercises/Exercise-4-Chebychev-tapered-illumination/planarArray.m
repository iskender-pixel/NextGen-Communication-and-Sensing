% Parameters
    N = 8;                    
    f = 15e9;                 
    c = 3e8;                  
    lambda = c / f;           
    dx = lambda / 2;          
    dy = lambda / 2;       
    k0 = 2*pi / lambda;       
    theta0 = 0;
    phi0 = 0;
    
    %Coordinatos
    theta = linspace(0, pi, 361);
    phi = linspace(eps, 2*pi, 361);
    
    [TH,PH] = meshgrid(theta,phi);
    
    %Chebychev window
    coeff = chebwin(N,40);
    coeffGrid = coeff * coeff.';
    stem3(coeffGrid);
    
    %Wavenumbers
    kx_0 = k0*sin(theta0).*cos(phi0);
    ky_0 = k0*sin(theta0).*sin(phi0);
    kx = k0*sin(TH).*cos(PH);
    ky = k0*sin(TH).*sin(PH);
    
    AF_uniform = zeros(size(TH));
    AF = zeros(size(TH));
    
    for m = 0:N-1
        for n = 0:N-1
            AF_uniform = AF_uniform + exp(1j * (m*dx*(kx-kx_0) + n*dy*(ky - ky_0)));
        end
    end
    
    for m = 0:N-1
        for n = 0:N-1
            AF = AF + coeffGrid(m+1,n+1) *exp(1j * (m*dx*(kx-kx_0) + n*dy*(ky - ky_0)));
        end
    end
    
    
    AF_uniform_mag_dB = 20*log10(abs(AF_uniform));
    AF_uniform_mag_dB = AF_uniform_mag_dB - max(AF_uniform_mag_dB(:));
    
    TH_deg = rad2deg(TH); 
    PH_deg = rad2deg(PH);
    %patternCustom(AF_uniform_mag_dB(:),TH_deg(:),PH_deg(:))
    
    
    AF_mag_dB = 20*log10(abs(AF));
    AF_mag_dB = AF_mag_dB - max(AF_mag_dB(:)); 
    %patternCustom(AF_mag_dB(:),TH_deg(:),PH_deg(:))
    
    
    patternCustom(AF_mag_dB(:),TH_deg(:),PH_deg(:),CoordinateSystem="rectangular", Slice="phi", SliceValue=rad2deg(phi(90)));
    hold on
    patternCustom(AF_uniform_mag_dB(:),TH_deg(:),PH_deg(:),CoordinateSystem="rectangular", Slice="phi", SliceValue=rad2deg(phi(90)));
    hold off
    
    %Directivity
    U = abs(AF).^2;
    Umax = max(U(:)); 
    Prad = trapz(phi, trapz(theta, U.*sin(TH), 2));
    D = 4*pi*Umax/Prad;
    D_dB = 10*log10(abs(D));
    fprintf('Directivity weighted (dB): %.3f dB\n', D_dB);
    
    %uniform
    U_uniform = abs(AF_uniform).^2;
    Umax_uniform = max(U_uniform(:));
    Prad_uniform = trapz(phi, trapz(theta, U_uniform.*sin(TH), 2));
    D_uniform = 4*pi*Umax_uniform/Prad_uniform;
    D_uniform_dB = 10*log10(abs(D_uniform));
    fprintf('Directivity uniform (dB): %.3f dB\n', D_uniform_dB);