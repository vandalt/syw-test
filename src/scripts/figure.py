import simulation
import matplotlib.pyplot as plt
import paths

# Run the simulation for some inputs
data = simulation.run()

# Plot the results
fig, ax = plt.subplots(1)
ax.plot(data, color="k")
fig.savefig(paths.figures / "figure.pdf")
