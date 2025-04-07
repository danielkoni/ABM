import seaborn as sns
import matplotlib.pyplot as plt
from money_model import MoneyModel

starter_model = MoneyModel(10)
starter_model.step()

model = MoneyModel(10) # Tells the model to reate 10 agents
for _ in range(
    30
): #Runs the model for 10 steps; an underscore is convention for a variable that is not used
    model.step()


agent_wealth = [a.wealth for a in model.agents]
# Create a histogram with seaborn
g = sns.histplot(agent_wealth, discrete = True)
g.set(
    title="Wealth distribution", xlabel="Wealth", ylabel="number of agents"
); # The semicolon is just to avoid printing the object representation


all_wealth = []
# This runs the model 100 times, each model executing 10 steps
for _ in range(100):
    # Run the model
    model = MoneyModel(10)
    for _ in range(30):
        model.step()

    # Store the results
    for agent in model.agents:
        all_wealth.append(agent.wealth)


g = sns.histplot(all_wealth, discrete=True)
g.set(title="Wealth distribution", xlabel="Wealth", ylabel="number of agents");


plt.show()