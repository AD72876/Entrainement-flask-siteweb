import json
import os

FICHIER_JOHNSON = "messages.json"

def charger_messages():
    if os.path.exists(FICHIER_JOHNSON):
        with open(FICHIER_JOHNSON, "r", encoding="utf-8") as f:
            data = json.load(f)

            if not isinstance(data, list):
                return []

            return data
    return []


def sauvegarder_messages(messages):
    with open(FICHIER_JOHNSON, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=4, ensure_ascii=False)
