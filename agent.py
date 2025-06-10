"""
Flask application for an AI Recipe Generator agent.

This script initializes a Flask web server that exposes endpoints to interact
with an AI agent powered by Google's Gemini model and the smolagents framework.
The agent can suggest recipes based on user-defined goals, dietary preferences,
and available pantry items.
"""
from flask import Flask
from tools.calorie_tool import CalorieEstimatorTool
from tools.memory_tool import MemoryTool
from tools.pantry_tool import PantryTool
from tools.search_tool import DuckDuckGoSearchTool
from smolagents import CodeAgent, HfApiModel
from gemini_model import GeminiModel
import os

app = Flask(__name__)

@app.route('/')
def index():
    """Index route, can be used for health checks."""
    return "I am Pantry Agent"


@app.route('/agent')
def agent():
    """
    Main route to trigger the AI recipe agent.
    It initializes tools, defines user goals, constructs a prompt,
    and runs the agent to generate a recipe suggestion.
    """
    # === User Inputs ===
    # Define the user's dietary goal (e.g., "lose weight", "build muscle").
    goal = "lose weight"
    # Define the user's dietary preference (e.g., "meat", "veg", "vegan").
    diet = "meat"
    # Path to the JSON file containing the list of available pantry items.
    pantry_json_path = "pantry.json"

    # === Initialize Tools ===
    # Tool to manage and access pantry inventory.
    pantry_tool = PantryTool(pantry_json_path)
    # Tool to provide memory capabilities to the agent (e.g., recalling past interactions).
    memory_tool = MemoryTool()
    # Tool for performing web searches (e.g., finding recipes online).
    search_tool = DuckDuckGoSearchTool()
    # Tool for estimating calories in ingredients or recipes.
    calorie_tool = CalorieEstimatorTool()

    # Initialize the Gemini language model wrapper.
    model = GeminiModel()

    # Retrieve the list of available items from the pantry.
    pantry_items = pantry_tool.get_available_items()

    # === Build Prompt ===
    # This prompt guides the agent's reasoning process. It includes:
    # - A system message defining the agent's role.
    # - A "Thoughts" section to outline the initial plan.
    # - A "Code" section with an example of how to use a tool (search_tool in this case).
    # This structure is designed for an agent that can plan and execute code/tool calls.
    query_text = (
        f"You are an assistant that uses tools to generate recipes.\n"
        f"Thoughts: To suggest a {diet} recipe for someone who wants to {goal}, I will search for it.\n"
        f"Code:\n```py\n"
        f"search_tool({{\"query\": \"{diet} recipe to {goal} using {', '.join(pantry_items)}\"}})\n"
        f"```\n"
        f"Once I get results, I will estimate calories and summarize them."
    )


    # === Create the Agent ===
    # Initialize the CodeAgent with the defined tools and model.
    # - tools: A list of tools the agent can use.
    # - model: The language model instance.
    # - add_base_tools: If True, includes basic tools like a Python interpreter for the agent.
    # - planning_interval: How many steps the agent takes before replanning.
    agent = CodeAgent(
        tools=[pantry_tool, search_tool, calorie_tool, memory_tool],
        model=model,
        add_base_tools=True,
        planning_interval=2
    )

    # === Execute the Agent ===
    # Run the agent with the constructed query prompt.
    # The agent will process the prompt, potentially use tools, and generate a response.
    response = agent.run(query_text)
    # print(response) # Uncomment for debugging to see the raw agent response.
    return response


if __name__ == "__main__":
    # Reads the port from the PORT environment variable, defaulting to 8080.
    # This is important for compatibility with deployment platforms like Google Cloud Run or Heroku.
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)