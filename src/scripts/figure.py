import matplotlib.pyplot as plt
import numpy as np
import paths

data = np.loadtxt(paths.data / "simulation.dat")

# Plot the results
fig, ax = plt.subplots(1)
ax.plot(data, color="k")
fig.savefig(paths.figures / "figure.pdf")
