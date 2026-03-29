
+import json
from elasticsearch import Elasticsearch, helpers

# -----------------------------
# 1. Connexion à Elasticsearch
# -----------------------------
es = Elasticsearch("http://localhost:9200")

index_name = "harmbench-results"

# -----------------------------
# 2. Création de l'index (si besoin)
# -----------------------------
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)
    print(f"Index '{index_name}' créé.")
else:
    print(f"Index '{index_name}' déjà existant.")

# -----------------------------
# 3. Charger les résultats
# -----------------------------
with open("results.json", "r", encoding="utf-8") as f:
    results = json.load(f)

print(f"{len(results)} documents chargés depuis results.json")

# -----------------------------
# 4. Préparer les actions bulk
# -----------------------------
actions = []

for item in results:
    actions.append({
        "_index": index_name,
        "_source": item
    })

# -----------------------------
# 5. Envoi en bulk
# -----------------------------
helpers.bulk(es, actions)
print("Export vers Elasticsearch terminé !")
