from smolagents import Tool
from langchain.docstore.document import Document
from datetime import datetime
import json

class PantryTool(Tool):
    name = "pantry_checker"
    description = "Lists non-expired pantry items from your pantry JSON."
    inputs = {
        "query": {
            "type": "string",
            "description": "A prompt or trigger to return pantry contents"
        }
    }
    output_type = "string"

    def __init__(self, json_path: str):
        with open(json_path) as f:
            self.pantry_data = json.load(f)

        self.docs = [
            Document(
                page_content="\n".join([
                    f"Item: {item['item']}",
                    f"Quantity: {item['quantity']}",
                    f"Category: {item['category']}",
                    f"Expiry: {item['expiry']}"
                ]),
                metadata={"item": item["item"], "expiry": item["expiry"]}
            )
            for item in self.pantry_data
            if self._is_not_expired(item["expiry"])
        ]

        super().__init__()

    def _is_not_expired(self, expiry_date: str) -> bool:
        return datetime.strptime(expiry_date, "%Y-%m-%d") > datetime.today()

    def forward(self, query: str) -> str:
        # Ensure the method matches the expected signature and behavior
        if not isinstance(query, str):
            raise ValueError("Query must be a string.")

        items = [doc.metadata["item"] for doc in self.docs]
        return f"Available pantry items: {', '.join(items)}"

    def get_available_items(self) -> list:
        return [doc.metadata["item"] for doc in self.docs]

    def match_recipe_ingredients(self, ingredients: list) -> bool:
        pantry_items = set(self.get_available_items())
        return any(ingredient.lower() in pantry_items for ingredient in ingredients)
