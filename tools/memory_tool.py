from smolagents import Tool

class MemoryTool(Tool):
    name = "recipe_memory"
    description = "Stores recipe names to avoid suggesting duplicates"
    inputs = {
        "recipe_name": {
            "type": "string",
            "description": "The name of the recipe to remember"
        }
    }
    output_type = "string"

    def __init__(self):
        self.memory = []
        super().__init__()

    def forward(self, recipe_name: str) -> str:
        if recipe_name.lower() in [r.lower() for r in self.memory]:
            return f"⚠️ '{recipe_name}' was already suggested before."
        self.memory.append(recipe_name)
        return f"✅ Remembered '{recipe_name}'."
