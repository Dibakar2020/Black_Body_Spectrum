import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h,c,k 

# Constants
T_cmb=2.725   # Temperature of the CMB in Kelvin

# Function to calculate the black body spectrum
def black_body_spectrum(frequency, temperature):
    # Planck's law
    return (2 * h *c* frequency**3 ) * (1 / (np.exp((h *c* frequency*100) / (k * temperature)) - 1))*10**26

# Load data from NASA
data=np.loadtxt('cmb_data.txt')

# Extract frequency and CMB flux
frequency = data[:,0]      #this is actually 1/wavelength
cmb_flux=data[:,1]
frequency1 = 100*c*data[:,0]    # here i convert 1/wavelength to frequency
# Calculate black body spectrum
bb_spectrum = black_body_spectrum(frequency, T_cmb)


# Plot the black body spectrum
plt.plot(frequency1, bb_spectrum, label='Black Body Spectrum (T=2.725 K)',linestyle="--",linewidth=2)

# Superimpose the CMB flux
plt.plot(frequency1, cmb_flux, label='CMB Flux',linestyle="dotted",linewidth=3)

# Find the wavelength at which the black body spectrum peaks
peak_wavelength_index=np.argmax(bb_spectrum)
peak_wavelength=c/frequency1[peak_wavelength_index] 
print(f"The wavelength at which the black body spectrum peaks is approximately {peak_wavelength:.2e} meters.")

# Add labels and legend
plt.xlabel('Frequency (Hz)')
plt.ylabel('Spectral Radiance (MJy/sr)')
plt.legend()

# Save the plot to a PDF file
plt.savefig('cmb_spectrum_plot.pdf')

# Show the plot
plt.show()
