import numpy as np
from forward import forward_EZ

def simulate_data(N=100, seed=42):
    """
    Simulates N trials of data using the EZ Diffusion Model.

    Parameters:
    N (int): Number of simulated samples.
    seed (int): Random seed for reproducibility.

    Returns:
    np.ndarray: Simulated dataset (Nx6) with columns (a, v, t, Rpred, Mpred, Vpred).
    """
    np.random.seed(seed)

    # Define reasonable parameter ranges
    a_values = np.random.uniform(0.5, 2.0, N)  # Boundary separation
    v_values = np.random.uniform(0.5, 2.0, N)  # Drift rate
    t_values = np.random.uniform(0.1, 0.5, N)  # Nondecision time

    # Storage for simulated data
    data = []

    for i in range(N):
        a, v, t = a_values[i], v_values[i], t_values[i]
        Rpred, Mpred, Vpred = forward_EZ(a, v, t)
        
        data.append([a, v, t, Rpred, Mpred, Vpred])

    return np.array(data)

if __name__ == "__main__":
    simulated_data4000 = simulate_data(N=4000)  # Generate 1000 samples
    simulated_data10 = simulate_data(N=10)
    simulated_data40 = simulate_data(N=40)
    np.savetxt("simulated_data4000.csv", simulated_data4000, delimiter=",",
               header="a,v,t,Rpred,Mpred,Vpred", comments="")
    np.savetxt("simulated_data10.csv", simulated_data10, delimiter=",",
               header="a,v,t,Rpred,Mpred,Vpred", comments="")
    np.savetxt("simulated_data40.csv", simulated_data40, delimiter=",",
               header="a,v,t,Rpred,Mpred,Vpred", comments="")

    print("Simulation complete. Data saved to simulated_data400.csv, simalated_data10.csv and simulated_data40.csv")
