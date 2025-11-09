# main.py
from fastapi import FastAPI, HTTPException, Path
from typing import List, Optional
import uuid

# Les imports locaux sont nécessaires et supposés exister dans le projet
# Votre Chef de Groupe a défini ces modules :
# from schemas import ProjectCreate, Project, GradeUpdate
# from db import load_db, save_db
# Puisque je n'ai pas le contenu de schemas.py et db.py, je les garde.

# J'ai ajouté ces lignes ici pour simuler les imports manquants si vous n'avez pas ces fichiers
# Si votre chef de groupe a bien créé ces fichiers, vous pouvez ignorer cette partie
# MAIS si votre API ne démarre pas, c'est que ces fichiers manquent ou sont mal nommés.
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
    from pydantic import BaseModel
    class ProjectCreate(BaseModel):
        studentName: str
        course: str
        githubUrl: str
    class Project(ProjectCreate):
        id: str
        grade: Optional[int] = None
    class GradeUpdate(BaseModel):
        grade: int
# Fin de la simulation temporaire


app = FastAPI(
    title="ProjetAPI - Gestion des Projets Étudiants",
    version="1.0.0",
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/projects", response_model=Project, tags=["Projets"])
def create_project(project: ProjectCreate):
    projects = load_db()
    new_id = str(uuid.uuid4())[:8]
    new_project = {
        "id": new_id,
        **project.model_dump(),  # Utiliser model_dump() pour Pydantic v2
        "grade": None,
    }
    projects.append(new_project)
    save_db(projects)
    return Project(**new_project)


# code de pouhe
@app.put("/projects/{project_id}/grade", response_model=Project, tags=["Projets"])
def grade_project(
    # ARGUMENT OBLIGATOIRE EN PREMIER (CORRECTION DE LA SYNTAXE PYTHON)
    grade_data: GradeUpdate,
    # ARGUMENT AVEC VALEUR PAR DÉFAUT EN DEUXIÈME (FastAPI Path)
    project_id: str = Path(..., description="ID du projet à noter"),
):
    projects = load_db()
    project = next((p for p in projects if p["id"] == project_id), None)

    if not project:
        raise HTTPException(status_code=404, detail="Projet non trouvé")

    # Mise à jour du grade (grade_data est garanti d'être présent)
    project["grade"] = grade_data.grade

    save_db(projects)

    # Retourne le modèle Pydantic mis à jour
    return Project(**project)


@app.get("/projects", response_model=List[Project], tags=["Projets"])
def list_projects():
    return [Project(**p) for p in load_db()]
