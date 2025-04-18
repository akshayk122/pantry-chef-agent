


# 🤖 AI Recipe Generator

An intelligent recipe assistant that suggests personalized meal ideas based on your pantry, dietary goals, and preferences powered by Gemini + smolagents.

---

### 🚀 Features

- 🧠 Uses Google Gemini to plan recipes step-by-step  
- 🧂 Checks your pantry and suggests what you can cook  
- 🔎 Searches for real recipes online using DuckDuckGo  
- 🧮 Estimates calories for ingredients  
- 🧰 Modular tool system: search, pantry, memory, calorie estimator  

---

### 🗂️ Project Structure

```
project-root/
│
├── agent.py                  # Main script to run the recipe agent
├── gemini_model.py           # Custom wrapper for Gemini API
├── pantry.json               # JSON file with pantry items
├── tools/
│   ├── pantry_tool.py
│   ├── search_tool.py
│   ├── calorie_tool.py
│   └── memory_tool.py
```

---

### 🧪 How It Works

1. You define a goal like `"lose weight"` and a diet like `"veg"` or `"meat"`  
2. The agent looks at your pantry and constructs a search query  
3. It uses a Gemini-powered LLM to plan and call tools  
4. You get a final structured recipe with calorie estimation

---

## 🛠️ Setup

### 1. Clone and enter the project

```bash
git clone https://github.com/akshayk122/pantry-chef-agent.git
cd pantry-chef-agent
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Also install Gemini SDK:

```bash
pip install google-generativeai
```

### 4. Set your Gemini API Key

```bash
export GOOGLE_API_KEY="your-gemini-api-key"
```

---

## ▶️ Run the Agent

```bash
python agent.py
```

---

## 🧾 Sample pantry.json

```json
[
  {"item": "chicken breast", "quantity": "1 lb", "category": "protein", "expiry": "2025-05-01"},
  {"item": "olive oil", "quantity": "1 tbsp", "category": "oil", "expiry": "2025-06-01"},
  {"item": "broccoli", "quantity": "1 head", "category": "vegetable", "expiry": "2025-04-25"},
  {"item": "red bell pepper", "quantity": "1", "category": "vegetable", "expiry": "2025-04-25"}
]
```

---

## ✅ Sample Agent Output

**Recipe:** Healthy Chicken Stir-Fry with Broccoli and Bell Pepper  
**Yields:** 4 servings  
**Time:** 20 minutes  

**Description:**  
A quick and healthy stir-fry featuring tender chicken, crisp broccoli, and bell pepper in a savory soy-ginger-garlic sauce. Great served over brown rice or quinoa for a balanced meal.

**Ingredients:**
- 1 lb (450g) chicken breasts, cut into 1-inch cubes  
- 1 tablespoon olive oil  
- 1 large head broccoli, cut into florets (about 4 cups)  
- 1 red bell pepper, seeded and chopped  
- **Sauce:** 1/4 cup low-sodium soy sauce, 2 tbsp honey, 1 tbsp rice vinegar, 2 cloves garlic (minced), 1 tsp fresh ginger (grated), 1 tsp cornstarch mixed with 1 tbsp water  
- *(Optional: 1/2 tsp Sriracha or red pepper flakes for spice)*  
- *(Optional garnish: green onions, sesame seeds)*

**Instructions:**
1. Whisk together sauce ingredients (soy sauce, honey, vinegar, garlic, ginger, optional Sriracha).  
2. Heat olive oil in a large skillet/wok over medium-high heat. Cook chicken until browned (5–7 min); remove and set aside.  
3. Add broccoli and bell pepper to the skillet; stir-fry until crisp-tender (4–5 min).  
4. Return chicken to skillet. Pour sauce over everything and stir to coat.  
5. Add cornstarch slurry; stir constantly until sauce thickens (1–2 min).  
6. Serve immediately, optionally over brown rice or quinoa and with garnishes.

**Calorie Estimate (per serving):**
- Tool Estimation: **~273 kcal**
- Website Estimation: **~380 kcal**

Enjoy your healthy meal!

<img width="803" alt="image" src="https://github.com/user-attachments/assets/bb0b6e64-ec3b-4d02-a636-3783f3a1e431" />


---

## 🧠 Tools Used


- [`smolagents`](https://github.com/huggingface/smolagents) – lightweight agent framework used to develop the recipe agent with dynamic tool calling and planning  
- [`google-generativeai`](https://pypi.org/project/google-generativeai/) – used to integrate the Gemini model as the core LLM behind recipe generation  
- **DuckDuckGoSearchTool** – used as a web search tool to find relevant recipes and nutritional content online  

---
## 🧠 Flow Chart
![Recipe_Generator](https://github.com/user-attachments/assets/9975df7b-551b-4864-bae1-110e753ff762)

---
