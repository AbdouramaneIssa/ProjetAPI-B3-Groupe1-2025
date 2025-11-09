// script.js

const API_BASE_URL = window.location.origin; // L'API est servie sur le même domaine

document.addEventListener('DOMContentLoaded', () => {
    loadProjects();
    document.getElementById('project-form').addEventListener('submit', handleProjectSubmit);
});

/**
 * Charge et affiche la liste des projets.
 */
async function loadProjects() {
    try {
        const response = await fetch(`${API_BASE_URL}/projects`);
        if (!response.ok) {
            throw new Error(`Erreur HTTP: ${response.status}`);
        }
        const projects = await response.json();
        renderProjects(projects);
    } catch (error) {
        console.error("Erreur lors du chargement des projets:", error);
        document.getElementById('projects-table-body').innerHTML = `<tr><td colspan="6" class="text-danger text-center">Erreur de connexion à l'API.</td></tr>`;
    }
}

/**
 * Affiche les projets dans le tableau.
 * @param {Array<Object>} projects - La liste des projets.
 */
function renderProjects(projects) {
    const tableBody = document.getElementById('projects-table-body');
    tableBody.innerHTML = ''; // Vider le tableau

    if (projects.length === 0) {
        tableBody.innerHTML = `<tr><td colspan="6" class="text-center">Aucun projet soumis pour le moment.</td></tr>`;
        return;
    }

    projects.forEach(project => {
        const row = tableBody.insertRow();

        // ID
        row.insertCell().textContent = project.id;

        // Nom de l'Étudiant
        row.insertCell().textContent = project.studentName;

        // Cours
        row.insertCell().textContent = project.course;

        // URL GitHub
        const githubCell = row.insertCell();
        const githubLink = document.createElement('a');
        githubLink.href = project.githubUrl;
        githubLink.textContent = 'Voir le dépôt';
        githubLink.target = '_blank';
        githubCell.appendChild(githubLink);

        // Note
        const gradeCell = row.insertCell();
        if (project.grade !== null && project.grade !== undefined) {
            gradeCell.innerHTML = `<span class="grade-display">${project.grade}/20</span>`;
        } else {
            gradeCell.innerHTML = `<span class="no-grade">Non noté</span>`;
        }

        // Action (Bouton Noter)
        const actionCell = row.insertCell();
        const gradeButton = document.createElement('button');
        gradeButton.textContent = 'Noter';
        gradeButton.classList.add('btn', 'btn-sm', 'btn-warning', 'btn-action');
        gradeButton.onclick = () => promptForGrade(project.id);
        actionCell.appendChild(gradeButton);

        // Action (Bouton Supprimer)
        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Supprimer';
        deleteButton.classList.add('btn', 'btn-sm', 'btn-danger', 'btn-action');
        deleteButton.onclick = () => deleteProject(project.id);
        actionCell.appendChild(deleteButton);
    });
}

/**
 * Gère la soumission du formulaire de nouveau projet.
 * @param {Event} event - L'événement de soumission.
 */
async function handleProjectSubmit(event) {
    event.preventDefault();
    const form = event.target;
    const messageDiv = document.getElementById('form-message');
    messageDiv.textContent = '';
    messageDiv.className = 'mt-3';

    const projectData = {
        studentName: form.elements.studentName.value,
        course: form.elements.course.value,
        githubUrl: form.elements.githubUrl.value,
    };

    try {
        const response = await fetch(`${API_BASE_URL}/projects`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(projectData),
        });

        const result = await response.json();

        if (response.ok) {
            messageDiv.classList.add('alert', 'alert-success');
            messageDiv.textContent = `Projet soumis avec succès ! ID: ${result.id}`;
            form.reset();
            loadProjects(); // Recharger la liste
        } else {
            messageDiv.classList.add('alert', 'alert-danger');
            messageDiv.textContent = `Erreur lors de la soumission: ${result.detail || 'Erreur inconnue'}`;
        }
    } catch (error) {
        console.error("Erreur de soumission:", error);
        messageDiv.classList.add('alert', 'alert-danger');
        messageDiv.textContent = "Erreur de connexion à l'API lors de la soumission.";
    }
}

/**
 * Demande une note à l'utilisateur et appelle l'API pour noter le projet.
 * @param {string} projectId - L'ID du projet à noter.
 */
async function promptForGrade(projectId) {
    const grade = prompt("Entrez la note (sur 20) pour le projet " + projectId + ":");
    const gradeNumber = parseInt(grade, 10);

    if (grade === null || isNaN(gradeNumber) || gradeNumber < 0 || gradeNumber > 20) {
        if (grade !== null) {
            alert("Note invalide. Veuillez entrer un nombre entre 0 et 20.");
        }
        return;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/projects/${projectId}/grade`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ grade: gradeNumber }),
        });

        if (response.ok) {
            alert(`Projet ${projectId} noté avec succès: ${gradeNumber}/20.`);
            loadProjects(); // Recharger la liste
        } else {
            const result = await response.json();
            alert(`Erreur lors de la notation: ${result.detail || 'Erreur inconnue'}`);
        }
    } catch (error) {
        console.error("Erreur de notation:", error);
        alert("Erreur de connexion à l'API lors de la notation.");
    }
}

/**
 * Supprime un projet après confirmation.
 * @param {string} projectId - L'ID du projet à supprimer.
 */
async function deleteProject(projectId) {
    if (!confirm(`Êtes-vous sûr de vouloir supprimer le projet ${projectId} ?`)) {
        return;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/projects/${projectId}`, {
            method: 'DELETE',
        });

        if (response.ok) {
            alert(`Projet ${projectId} supprimé avec succès.`);
            loadProjects(); // Recharger la liste
        } else {
            const result = await response.json();
            alert(`Erreur lors de la suppression: ${result.detail || 'Erreur inconnue'}`);
        }
    } catch (error) {
        console.error("Erreur de suppression:", error);
        alert("Erreur de connexion à l'API lors de la suppression.");
    }
}
