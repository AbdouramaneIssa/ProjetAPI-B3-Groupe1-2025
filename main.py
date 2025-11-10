# main.py
from fastapi import FastAPI, HTTPException, Path
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from typing import List
import os
import uuid

# Imports locaux (ils existent déjà dans ton projet)
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
async def serve_index() -> FileResponse:
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))


# Endpoint d'information basique
@app.get("/docs", include_in_schema=True)
def read_root() -> dict:
    return {
        "message": "Bienvenue sur l'API ProjetAPI. Accédez à /docs pour la documentation Swagger."
    }


# ============================================================
# ✅ ZONE API — LES MEMBRES DU GROUPE DOIVENT COLLER LEUR CODE ICI
# ============================================================


# ------------------------------------------------------------
# ✅ 1️⃣ Abdouramane — POST /projects
# Permet d'ajouter un nouveau projet étudiant dans la base de données.
@app.post("/projects", response_model=Project, tags=["Projets"], status_code=201)
def create_project(project: ProjectCreate) -> Project:
    projects = load_db()
    new_id = str(uuid.uuid4())[:8]
    new_project = {
        "id": new_id,
        **project.model_dump(),
        "grade": None,
    }
    projects.append(new_project)
    save_db(projects)
    return Project(**new_project)
# ------------------------------------------------------------


# ------------------------------------------------------------
# ✅ 2️⃣ Elbachir — GET /projects
@app.get("/projects", response_model=List[Project], tags=["Projets"])
def list_projects() -> List[Project]:
    return [Project(**p) for p in load_db()]
# ------------------------------------------------------------


# ------------------------------------------------------------
# ✅ 3️⃣ Kelly — GET /projects/{id}
# (à compléter plus tard)
# ------------------------------------------------------------


# ------------------------------------------------------------
# ✅ 4️⃣ Nambogona — GET /projects/course/{course_name}
@app.get("/projects/course/{course_name}", response_model=List[Project], tags=["Projets"])
def list_projects_by_course(course_name: str) -> List[Project]:
    projects = load_db()
    filtered = [p for p in projects if p["course"].lower() == course_name.lower()]
    return [Project(**p) for p in filtered]
# ------------------------------------------------------------


# ------------------------------------------------------------
# ✅ 5️⃣ Elie-Junior — PUT /projects/{id}/grade
@app.put("/projects/{project_id}/grade", response_model=Project, tags=["Projets"])
def grade_project(
    grade_data: GradeUpdate,
    project_id: str = Path(..., description="ID du projet à noter"),
) -> Project:
    projects = load_db()
    project = next((p for p in projects if p["id"] == project_id), None)

    if not project:
        raise HTTPException(status_code=404, detail="Projet non trouvé")

    project["grade"] = grade_data.grade
    save_db(projects)
    return Project(**project)
# ------------------------------------------------------------


# ------------------------------------------------------------
# ✅ 6️⃣ Booz — DELETE /projects/{id}
# (à compléter plus tard)
# ------------------------------------------------------------


# ✅ FIN DES ZONES — NE PAS MODIFIER LE RESTE DU FICHIER
