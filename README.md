# 🛡️ HarmBench AI Security Benchmark

## 📝 Project Description
This project was developed during a hackathon. Its goal is to evaluate and analyze the security of open-source artificial intelligence models using the HarmBench datasets. The test results are then indexed for analysis using a containerized architecture based on the ELK stack (Elasticsearch, Logstash, Kibana).

## 🏗️ Architecture and Main Files
* **`extract.py`**: Extraction and filtering of test data (targeted categories: chemical/biological, illegal, misinformation) to generate prompts.
* **`benchmark.py`**: Main script to run security tests on the AI models.
* **`export_to_elasticsearch.py`**: Sends the evaluation results (`results.json`) to a local Elasticsearch node.
* **`docker-compose.yml`**: Docker configuration file to quickly deploy the database environment.

## ⚙️ Prerequisites
* [Docker](https://www.docker.com/) and Docker Compose installed on your machine.
* [Python 3.x](https://www.python.org/)

## 🚀 Installation and Usage

**Run the database environment and execute the scripts:**
```bash
docker-compose up -d
python harmbench-benchmark/data/extract.py
python harmbench-benchmark/benchmark.py
python harmbench-benchmark/export_to_elasticsearch.py
