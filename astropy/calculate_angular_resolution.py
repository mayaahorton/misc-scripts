import numpy as np

def calculate_angular_resolution(frequency_mhz, baseline_m, k=1.22):
    """
    Calculate synthesized FWHM for a given frequency and baseline.

    Parameters:
    - frequency_mhz: frequency in MHz
    - baseline_m: baseline in meters
    - k: aperture constant (default 1.22 for circular aperture)

    Returns:
    - fwhm_degrees: FWHM in degrees
    - fwhm_arcsec: FWHM in arcseconds
    - wavelength: wavelength in meters
    """
    c = 3e8  # Speed of light in m/s
    wavelength = c / (frequency_mhz * 1e6)
    fwhm_radians = (k * wavelength) / baseline_m
    fwhm_degrees = np.degrees(fwhm_radians)
    fwhm_arcsec = fwhm_degrees * 3600
    return fwhm_degrees, fwhm_arcsec, wavelength

