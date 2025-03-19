import numpy as np

def forward_EZ(a, v, t):
    """
    Compute predicted summary statistics given model parameters.
    
    Parameters:
    a (float): Boundary separation (0.5 to 2)
    v (float): Drift rate (0.5 to 2)
    t (float): Nondecision time (0.1 to 0.5)
    
    Returns:
    tuple: (Rpred, Mpred, Vpred)
    """
    y = np.exp(-a * v)
    print(f"a: {a}, v: {v}, a*v: {a*v}, y: {y}")

    Rpred = 1 / (1 + y)
    Mpred = t + (a / (2 * v)) * ((1 - y) / (1 + y))
    Vpred = (a / (2 * v**3)) * ((1 - 2 * a * v * y - y**2) / ((y + 1) ** 2))
    
    return (Rpred, Mpred, Vpred)