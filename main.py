# main.py
from fastapi import FastAPI, HTTPException, Path
from typing import List, Optional
import uuid

# Imports locaux
from schemas import ProjectCreate, Project, GradeUpdate
from db import load_db, save_db

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/projects", response_model=Project)
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


@app.put("/projects/{project_id}/grade", response_model=Project)
def grade_project(
    project_id: str = Path(..., description="ID du projet à noter"),
    grade_data: Optional[GradeUpdate] = None,
):
    projects = load_db()
    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        raise HTTPException(status_code=404, detail="Projet non trouvé")
    if grade_data:
        project["grade"] = grade_data.grade
    save_db(projects)
    return Project(**project)


@app.get("/projects", response_model=List[Project])
def list_projects():
    return [Project(**p) for p in load_db()]
