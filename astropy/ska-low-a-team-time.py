import numpy as np
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
import astropy.units as u

# 1) Site
location = EarthLocation(lat=-26.703319*u.deg,
                         lon=116.670815*u.deg,
                         height=377.8*u.m)

# 2) Coordinates as before (decimal degrees → Quantity)
ra_deg  = np.array([350.86667, 201.36667, 299.86667,
                    50.67375, 252.78333, 139.52500,
                    79.95833,  83.63333, 187.70417])
dec_deg = np.array([ 58.81167, -43.01917,  40.73389,
                    -37.20830,   4.99250, -12.09556,
                    -45.77889,  22.01444,  12.39111])
coords = SkyCoord(ra=ra_deg*u.deg,
                  dec=dec_deg*u.deg,
                  frame='icrs')

# 3) Build the time array
t0 = Time("2025-01-01T00:00:00", scale='utc')
t1 = Time("2026-01-01T00:00:00", scale='utc')
n_hours = int((t1 - t0).to(u.hour).value)
times   = t0 + np.arange(n_hours)*u.hour

# 4) Compute altitudes *per source* into a (9 × n_hours) array
altitudes = np.zeros((len(coords), n_hours))
aa_frame = AltAz(obstime=times, location=location)

for i, src in enumerate(coords):
    aa = src.transform_to(aa_frame)
    altitudes[i, :] = aa.alt.deg

# 5) Visibility fraction
visible_any = np.any(altitudes > 0, axis=0)
fraction = visible_any.sum() / visible_any.size

print(f"Fraction of the year with ≥1 source up: {fraction:.4f} ({fraction*100:.1f}%)")

