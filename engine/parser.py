import json
import os


def load_player(player_name):

    filename = os.path.join(
        "data",
        "players",
        f"{player_name}.json"
    )

    with open(filename, "r", encoding="utf-8") as f:
        raw = json.load(f)

    data = raw["data"]

    return {
        "player": data["player"],
        "last_checked": data["last_checked"],
        "completed": data["total_collections_finished"],
        "available": data["total_collections_available"],
        "percent": (
            data["total_collections_finished"]
            / data["total_collections_available"]
        ) * 100,
        "activities": data["items"],
    }