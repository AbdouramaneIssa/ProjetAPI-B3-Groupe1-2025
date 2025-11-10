# main.py
from fastapi import FastAPI, HTTPException, Path
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from typing import List, Optional # Ajoutez List et Optional pour les imports
import os
import uuid # Ajoutez uuid pour la fonction create_project
from pydantic import BaseModel # Ajoutez BaseModel si vous gardez la simulation

# Les imports locaux sont nécessaires et supposés exister dans le projet
# Votre Chef de Groupe a défini ces modules :
try:
    from schemas import ProjectCreate, Project, GradeUpdate
    from db import load_db, save_db
except ImportError:
    # Ceci est une solution temporaire pour les tests si les fichiers n'existent pas encore
    print("ATTENTION: Les fichiers schemas.py ou db.py sont manquants. Le code pourrait échouer au lancement.")
    
    # --- SIMULATION DE db.py (temporaire) ---
    def load_db(): return []
    def save_db(data): pass
    
    # --- SIMULATION DE schemas.py (temporaire) ---
    # Ces définitions sont nécessaires si les imports échouent
    class ProjectCreate(BaseModel):
        studentName: str
        course: str
        githubUrl: str
    class Project(ProjectCreate):
        id: str
        grade: Optional[int] = None
    class GradeUpdate(BaseModel):
        grade: int

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
# Permet d'ajouter un nouveau projet étudiant dans la base de données.

@app.post("/projects", response_model=Project, tags=["Projets"], status_code=201) # Fusion des deux versions ici
def create_project(project: ProjectCreate):
    projects = load_db()
    # import uuid a été déplacé en haut
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

@app.get("/projects", response_model=List[Project])
def list_projects():
    return [Project(**p) for p in load_db()]
# ------------------------------------------------------------


# ------------------------------------------------------------
# ✅ 3️⃣ Kelly — GET /projects/{id}
# COLLER ICI ton endpoint get_project()
# ------------------------------------------------------------


# ------------------------------------------------------------
# ✅ 4️⃣ Nambogona — GET /projects/course/{courseName}

@app.get("/projects/course/{course_name}", response_model=List[Project], tags=["Projets"])
def list_projects_by_course(course_name: str):
    projects = load_db()
    filtered = [p for p in projects if p["course"].lower() == course_name.lower()]
    return [Project(**p) for p in filtered]
# ------------------------------------------------------------


# ------------------------------------------------------------
# ✅ 5️⃣ Elie-Junior — PUT /projects/{id}/grade
@app.put("/projects/{project_id}/grade", response_model=Project)
def grade_project(project_id: str, grade_data: GradeUpdate):
    projects = load_db()

    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        raise HTTPException(status_code=404, detail="Projet non trouvé")

    if not (0 <= grade_data.grade <= 20):
        raise HTTPException(status_code=400, detail="La note doit être entre 0 et 20")

    project["grade"] = grade_data.grade
    save_db(projects)

    return Project(**project)

# ------------------------------------------------------------


# ------------------------------------------------------------
# ✅ 6️⃣ Booz — DELETE /projects/{id}
# COLLER ICI ton endpoint delete_project()
@app.delete("/projects/{project_id}", status_code=204)
def delete_project(project_id: str):
    projects = load_db()
    initial_len = len(projects)

    projects[:] = [p for p in projects if p["id"] != project_id]

    if len(projects) == initial_len:
        raise HTTPException(status_code=404, detail="Projet non trouvé")

    save_db(projects)
    return {"message": "Projet supprimé avec succès"}
# ------------------------------------------------------------


# ✅ FIN DES ZONES — NE PAS MODIFIER LE RESTE DU FICHIER