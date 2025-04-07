import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import Spatial_MoneyModel
from Spatial_MoneyModel import MoneyModel

model = MoneyModel(100, 10, 10)
for _ in range(10):
    model.step()


agent_counts = np.zeros((model.grid.width, model.grid.height))
for cell_content, (x, y) in model.grid.coord_iter():
    agent_count = len(cell_content)
    agent_counts [x] [y] = agent_count
# Plot using seaborn, with a visual size of 5x5
g = sns.heatmap(agent_counts, cmap="viridis", annot=True, cbar=False, square=True)
g.figure.set_size_inches(5, 5)
g.set(title="number of agents on each cell of the grid");
plt.show()