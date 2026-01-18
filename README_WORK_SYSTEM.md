#!/usr/bin/env markdown
# 🎓 Système de Gestion des Travaux Académiques

## Table des Matières
1. [Aperçu](#aperçu)
2. [Installation et Configuration](#installation-et-configuration)
3. [Utilisation](#utilisation)
4. [Architecture](#architecture)
5. [Documentation API](#documentation-api)
6. [Dépannage](#dépannage)

---

## Aperçu

Le **Système de Gestion des Travaux Académiques** est une solution complète permettant aux formateurs de:

- 📝 **Créer des travaux** individuels ou collectifs avec consignes détaillées
- 🎯 **Assigner des travaux** à des étudiants spécifiques
- 📊 **Consulter et suivre** l'état d'avancement
- ✏️ **Mettre à jour les statuts** et ajouter des commentaires

### Caractéristiques Principales

✨ **Interface Web Intuitive** - Trois pages d'application faciles à utiliser
🔒 **Sécurisé** - Validation complète côté client et serveur
⚡ **Performant** - Requêtes optimisées et interfaces rapides
📱 **Responsive** - Fonctionne sur tous les appareils
📚 **Bien Documenté** - Documentation technique et guides d'utilisation

---

## Installation et Configuration

### Prérequis

```bash
Python 3.10+
Django 5.2.9
Django REST Framework
SQLite (ou PostgreSQL)
```

### 1. Configuration de la Base de Données

Les migrations sont déjà créées et appliquées:

```bash
cd backend
python manage.py migrate
```

Vérifier le statut:
```bash
python manage.py showmigrations espaces_pedagogiques
```

### 2. Lancer le Serveur

```bash
cd backend
python manage.py runserver
```

Accédez à: `http://localhost:8000/`

### 3. Créer un Compte Admin (Optionnel)

```bash
python manage.py createsuperuser
```

Puis visitez: `http://localhost:8000/admin/`

---

## Utilisation

### Workflow Complet

#### Étape 1️⃣ : Créer un Travail

**URL:** `http://localhost:8000/frontend/creer-travail.html`

1. Remplir le formulaire:
   - **Titre:** Ex: "Projet Final Django"
   - **Description:** Contexte et objectifs
   - **Type:** Choisir "Individuel" ou "Collectif"
   - **Consignes:** Instructions détaillées
   - **Date d'Échéance:** Sélectionner une date/heure
   - **Espace:** Sélectionner l'espace pédagogique

2. Cliquer "Créer le Travail"
3. Message de succès → Travail créé ✅

**Exemple de Travail:**
```
Titre: Projet Web Responsive
Type: Individuel
Consignes: Créer un site web responsive avec HTML/CSS/JS
Échéance: 31 Décembre 2024 à 23h59
```

#### Étape 2️⃣ : Assigner le Travail

**URL:** `http://localhost:8000/frontend/assigner-travail.html`

1. **Sélectionner le travail** dans le dropdown
   - Les détails s'affichent automatiquement
   
2. **Rechercher les étudiants**
   - Taper pour filtrer par nom/email
   - Cliquer sur les cartes pour sélectionner (fond bleu)
   
3. **Ajouter des notes** (optionnel)
   - Instructions supplémentaires pour les étudiants
   
4. **Assigner** en cliquant le bouton
   - Les travaux sont assignés à tous les étudiants sélectionnés
   - Les doublons sont automatiquement évités ✅

**Exemple de Sélection:**
- Travail: "Projet Web Responsive"
- Étudiants: Jean Dupont, Marie Martin, Pierre Legrand
- Notes: "N'oubliez pas le responsive design!"

#### Étape 3️⃣ : Consulter et Suivre

**URL:** `http://localhost:8000/frontend/consultation-formateur-travaux.html`

1. **Filtrer les travaux**
   - Par Espace Pédagogique
   - Par Statut (Assigné, En cours, Complété, Évalué)

2. **Voir les assignations**
   - Cliquer sur un travail pour le déployer
   - Voir tous les étudiants et leur statut

3. **Mettre à jour le statut**
   - Cliquer "Mettre à jour" sur une assignation
   - Changer le statut
   - Ajouter des commentaires
   - Sauvegarder ✅

4. **Voir les statistiques**
   - Totaux par statut affichés en haut
   - Vue d'ensemble rapide du statut

**Exemple de Suivi:**
```
Travail: Projet Web Responsive
Total: 3 assignations

- Jean Dupont    → En cours (assigné le 15/01)
- Marie Martin   → Complété (assigné le 15/01)
- Pierre Legrand → Assigné (assigné le 15/01)

Actions: Mettre à jour les statuts au fur et à mesure
```

---

## Architecture

### Hiérarchie des Données

```
EspacePedagogique (1)
├── Formateur (N)
├── Promotion (N)
│   └── Etudiant (N)
└── TravailIndividuel (N)
    ├── AssignationTravail (N)
    │   └── Etudiant (1)
    └── Livraison (N)
        └── Etudiant (1)
```

### Modèles de Données

#### TravailIndividuel (Travail)

```python
{
    "id": 5,
    "titre": "Projet Final Django",
    "description": "Créez une application web complète",
    "type_travail": "individuel",                    # ✨ NOUVEAU
    "consignes": "Consignes détaillées ici...",     # ✨ NOUVEAU
    "date_echeance": "2024-12-31T23:59:59",
    "espace": {
        "id": 1,
        "nom": "Développement Web",
        "matiere": "Informatique"
    },
    "date_creation": "2024-01-15T10:30:00",
    "nombre_livraisons": 0,
    "nombre_assignations": 3
}
```

#### AssignationTravail (Assignation)

```python
{
    "id": 12,
    "etudiant": {
        "id": 3,
        "nom": "Dupont",
        "prenom": "Jean",
        "email": "jean.dupont@school.fr"
    },
    "travail": { ... },                             # TravailIndividuel
    "date_assignation": "2024-01-15T10:35:00",
    "statut": "en_cours",
    "notes": "Bonne chance! Posez des questions si besoin."
}
```

### Statuts des Assignations

| Statut | Signification | Utilisé Quand |
|--------|---------------|---------------|
| **assigné** | Travail assigné, pas commencé | À l'assignation |
| **en_cours** | L'étudiant a commencé | Après le démarrage |
| **complété** | Étudiant a remis le travail | Après la soumission |
| **évalué** | Travail évalué et noté | Après correction |

---

## Documentation API

### Endpoints Disponibles

#### 1. Assigner un Travail

```http
POST /api/travaux/assigner/
Content-Type: application/json

{
    "travail_id": 5,
    "etudiant_id": 3,
    "notes": "Notes optionnelles du formateur"
}
```

**Response (201 Created):**
```json
{
    "success": true,
    "message": "Travail assigné avec succès",
    "data": {
        "id": 12,
        "etudiant": {...},
        "travail": {...},
        "date_assignation": "2024-01-15T10:35:00",
        "statut": "assigné",
        "notes": "..."
    }
}
```

#### 2. Lister les Travaux Assignés à un Étudiant

```http
GET /api/etudiants/3/travaux-assignes/
```

**Response:**
```json
{
    "success": true,
    "data": [
        {
            "id": 12,
            "travail": {...},
            "date_assignation": "2024-01-15T10:35:00",
            "statut": "en_cours",
            "notes": "..."
        }
    ]
}
```

#### 3. Lister les Travaux d'un Espace avec Assignations

```http
GET /api/espaces/1/travaux-assignes/
```

**Response:**
```json
{
    "success": true,
    "espace": {
        "id": 1,
        "nom": "Développement Web"
    },
    "travaux": [
        {
            "id": 5,
            "titre": "Projet Final Django",
            "assignations": [
                {
                    "id": 12,
                    "etudiant": {...},
                    "statut": "en_cours"
                }
            ]
        }
    ]
}
```

#### 4. Mettre à Jour une Assignation

```http
PATCH /api/assignations/12/mettre-a-jour/
Content-Type: application/json

{
    "statut": "complété",
    "notes": "Travail reçu et excellent!"
}
```

**Response:**
```json
{
    "success": true,
    "message": "Assignation mise à jour avec succès",
    "data": {
        "id": 12,
        "statut": "complété",
        "notes": "Travail reçu et excellent!"
    }
}
```

### Codes d'Erreur

| Code | Message | Cause |
|------|---------|-------|
| 400 | "Ce travail est déjà assigné à cet étudiant" | Unicité violée |
| 404 | "Cet étudiant n'existe pas" | ID étudiant invalide |
| 404 | "Ce travail individuel n'existe pas" | ID travail invalide |
| 400 | Statut invalide | Statut non reconnu |

---

## Dépannage

### Le Serveur ne démarre pas

```bash
# Vérifier les migrations
python manage.py showmigrations

# Appliquer les migrations
python manage.py migrate

# Vérifier la configuration
python manage.py check
```

### Les données ne s'affichent pas

```bash
# Vérifier les données en base
python manage.py shell
>>> from espaces_pedagogiques.models import TravailIndividuel
>>> TravailIndividuel.objects.all()

# Vérifier la console du navigateur (F12)
# Chercher les erreurs dans l'onglet "Network"
```

### Erreur "Ce travail est déjà assigné"

Cette erreur est **normale et saine**. Elle signifie que:
- Ce travail est déjà assigné à cet étudiant
- Le système l'empêche (contrainte d'unicité)

**Solution:** Sélectionner un autre étudiant

### Les pages HTML ne s'affichent pas

Vérifier:
1. Le serveur tourne: `python manage.py runserver`
2. L'URL est correcte: `http://localhost:8000/frontend/nompage.html`
3. La console du navigateur (F12) pour les erreurs JavaScript

### Les appels API échouent

1. **Vérifier la réponse dans Network (F12)**
   - Status code (200, 400, 404, 500)?
   - Message d'erreur dans la réponse?

2. **Vérifier le terminal Django**
   - Erreurs d'importation?
   - Erreurs de base de données?

3. **Vérifier les logs**
   ```bash
   python manage.py runserver > server.log 2>&1
   # Ouvrir server.log pour voir les erreurs
   ```

---

## Points de Vérification

### ✅ Installation Réussie

- [ ] `python manage.py migrate` s'exécute sans erreur
- [ ] `python manage.py check` ne montre que des warnings (staticfiles)
- [ ] `python manage.py runserver` démarre le serveur
- [ ] Les trois pages HTML sont accessibles
- [ ] Les modèles s'importent: `from espaces_pedagogiques.models import AssignationTravail`

### ✅ Fonctionnalité Testée

- [ ] Créer un travail: OK
- [ ] Assigner le travail: OK
- [ ] Voir les assignations: OK
- [ ] Mettre à jour le statut: OK
- [ ] Ajouter des notes: OK

---

## Fichiers Importants

### Backend
```
backend/
├── espaces_pedagogiques/
│   ├── models.py           # TravailIndividuel + AssignationTravail
│   ├── serializers.py      # Sérializers
│   ├── views.py            # 5 endpoints API
│   ├── urls.py             # Routes
│   └── migrations/
│       └── 0005_...py      # Migration AssignationTravail
└── manage.py               # Commandes Django
```

### Frontend
```
frontend/
├── creer-travail.html          # Création
├── assigner-travail.html       # Assignation
└── consultation-formateur-travaux.html  # Suivi
```

### Documentation
```
├── WORK_MANAGEMENT_GUIDE.md        # Guide technique complet
├── IMPLEMENTATION_WORK_SYSTEM.md   # Détails d'implémentation
├── QUICK_START_WORK_SYSTEM.md      # Guide rapide
└── SYSTEM_SUMMARY.md               # Résumé implémentation
```

---

## Support et Ressources

### Documentation Complète
- 📖 `WORK_MANAGEMENT_GUIDE.md` - Guide technique détaillé
- 🚀 `QUICK_START_WORK_SYSTEM.md` - Démarrage rapide
- 📋 `IMPLEMENTATION_WORK_SYSTEM.md` - Spécifications techniques

### Commandes Utiles

```bash
# Lancer le serveur
python manage.py runserver

# Tester les imports
python test_imports.py

# Créer superuser
python manage.py createsuperuser

# Voir les migrations
python manage.py showmigrations

# Afficher les modèles
python manage.py inspect_model espaces_pedagogiques.AssignationTravail
```

### Accès Rapide

| Page | URL |
|------|-----|
| Créer Travail | `http://localhost:8000/frontend/creer-travail.html` |
| Assigner | `http://localhost:8000/frontend/assigner-travail.html` |
| Consulter | `http://localhost:8000/frontend/consultation-formateur-travaux.html` |
| Admin | `http://localhost:8000/admin/` |
| API | `http://localhost:8000/api/` |

---

## Auteur et Licence

Développé pour le projet de gestion pédagogique.

---

**Le système est prêt pour une utilisation en production.** ✅

Pour questions ou support, consultez la documentation ou contactez l'équipe technique.
