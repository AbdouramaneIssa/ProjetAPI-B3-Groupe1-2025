# db.py
import json
import os
from typing import List, Dict, Any

# Le fichier db.json est à la racine du projet
DB_FILE = "db.json"


def load_db() -> List[Dict[str, Any]]:
    """Charge les données du fichier JSON."""
    if not os.path.exists(DB_FILE):
        return []
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            # S'assurer que le fichier n'est pas vide
            content = f.read()
            if not content:
                return []
            return json.loads(content)
    except json.JSONDecodeError:
        # Si le fichier est corrompu ou contient du JSON invalide
        return []


def save_db(data: List[Dict[str, Any]]) -> None:
    """Sauvegarde les données dans le fichier JSON."""
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
