# main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
import os

# Imports locaux
from schemas import ProjectCreate, Project, GradeUpdate
from db import load_db, save_db

# Définir le chemin de base pour les fichiers statiques
STATIC_DIR = "static"

# Créer l'application FastAPI
app = FastAPI(
    title="ProjetAPI - Gestion des Projets Étudiants",
    description="API REST pour la soumission et la notation de projets étudiants.",
    version="1.0.0",
)

# Servir les fichiers statiques (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Page HTML principale (interface web)
@app.get("/", include_in_schema=False)
async def serve_index():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))

# Endpoint d'information basique
@app.get("/docs", include_in_schema=True)
def read_root():
    return {"message": "Bienvenue sur l'API ProjetAPI. Accédez à /docs pour la documentation Swagger."}


# ============================================================
# ✅ ZONE API — LES MEMBRES DU GROUPE DOIVENT COLLER LEUR CODE ICI
# ============================================================


# ------------------------------------------------------------
# ✅ 1️⃣ Abdouramane — POST /projects
# COLLER ICI ton endpoint POST /projects
# ------------------------------------------------------------


# ------------------------------------------------------------
# ✅ 2️⃣ Elbachir — GET /projects
# COLLER ICI ton endpoint list_projects()
# ------------------------------------------------------------


# ------------------------------------------------------------
# ✅ 3️⃣ Kelly — GET /projects/{id}
# COLLER ICI ton endpoint get_project()
# ------------------------------------------------------------


# ------------------------------------------------------------
# ✅ 4️⃣ Nambogona — GET /projects/course/{courseName}
# COLLER ICI ton endpoint list_projects_by_course()
# ------------------------------------------------------------


# ------------------------------------------------------------
# ✅ 5️⃣ Elie-Junior — PUT /projects/{id}/grade
# COLLER ICI ton endpoint grade_project()
# ------------------------------------------------------------


# ------------------------------------------------------------
# ✅ 6️⃣ Booz — DELETE /projects/{id}
# COLLER ICI ton endpoint delete_project()
# ------------------------------------------------------------


# ✅ FIN DES ZONES — NE PAS MODIFIER LE RESTE DU FICHIER
