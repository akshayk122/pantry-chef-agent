# PantryChef AI

<div align="center">

  <img src="https://github-readme-stats.vercel.app/api?username=akshayk122&show_icons=true&theme=tokyonight&include_all_commits=true&count_private=true&border_radius=10&hide_title=true" height="165em" alt="GitHub Stats" />
  <img src="https://streak-stats.demolab.com/?user=akshayk122&theme=tokyonight&hide_border=true&border_radius=10" height="165em" alt="GitHub Streak" />

</div>

PantryChef AI is a smart recipe assistant that turns what you already have at home into delicious, practical meal ideas. It combines your pantry inventory, dietary goals, and web research to suggest recipes that are relevant, nutritious, and easy to cook.

Built with Google's Gemini model and the `smolagents` framework, PantryChef AI can reason through your ingredients, search for suitable recipes, estimate calories, and produce a final recommendation tailored to your needs.

---

## Why this project stands out

- Uses your actual pantry items instead of generic recipe suggestions
- Adapts to a goal such as weight loss, muscle gain, or simple home cooking
- Supports dietary preferences like meat, veg, or vegan
- Pulls in web-based recipe inspiration and nutrition data
- Provides a coherent final output with ingredients, instructions, and calorie estimates

---

## Key features

- 🧠 AI-powered recipe planning using Gemini
- 🛒 Pantry-aware suggestions based on saved ingredients
- 🔎 Web search for relevant recipe ideas and cooking inspiration
- 📏 Calorie estimation for ingredients and meals
- 🧰 Modular tool-based architecture for search, memory, pantry access, and calculations
- 🌐 Simple Flask app interface to run the assistant locally or in deployment environments

---

## Project architecture

The project is organized around a lightweight agent system:

- `agent.py` — Flask application and main agent orchestration
- `gemini_model.py` — wrappers around the Gemini API
- `pantry.json` — pantry inventory data
- `tools/` — reusable tools for pantry lookup, search, memory, and calorie estimation

This makes it easy to extend with new features or agent capabilities.

---

## Repository structure

```text
pantry-chef-agent/
├── agent.py                 # Flask server and recipe agent entry point
├── gemini_model.py          # Gemini API wrapper
├── pantry.json              # Pantry inventory source
├── requirements.txt         # Python dependencies
├── Dockerfile               # Container setup
├── tools/
│   ├── pantry_tool.py       # Reads pantry items
│   ├── search_tool.py       # Web recipe search
│   ├── calorie_tool.py      # Nutrition estimate helper
│   └── memory_tool.py       # Agent memory support
├── README.md                # Project overview and setup guide
├── deploymen_steps.txt      # Deployment notes
├── .gitignore
├── .dockerignore
└── LICENSE                  # License file (if present in your repository)
```

---

## How it works

1. The user defines a goal, such as "lose weight".
2. The agent checks the pantry inventory and identifies available ingredients.
3. It constructs a targeted search query and searches for recipe ideas.
4. The Gemini model plans a suitable recipe based on the ingredients and goals.
5. The agent estimates calories and returns a final, structured meal suggestion.

---

## Local setup

### 1. Clone the repository

```bash
git clone https://github.com/akshayk122/pantry-chef-agent.git
cd pantry-chef-agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
# On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your Gemini API key

```bash
export GOOGLE_API_KEY="your-gemini-api-key"
```

If you're using Windows PowerShell:

```powershell
$env:GOOGLE_API_KEY="your-gemini-api-key"
```

---

## Run the app

```bash
python agent.py
```

By default, the Flask app runs on port `8080` unless a different port is provided through the `PORT` environment variable.

---

## Example pantry data

```json
[
  {"item": "chicken breast", "quantity": "1 lb", "category": "protein", "expiry": "2025-05-01"},
  {"item": "olive oil", "quantity": "1 tbsp", "category": "oil", "expiry": "2025-06-01"},
  {"item": "broccoli", "quantity": "1 head", "category": "vegetable", "expiry": "2025-04-25"},
  {"item": "red bell pepper", "quantity": "1", "category": "vegetable", "expiry": "2025-04-25"}
]
```

---

## Example output

```text
Recipe: Healthy Chicken Stir-Fry with Broccoli and Bell Pepper
Yields: 4 servings
Time: 20 minutes

Description:
A quick and balanced stir-fry with tender chicken, broccoli, and bell pepper.

Ingredients:
- 1 lb chicken breast
- 1 tbsp olive oil
- 1 head broccoli
- 1 red bell pepper
- Soy sauce, garlic, ginger, and optional chili flakes

Instructions:
1. Sauté the chicken until cooked.
2. Add vegetables and cook until vibrant and crisp.
3. Mix in sauce and toss thoroughly.
4. Serve warm with rice or quinoa.

Calorie estimate:
- Tool estimate: ~273 kcal per serving
- Web estimate: ~380 kcal per serving
```

---

## Tech stack

- Python
- Flask
- Google Gemini API
- `smolagents`
- DuckDuckGo search integration
- JSON-based pantry management

---

## Future improvements

- Add user authentication and saved profiles
- Support meal planning for multiple days
- Include grocery suggestions when pantry items are insufficient
- Add image-based ingredient recognition
- Improve recipe filtering for allergies and cuisines

---

## Contributing

Contributions are welcome. If you'd like to improve the project, please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test the behavior locally
5. Submit a pull request with a clear description

Example:

```bash
git checkout -b feature/new-recipe-feature
git commit -m "Add support for dietary filters"
git push origin feature/new-recipe-feature
```

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## A quick note

PantryChef AI is designed to be practical, approachable, and useful in everyday cooking. The goal is not just to generate recipes, but to help people make better use of what they already have while reducing food waste and making meal planning easier.

If you enjoy the project, feel free to star the repository and contribute new ideas.
