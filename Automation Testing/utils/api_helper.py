import requests
import yaml
import os

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

config = load_config()
BASE_URL = config["base_url"]

def get(endpoint):
    url = BASE_URL + endpoint
    response = requests.get(url)
    return response

def post(endpoint, payload):
    url = BASE_URL + endpoint
    response = requests.post(url, json=payload)
    return response
