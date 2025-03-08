from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import Slider

class MovingAgent(Agent):
    """An agent that moves randomly on a grid."""
    
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        """Move to a random neighboring cell."""
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

class SimpleModel(Model):
    """A simple agent-based model with a grid and movement."""
    
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = MultiGrid(width, height, torus=True)  # Torus = wraparound edges
        self.schedule = RandomActivation(self)

        # Create agents and place them randomly on the grid
        for i in range(self.num_agents):
            agent = MovingAgent(i, self)
            self.schedule.add(agent)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x, y))

    def step(self):
        """Advance the model by one step."""
        self.schedule.step()

# Visualization function
def agent_portrayal(agent):
    """Define how agents are displayed on the grid."""
    return {"Shape": "circle", "Color": "red", "Filled": True, "r": 0.8}

# Create a grid visualization
grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)  # 10x10 grid, 500x500 pixels

# Set up the interactive model server
server = ModularServer(SimpleModel,
                       [grid],
                       "Simple ABM",
                       {"N": Slider("Number of Agents", 5, 1, 20, 1),
                        "width": 10, "height": 10})

if __name__ == "__main__":
    server.launch()