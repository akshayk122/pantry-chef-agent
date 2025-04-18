from smolagents import Tool, DuckDuckGoSearchTool

class CalorieEstimatorTool(Tool):
    name = "calorie_estimator"
    description = "Estimates calories for ingredients by searching online"
    inputs = {
        "ingredients": {
            "type": "string",
            "description": "Comma-separated ingredients"
        }
    }
    output_type = "string"

    def forward(self, ingredients: str) -> str:
        search_tool = DuckDuckGoSearchTool()
        ingredient_list = [i.strip() for i in ingredients.split(",")]
        results = []

        for item in ingredient_list:
            query = f"calories in 100g of {item}"
            try:
                result = search_tool({"query": query})
                results.append(f"🔸 {item}: {result.splitlines()[0]}")
            except Exception as e:
                results.append(f"🔸 {item}: lookup failed")

        return "\n".join(results)
