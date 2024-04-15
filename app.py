from mesa.experimental import JupyterViz
from model import HotellingModel


# This function defines how agents are visually represented in the simulation.
def agent_portrayal(agent):
    # Basic portrayal with agents shown as circles.
    portrayal = {
        "Shape": "circle",  # The shape of the agent in the visualization.
        "r": 0.8,  # Radius of the circle, determining the size of the agent.
        "Filled": "true",  # Specifies that the shape should be filled.
        "Layer": 0,  # The layer on which the agent is drawn.
        # Lower numbers are drawn first.
    }

    # Check if the agent has a 'price' attribute.
    # This is to ensure compatibility
    # with different types of agents.
    if hasattr(agent, "price"):
        # The color of the agent is determined by its price to visualize
        # the pricing strategy dynamically.
        if agent.price > 12:
            portrayal[
                "color"
            ] = "#FF0000"  # Agents with a price above 12 are colored red,
            # indicating higher prices.
        elif agent.price > 8:
            portrayal["color"] = "#FFA500"  # Agents with a price above 8 and
            # up to 12 are colored orange,indicating moderate prices.
        else:
            portrayal["color"] = "#00FF00"  # Agents with a price of 8 or below
            # are colored green,indicating lower prices.

    return portrayal  # Return the portrayal dictionary to be used by
    # the visualization engine.


model_params = {
    "N": {
        "type": "SliderInt",
        "value": 20,
        "label": "Number of agents:",
        "min": 10,
        "max": 100,
        "step": 1,
    },
    "mode": {
        "type": "Select",
        "value": "default",
        "label": "Mode:",
        "values": ["default", "pricing_only", "moving_only"]
    },
    "environment_type": {
        "type": "Select",
        "value": "grid",
        "label": "Environment Type:",
        "values": ["grid", "line"]
    },
    "mobility_rate": {
        "type": "SliderInt",
        "value": 100,
        "label": "Mobility Rate (%):",
        "min": 1,
        "max": 100,
        "step": 1,
    },
    "width": {
        "type": "SliderInt",
        "value": 20,  # Adjusted from 10 to 20 for wider grid
        "label": "Grid Width:",
        "min": 10,
        "max": 50,
        "step": 1,
    },
    "height": {
        "type": "SliderInt",
        "value": 20,  # Adjusted from 10 to 20 for taller grid
        "label": "Grid Height:",
        "min": 10,
        "max": 50,
        "step": 1,
    },
}

# Instantiate the JupyterViz component with your model
page = JupyterViz(
    model_class=HotellingModel,
    model_params=model_params,
    measures=["Average Price", "Total Revenue", "Price Variance"],
    name="Hotelling's Law Model",
    agent_portrayal=agent_portrayal,
)

# Display the visualization in the Jupyter Notebook
page
