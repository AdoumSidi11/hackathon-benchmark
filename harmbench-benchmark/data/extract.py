import pandas as pd # type: ignore
import json

# Charger le CSV
df = pd.read_csv("C:/Users/bamba/HarmBench/data/behavior_datasets/harmbench_behaviors_text_all.csv")

# Catégories ciblées
categories = ["chemical_biological", "illegal", "misinformation_disinformation"]
subset = []

for cat in categories:
    filtered = df[df["SemanticCategory"] == cat]
    sampled = filtered.sample(n=10, random_state=42)
    for _, row in sampled.iterrows():
        subset.append({
            "id": row["BehaviorID"],
            "category": cat,
            "prompt": row["Behavior"]
        })

# Sauvegarder en JSON
with open("prompts.json", "w", encoding="utf-8") as f:
    json.dump(subset, f, ensure_ascii=False, indent=4)