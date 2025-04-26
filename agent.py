from flask import Flask
from tools.calorie_tool import CalorieEstimatorTool
from tools.memory_tool import MemoryTool
from tools.pantry_tool import PantryTool
from tools.search_tool import DuckDuckGoSearchTool
from smolagents import CodeAgent, HfApiModel
from gemini_model import GeminiModel
import os

app=Flask()

@app.route('/')
def index():
    return "I am Pantry Agent"


@app.route('/agent')
def agent():
    # === User Inputs ===
    goal = "lose weight"
    diet = "meat"
    pantry_json_path = "pantry.json"

    # === Initialize Tools ===
    pantry_tool = PantryTool(pantry_json_path)
    memory_tool = MemoryTool()
    search_tool = DuckDuckGoSearchTool()
    calorie_tool = CalorieEstimatorTool()


    model = GeminiModel()

    # === Fix: call get_available_items() (add parentheses)
    pantry_items = pantry_tool.get_available_items()

    # === Build Prompt

    query_text = (
        f"You are an assistant that uses tools to generate recipes.\n"
        f"Thoughts: To suggest a {diet} recipe for someone who wants to {goal}, I will search for it.\n"
        f"Code:\n```py\n"
        f"search_tool({{\"query\": \"{diet} recipe to {goal} using {', '.join(pantry_items)}\"}})\n"
        f"```\n"
        f"Once I get results, I will estimate calories and summarize them."
    )


    # === Create the Agent
    agent = CodeAgent(
        tools=[pantry_tool, search_tool, calorie_tool, memory_tool],
        model=model,
        add_base_tools=True,
        planning_interval=2
    )

    # === Execute the Agent ===
    response = agent.run(query_text)
    #print(response)
    return response


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # <-- Important
    app.run(host="0.0.0.0", port=port)