import requests
import json

def fetch_top_models():
    url = "https://huggingface.co/api/models"
    response = requests.get(url)
    models = response.json()

    sorted_models = sorted(models, key=lambda x: x['downloads'], reverse=True)
    top_models = sorted_models[:10]

    report = [{"model": model["modelId"], "downloads": model["downloads"]} for model in top_models]

    with open("top_models_report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("Report generated: top_models_report.json")

if __name__ == "__main__":
    fetch_top_models()
