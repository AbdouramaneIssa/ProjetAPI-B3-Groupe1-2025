# 🚀 ProjetAPI – Gestion des Projets Étudiants (B3 Groupe 1 – 2025)

Bienvenue dans **ProjetAPI**, une application **FastAPI** développée par le Groupe 1 – B3 2025.
Ce projet illustre une approche complète de **DevOps**, intégrant :
- un **pipeline CI/CD GitHub Actions**,
- une **revue de code automatisée par IA (Gemini)**,
- un **système pre-commit** pour garantir la qualité du code,
- et une **release versionnée** propre.

---

## 🧭 Sommaire

1. [🧩 Installation & Lancement](#-installation--lancement)
2. [🤖 CI/CD & Automatisation](#-cicd--automatisation)
3. [🧹 Pre-commit & Qualité du Code](#-pre-commit--qualité-du-code)
4. [🏷️ Release & Tagging](#️-release--tagging)
5. [🐞 Problèmes rencontrés & Solutions](#-problèmes-rencontrés--solutions)

---

## 🧩 Installation & Lancement

Cette section décrit comment installer et exécuter le projet **ProjetAPI** en local.

### 🧰 Prérequis

Avant de commencer, assurez-vous d’avoir :
- **Python 3.10+**
- **pip** installé
- **Git**
- Un éditeur (VS Code recommandé)

### 📦 Installation

```bash
# Cloner le projet
git clone https://github.com/AbdouramaneIssa/ProjetAPI-B3-Groupe1-2025.git
cd ProjetAPI-B3-Groupe1-2025
```

#### 🧱 Créer et activer l’environnement virtuel

**Windows PowerShell :**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**macOS / Linux :**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 📚 Installer les dépendances
```bash
pip install -r requirements.txt
```

#### 🚀 Lancer le serveur FastAPI
```bash
uvicorn main:app --reload
```

### 🌐 Accès à l’application

| Interface | URL |
| :--- | :--- |
| 💻 Interface Web (Bootstrap) | `http://127.0.0.1:8000/` |
| 📘 Swagger (Documentation API) | `http://127.0.0.1:8000/docs` |

---

## 🤖 CI/CD & Automatisation

Le projet intègre un pipeline complet CI/CD GitHub Actions pour automatiser les contrôles qualité et les revues IA.

### 🧩 Objectif du pipeline

- Vérifier le linting et le typage (qualité du code)
- Bloquer les PR contenant des erreurs
- Automatiser la revue IA avec Gemini
- Envoyer des e-mails à l’équipe

### 🧪 Workflow 1 : CI de Base (`.github/workflows/ci.yml`)

**🔹 Déclencheur :**
Sur chaque Pull Request vers `develop`.

**🔹 Étapes :**
1. Setup – installe Python
2. Linting – `flake8 --max-line-length=100`
3. Type-check – `mypy . --ignore-missing-imports`
4. Tests unitaires (optionnel)

**🧠 Objectif :**
Empêcher le merge d’une PR contenant des erreurs. Une CI rouge 🔴 bloque le merge.

### 🤖 Workflow 2 : Revue IA & Notification (`.github/workflows/llm-review.yml`)

**🔹 Déclencheur :**
Sur chaque Pull Request (`opened` ou `synchronize`) vers `develop`.

**🔹 Étapes :**
1. Récupère le diff du code
2. Envoie le diff à Gemini API
3. Commente automatiquement la PR sur GitHub
4. Envoie un e-mail de résumé à l’équipe

**🔹 Secrets requis :**

| Secret | Description |
| :--- | :--- |
| `GEMINI_API_KEY` | Clé API Gemini |
| `MAIL_USERNAME` | Adresse mail d’envoi |
| `MAIL_PASSWORD` | Mot de passe d’application |
| `TEAM_EMAIL_LIST` | Liste des mails des membres séparés par des virgules |

### 🔒 Règles de protection des branches

| Branche | Règles |
| :--- | :--- |
| `develop` | 🔹 2 approbations obligatoires<br>🔹 Tous les checks CI/CD doivent passer |
| `main` | 🔹 Merge autorisé uniquement depuis `develop` |

### ✅ Résultat attendu

Pipeline complet et automatisé :
`✅ CI passe` → `✅ Revue IA` → `✅ Merge autorisé`
Processus déclenché automatiquement à chaque PR.

---

## 🧹 Pre-commit & Qualité du Code

Les hooks `pre-commit` garantissent la qualité du code avant chaque commit.

### ⚙️ Installation et activation :
```bash
pip install pre-commit
pre-commit install
```

### 🧪 Vérifier manuellement tout le projet :
```bash
pre-commit run --all-files
```

### 🔍 Hooks utilisés :

| Hook | Description |
| :--- | :--- |
| `flake8` | Vérifie la qualité et le style du code |
| `mypy` | Vérifie les types |
| `trailing-whitespace` | Supprime les espaces inutiles |
| `end-of-file-fixer` | Corrige la fin de fichier |

---

## 🏷️ Release & Tagging

Une release correspond à une version stable du projet.

### 🚀 Étapes finales :

1. Merger toutes les features vers `develop`
2. Créer une PR de `develop` → `main`
3. Une fois mergé :

```bash
git checkout main
git pull origin main
git tag v1.0.0
git push origin v1.0.0
```
4. Créer la Release GitHub basée sur ce tag (avec les notes de version)

### 🗑️ Supprimer un tag (si erreur) :
```bash
git tag -d v1.0.0
git push origin :refs/tags/v1.0.0
```

---

## 🐞 Problèmes rencontrés & Solutions

### ⚠️ 1️⃣ Erreurs de typage ou linting

**Problème :**
```sql
All conditional function variants must have identical signatures
```
**Solution :**
Uniformiser les signatures dans `main.py`, relancer :
```bash
flake8
mypy .
```

### ⚠️ 2️⃣ Erreur Gemini (API IA)

**Problème :**
```rust
unexpected EOF while looking for matching ')'
```
**Cause :**
Erreur de syntaxe YAML (EOF mal fermé).

**Solution :**
Corriger l’indentation et tester sur une PR.

### ⚠️ 3️⃣ Absence de status checks

**Problème :**
`“No required checks found when protecting develop”`

**Solution :**
1. Lancer une PR vers `develop`
2. Attendre la fin des workflows
3. Revenir dans les Branch Protection Rules et activer les checks CI/CD

### ⚠️ 4️⃣ Email non envoyé

**Problème :**
`Authentication failed`

**Solution :**
Créer un mot de passe d’application Gmail et le placer dans les Secrets.

### ⚠️ 5️⃣ Hook pre-commit inactif

**Solution :**
Réinstaller :
```bash
pip install pre-commit
pre-commit install
```

---

## 👥 Équipe du Projet

| Membre | Rôle |
| :--- | :--- |
| Abdouramane ISSA | 👑 Lead / DevOps |
| Mouhamed Bachirou | Backend |
| Alain Gérémy | Backend |
| Malachie | Backend |
| Kelly Tassa | Frontend |
| Booz | Backend |
| Elie Junior | QA & Tests |



## 🔗 Accéder au Wiki du Projet

Pour une documentation plus détaillée, des tutoriels et des informations supplémentaires, veuillez consulter notre Wiki :

[**📚 Consulter le Wiki du Projet**](https://github.com/AbdouramaneIssa/ProjetAPI-B3-Groupe1-2025/wiki)
