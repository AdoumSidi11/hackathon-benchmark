# 🛡️ HarmBench AI Security Benchmark

## 📝 Description du Projet
Ce projet a été développé dans le cadre d'un hackathon. Il a pour objectif d'évaluer et d'analyser la sécurité des modèles d'intelligence artificielle open-source en s'appuyant sur les datasets de HarmBench. Les résultats des tests sont ensuite indexés pour être analysés grâce à une architecture conteneurisée basée sur la stack ELK (Elasticsearch, Logstash, Kibana).

## 🏗️ Architecture et Fichiers Principaux
* **`extract.py`** : Extraction et filtrage des données de test (catégories ciblées : chimique/biologique, illégal, désinformation) pour générer les prompts.
* **`benchmark.py`** : Script principal permettant d'exécuter les tests de sécurité sur les modèles d'IA.
* **`export_to_elasticsearch.py`** : Envoi des résultats d'évaluation (`results.json`) vers un nœud Elasticsearch local.
* **`docker-compose.yml`** : Fichier de configuration Docker pour déployer rapidement l'environnement de base de données.

## ⚙️ Prérequis
* [Docker](https://www.docker.com/) et Docker Compose installés sur votre machine.
* [Python 3.x](https://www.python.org/)

## 🚀 Installation et Utilisation

**1. Lancer l'environnement de données (Elasticsearch)**
```bash
docker-compose up -d
python harmbench-benchmark/data/extract.py
python harmbench-benchmark/benchmark.py
python harmbench-benchmark/export_to_elasticsearch.py
