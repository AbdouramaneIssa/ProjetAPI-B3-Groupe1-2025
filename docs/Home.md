\# Travail Pratique (TP) Versioning Git et GitHub \[B3 Jou/Soir]



\*\*Module\*\* : Versioning et Gestion de Projet  

\*\*Niveau\*\* : Bachelor 3 Informatique  

\*\*Titre du TP\*\* : Git Flow au Pipeline DevOps : Construire et Automatiser une API Métier  

\*\*Durée\*\* : 3 jours  



---



\## 1. Objectifs Pédagogiques



Ce TP est conçu pour vous faire maîtriser le \*\*cycle de vie complet d’un projet logiciel en équipe\*\*. À la fin du projet, vous serez capable de :



\- Structurer un projet en utilisant le \*\*modèle Git Flow\*\* (`main`, `develop`, `feature`)

\- Utiliser les \*\*Git Hooks locaux\*\* (`pre-commit`) pour garantir la qualité du code avant le push

\- Collaborer efficacement sur \*\*GitHub\*\* (Issues, Pull Requests, revues de code)

\- Gérer les \*\*conflits de merge\*\* de manière professionnelle

\- Automatiser les processus qualité (CI) avec \*\*GitHub Actions\*\*

\- Intégrer une \*\*revue de code automatique par IA (LLM)\*\*

\- Gérer les \*\*Secrets GitHub\*\* pour les clés d’API et les notifications

\- Publier des \*\*versions logicielles\*\* (Tags \& Releases)



---



\## 2. Configuration de l’Équipe



\- \*\*Taille\*\* : Groupes de 5 à 7 étudiants

\- \*\*Rôles\*\* : Un membre du groupe sera désigné comme \*\*Lead\*\* ou \*\*Maintainer\*\* (il sera responsable de la création du dépôt, de la configuration des protections de branches, et des merges finaux)

\- \*\*Outil\*\* : Chaque groupe travaillera sur un \*\*dépôt privé\*\* sur GitHub. Le Lead invitera les autres membres comme collaborateurs.



---



\## 3. Le Projet Métier : `ProjetAPI`



Vous allez développer une \*\*API REST simple\*\* pour gérer les \*\*soumissions de projets étudiants pour un cours\*\*.



\### Technologie (au choix du groupe) :

\- \*\*Option A (TypeScript)\*\* : Node.js + Express.js + Zod (pour la validation des données)

\- \*\*Option B (Python)\*\* : \*\*FastAPI + Pydantic\*\* (pour la validation des données)



> \*\*Stockage des données\*\* : Pour simplifier, aucune base de données n’est requise. \*\*Utilisez un fichier `db.json`\*\* pour stocker les projets. Cela permettra de simuler les \*\*conflits de merge\*\* lors des modifications simultanées.



\### Fonctionnalités (issues) :

1\. `POST /projects` : Soumettre un nouveau projet (props : `studentName: string`, `course: string`, `githubUrl: string`). Génère un `id` unique.

2\. `GET /projects` : Liste tous les projets.

3\. `GET /projects/:id` : Obtenir les détails d’un projet spécifique par son `id`.

4\. `PUT /projects/:id/grade` : Permettre à un "professeur" de noter un projet (prop : `grade: number`).

5\. `DELETE /projects/:id` : Supprimer un projet.

6\. `GET /projects/course/:courseName` : Filtrer et retourner tous les projets d’un cours spécifique.

7\. \*\*Métier \[À choisir]\*\* : Documentation du projet dans le \*\*Wiki GitHub\*\* (comment installer, lancer le serveur, et utiliser chaque endpoint avec des exemples).



---



\## 4. Déroulé du TP par Phases



\### \*\*Phase 1 : Initialisation \& Structure (Git Flow \& Hooks)\*\*



\*\*Objectif\*\* : Mettre en place un dépôt sain, structuré selon Git Flow, et sécurisé par des contrôles locaux.



1\. \*\*Lead (Maintainer)\*\* :

&nbsp;  - Initialise le projet localement (FastAPI).

&nbsp;  - Configure \*\*flake8/Black\*\*.

&nbsp;  - Implémente le `pre-commit`.

&nbsp;  - Crée le commit initial et le pousse sur `main`.



2\. \*\*Lead (GitHub)\*\* :

&nbsp;  - Crée la branche `develop`.

&nbsp;  - Active \*\*Branch Protection Rules\*\* sur `develop` :

&nbsp;    - 2 approbations

&nbsp;    - CI requise

&nbsp;    - Pas de bypass



3\. \*\*Tous\*\* :

&nbsp;  - Clone le dépôt

&nbsp;  - `pre-commit install`

&nbsp;  - \*\*Test\*\* : Commit mal formaté → \*\*bloqué\*\*



---



\### \*\*Phase 2 : Collaboration \& Flux de Fonctionnalités\*\*



1\. Chaque membre :

&nbsp;  - `git switch develop \&\& git pull`

&nbsp;  - `git switch -c feature/...`

&nbsp;  - Code → commit → push

2\. \*\*PR\*\* : `feature/\*` → `develop` (2 relectures + CI)

3\. \*\*Merge\*\* : Squash and merge

4\. \*\*Conflits\*\* : Résolus localement



---



\### \*\*Phase 3 : CI/CD, IA \& Release\*\*



1\. \*\*CI GitHub Actions\*\* : `black --check .`, `flake8 .`

2\. \*\*Revue IA + Email\*\* : Gemini API + envoi email

3\. \*\*Secrets\*\* : `GEMINI\_API\_KEY`, `MAIL\_USERNAME`, etc.

4\. \*\*Release\*\* : `v1.0.0` sur `main`



---



\## Sommaire du Wiki



1\. \[Structure du projet](Structure-du-projet)  

2\. \[Git Flow](Git-Flow)  

3\. \[Endpoints API](Endpoints-API)  

4\. \[CI/CD \& Qualité](CI-CD-Qualite)  

5\. \[Revue IA + Email](Revue-IA-Email)  

6\. \[Sécurité](Securite)  

7\. \[Tâches par membre](Taches-par-membre)



---



\*\*Auteur\*\* : Malachie237-git  

\*\*Date\*\* : 09/11/2025

