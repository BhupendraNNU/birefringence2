import numpy as np

n_o = 1.484
n_e = 1.575

def calculate_pretilt_angle(delta_n_values):
    angles = []
    for delta_n in delta_n_values:
        n_eff = n_o + delta_n
        if not (n_o < n_eff < n_e):
            print(f"Warning: n_eff ({n_eff}) out of valid range. Check Δn value.")
            angles.append(np.nan)
            continue

        numerator = (n_e * n_o / n_eff)**2 - n_o**2
        denominator = n_e**2 - n_o**2
        value = numerator / denominator

        if value < 0 or value > 1:
            print(f"Warning: Arcsin domain error ({value}). Check input values.")
            angles.append(np.nan)
            continue

        theta_rad = np.arcsin(np.sqrt(value))
        angles.append(np.degrees(theta_rad))

    return angles
