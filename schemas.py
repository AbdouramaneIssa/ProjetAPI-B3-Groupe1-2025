from pydantic import BaseModel
from typing import Optional


class ProjectCreate(BaseModel):
    studentName: str
    course: str
    githubUrl: str


class Project(ProjectCreate):
    id: str
    grade: Optional[int] = None


class GradeUpdate(BaseModel):
    grade: int
