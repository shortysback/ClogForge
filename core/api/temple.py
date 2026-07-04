import json
import os
import requests


def sync_player(player_name):
    url = (
        "https://templeosrs.com/api/collection-log/"
        f"player_collection_log.php?player={player_name}"
        "&categories=all"
        "&includenames=1"
        "&includemissingitems=1"
    )

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()

    os.makedirs("data/players", exist_ok=True)

    file_path = f"data/players/{player_name}.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    return file_path