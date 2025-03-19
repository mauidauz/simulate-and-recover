import numpy as np

def inverse_EZ(Robs, Mobs, Vobs):
    if abs(Robs - 0.5) < 1e-6:
        raise ValueError(f"Robs is too close to 0.5: {Robs}. This leads to log(0) issues.")

    # Clip Robs to valid range
    Robs = np.clip(Robs, 1e-6, 0.499999)
    
    value = 1 - 2 * Robs
    print(f"Value inside log computation: {value}")  # Debugging

    y = np.log(abs(1 / value)) 
    print(f"Calculated y = {y}")

    discriminant = (Mobs * y) ** 2 - 4 * Vobs * y
    if discriminant < 0:
        raise ValueError("Negative discriminant: invalid parameters leading to complex sqrt.")
    
    alpha_est = (Mobs * y + np.sqrt(discriminant)) / 2
    nu_est = y / alpha_est
    tau_est = Mobs - (alpha_est / (2 * nu_est)) * ((1 - y) / (1 + y))

    return nu_est, alpha_est, tau_est