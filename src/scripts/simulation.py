import numpy as np
import paths


def run():
    return np.arange(200)

# Run the simulation for some inputs
data = run()
np.savetxt(paths.data / "simulation.dat", data)
