import json
CONFIG_FILE = "config.json"
def load_config():
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)
def change(name,number):
    config = load_config()
    config[str(name)]=number
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
