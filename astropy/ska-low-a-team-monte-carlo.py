import numpy as np

# --- A Team coordinates in decimal degrees ---
ra_deg = np.array([
    350.86667, 201.36667, 299.86667,
     50.67375, 252.78333, 139.52500,
     79.95833,  83.63333, 187.70417
])
dec_deg = np.array([
     58.81167, -43.01917,  40.73389,
    -37.20830,   4.99250, -12.09556,
    -45.77889,  22.01444,  12.39111
])

# --- Convert to radians ---
ra_rad  = np.deg2rad(ra_deg)
dec_rad = np.deg2rad(dec_deg)
radius  = np.deg2rad(10.0)  # 10° cap radius

# --- Monte Carlo sampling on the sphere ---
n_samples = 200_000
u   = np.random.uniform(-1, 1, n_samples)
phi = np.random.uniform(0, 2*np.pi, n_samples)
dec_samp = np.arcsin(u)
ra_samp  = phi

# Cartesian coords of random sky points
x_s = np.cos(dec_samp) * np.cos(ra_samp)
y_s = np.cos(dec_samp) * np.sin(ra_samp)
z_s = np.sin(dec_samp)
samples = np.vstack([x_s, y_s, z_s]).T  # shape (n_samples, 3)

# Cartesian coords of source caps
x_src = np.cos(dec_rad) * np.cos(ra_rad)
y_src = np.cos(dec_rad) * np.sin(ra_rad)
z_src = np.sin(dec_rad)
sources = np.vstack([x_src, y_src, z_src]).T  # shape (9, 3)

# Compute dot products and test within 10° of any source
cos_radius = np.cos(radius)
dots = sources @ samples.T  # shape (9, n_samples)
within_any = np.any(dots >= cos_radius, axis=0)

fraction = within_any.mean()
print(f"Sky fraction within 10° of any source: {fraction:.4f} ({fraction*100:.2f}%)")

