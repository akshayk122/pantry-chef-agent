from smolagents import Tool


class MemoryTool(Tool):
    name = "recipe_memory"
    description = "Stores recipe names so the app can avoid suggesting duplicate meals."
    inputs = {
        "recipe_name": {
            "type": "string",
            "description": "The exact recipe name to remember"
        }
    }
    output_type = "string"

    def __init__(self, memory=None):
        self.memory = memory if memory is not None else []
        super().__init__()

    def forward(self, recipe_name: str) -> str:
        if not isinstance(recipe_name, str):
            raise ValueError("recipe_name must be a string.")

        recipe_name = recipe_name.strip()
        if not recipe_name:
            return "No recipe name was provided."

        if recipe_name.lower() in [item.lower() for item in self.memory]:
            return f"⚠️ '{recipe_name}' was already suggested before."

        self.memory.append(recipe_name)
        return f"✅ Remembered '{recipe_name}'."

    def get_memory(self):
        return list(self.memory)
