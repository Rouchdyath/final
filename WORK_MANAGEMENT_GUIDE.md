# Documentation: Système de Gestion des Travaux

## Vue d'ensemble

Le système de gestion des travaux permet aux formateurs de :
1. **Créer des travaux** individuels ou collectifs avec des consignes détaillées
2. **Assigner des travaux** à des étudiants spécifiques
3. **Consulter et suivre** l'état d'avancement des travaux assignés
4. **Mettre à jour les statuts** et ajouter des commentaires sur les assignations

## Architecture du Système

### Modèles de Données

#### 1. TravailIndividuel (Travail)
Représente un travail/assignment académique

**Champs:**
- `id`: Identifiant unique (BigAutoField)
- `titre`: Titre du travail (CharField, max 200)
- `description`: Description détaillée du travail (TextField)
- `type_travail`: Type du travail (CharField, choices: 'individuel' ou 'collectif')
- `consignes`: Consignes détaillées pour les étudiants (TextField)
- `date_echeance`: Date limite de remise (DateTimeField)
- `espace`: Référence à EspacePedagogique (ForeignKey)
- `date_creation`: Horodatage de création (DateTimeField, auto_now_add=True)

**Relations:**
- `assignations`: OneToMany avec AssignationTravail
- `livraisons`: OneToMany avec Livraison

#### 2. AssignationTravail (Nouveau modèle)
Représente l'assignation d'un travail à un étudiant

**Champs:**
- `id`: Identifiant unique (BigAutoField)
- `etudiant`: Référence à Etudiant (ForeignKey, required)
- `travail`: Référence à TravailIndividuel (ForeignKey, required)
- `date_assignation`: Date d'assignation (DateTimeField, auto_now_add=True)
- `statut`: État de l'assignation (CharField, choices):
  - `assigné`: Travail assigné, en attente de démarrage
  - `en_cours`: L'étudiant a commencé le travail
  - `complété`: L'étudiant a remis le travail
  - `évalué`: Le formateur a évalué le travail
- `notes`: Commentaires du formateur (TextField, nullable)

**Contraintes:**
- `unique_together`: (etudiant, travail) - Un travail ne peut être assigné qu'une fois par étudiant

#### 3. Livraison
Représente la soumission d'un travail par un étudiant

**Champs:**
- `id`: Identifiant unique
- `etudiant`: Référence à Etudiant (ForeignKey)
- `travail`: Référence à TravailIndividuel (ForeignKey)
- `contenu`: Contenu de la livraison (TextField)
- `fichier`: Fichier joint optionnel (FileField)
- `date_soumission`: Date/heure de soumission (DateTimeField, auto_now_add=True)

## Endpoints API

### Création de Travaux

#### POST `/api/travaux/creer/`
Créer un nouveau travail (individuel ou collectif)

**Request Body:**
```json
{
    "titre": "Projet Final Django",
    "description": "Créez une application web complète avec Django REST Framework",
    "type_travail": "individuel",
    "consignes": "Instructions détaillées du travail...",
    "date_echeance": "2024-12-31T23:59:59",
    "espace_id": 1
}
```

**Response Success (201):**
```json
{
    "success": true,
    "message": "Travail créé avec succès",
    "data": {
        "id": 5,
        "titre": "Projet Final Django",
        "description": "...",
        "type_travail": "individuel",
        "consignes": "...",
        "date_echeance": "2024-12-31T23:59:59",
        "espace": {...},
        "date_creation": "2024-01-15T10:30:00",
        "nombre_livraisons": 0,
        "nombre_assignations": 0
    }
}
```

### Assignation de Travaux

#### POST `/api/travaux/assigner/`
Assigner un travail à un étudiant

**Request Body:**
```json
{
    "travail_id": 5,
    "etudiant_id": 3,
    "notes": "Bonne chance! N'hésitez pas à poser des questions."
}
```

**Response Success (201):**
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

### Consultation des Travaux

#### GET `/api/etudiants/<etudiant_id>/travaux-assignes/`
Lister tous les travaux assignés à un étudiant

**Response:**
```json
{
    "success": true,
    "data": [
        {
            "id": 12,
            "etudiant": {...},
            "travail": {...},
            "date_assignation": "2024-01-15T10:35:00",
            "statut": "en_cours",
            "notes": "..."
        }
    ]
}
```

#### GET `/api/espaces/<espace_id>/travaux-assignes/`
Lister tous les travaux d'un espace avec leurs assignations

**Response:**
```json
{
    "success": true,
    "espace": {
        "id": 1,
        "nom": "Développement Web",
        "matiere": "Informatique"
    },
    "travaux": [
        {
            "id": 5,
            "titre": "Projet Final Django",
            "type_travail": "individuel",
            "assignations": [
                {
                    "id": 12,
                    "etudiant": {...},
                    "statut": "en_cours",
                    "date_assignation": "2024-01-15T10:35:00"
                }
            ]
        }
    ]
}
```

#### GET `/api/etudiants/<etudiant_id>/travaux-par-formateur/`
Consulter les travaux assignés à un étudiant (vue formateur)

**Response:**
```json
{
    "success": true,
    "etudiant": {
        "id": 3,
        "nom": "Dupont",
        "prenom": "Jean"
    },
    "travaux_assignes": [
        {
            "id": 12,
            "travail": {...},
            "statut": "en_cours",
            "date_assignation": "2024-01-15T10:35:00",
            "notes": null
        }
    ]
}
```

### Gestion des Statuts

#### PATCH `/api/assignations/<assignation_id>/mettre-a-jour/`
Mettre à jour le statut et les notes d'une assignation

**Request Body:**
```json
{
    "statut": "complété",
    "notes": "Travail reçu et en cours d'évaluation"
}
```

**Response Success (200):**
```json
{
    "success": true,
    "message": "Assignation mise à jour avec succès",
    "data": {
        "id": 12,
        "etudiant": {...},
        "travail": {...},
        "date_assignation": "2024-01-15T10:35:00",
        "statut": "complété",
        "notes": "Travail reçu et en cours d'évaluation"
    }
}
```

## Interfaces Utilisateur

### 1. creer-travail.html
Page de création d'un nouveau travail

**Fonctionnalités:**
- Formulaire avec champs: Titre, Description, Type, Consignes, Échéance
- Sélecteur d'espace pédagogique
- Validation côté client
- Confirmation de succès avec redirection

**URL:** `http://localhost:8000/frontend/creer-travail.html`

### 2. assigner-travail.html
Page d'assignation de travaux aux étudiants

**Fonctionnalités:**
- Sélecteur de travail avec affichage des détails
- Liste interactive des étudiants avec recherche
- Sélection multiple des étudiants (tags visuels)
- Champ de notes optionnel pour chaque assignation
- Assignation en masse à plusieurs étudiants

**URL:** `http://localhost:8000/frontend/assigner-travail.html`

### 3. consultation-formateur-travaux.html
Page de consultation et suivi des travaux par les formateurs

**Fonctionnalités:**
- Filtrage par espace pédagogique
- Filtrage par statut (Assigné, En cours, Complété, Évalué)
- Affichage des travaux avec listes d'assignations
- Vue en carte pour chaque étudiant
- Modal de mise à jour du statut
- Statistiques globales (totaux par statut)
- Actualisation en temps réel

**URL:** `http://localhost:8000/frontend/consultation-formateur-travaux.html`

## Flux d'Utilisation

### Scénario 1: Créer et Assigner un Travail

1. **Création du Travail**
   - Accéder à `creer-travail.html`
   - Remplir le formulaire avec les détails
   - Sélectionner le type (individuel ou collectif)
   - Entrer les consignes détaillées
   - Cliquer "Créer le Travail"

2. **Assignation du Travail**
   - Accéder à `assigner-travail.html`
   - Sélectionner le travail créé
   - Affichage automatique des détails du travail
   - Rechercher et sélectionner les étudiants
   - Ajouter des notes optionnelles
   - Cliquer "Assigner aux Étudiants Sélectionnés"

3. **Suivi du Travail**
   - Accéder à `consultation-formateur-travaux.html`
   - Filtrer par espace pédagogique
   - Voir toutes les assignations avec leurs statuts
   - Mettre à jour les statuts au fur et à mesure
   - Ajouter des commentaires de correction

### Scénario 2: Consulter les Travaux d'un Étudiant

1. Via l'API:
   ```
   GET /api/etudiants/3/travaux-assignes/
   ```

2. Via l'interface:
   - Utiliser `consultation-formateur-travaux.html`
   - Rechercher les travaux assignés à l'étudiant
   - Voir l'historique des assignations

## Migrations

### Migration 0005_assignationtravail_and_update_travail.py

Cette migration ajoute:
1. Champ `type_travail` à TravailIndividuel (CharField avec choices)
2. Champ `consignes` à TravailIndividuel (TextField)
3. Nouveau modèle `AssignationTravail` avec structure complète
4. Contrainte d'unicité (etudiant, travail)

**Application:**
```bash
python manage.py migrate
```

## Sérializers

### TravailIndividuelSerializer
- Inclut les nouveaux champs: `type_travail`, `consignes`
- Compte les assignations: `nombre_assignations`
- Validation d'existence de l'espace

### AssignationTravailSerializer
- Validation de l'unicité (etudiant, travail)
- Sérialisation complète de l'étudiant et du travail
- Gestion des statuts et notes

## Gestion des Erreurs

### Erreurs Courantes et Resolutions

1. **"Ce travail est déjà assigné à cet étudiant"**
   - Vérifier que l'étudiant n'a pas déjà ce travail
   - Solution: Utiliser la liste de consultation pour vérifier

2. **"Cet espace pédagogique n'existe pas"**
   - L'espace sélectionné n'existe pas
   - Rafraîchir la liste des espaces

3. **"Cet étudiant n'existe pas"**
   - L'ID de l'étudiant n'existe pas
   - Vérifier que l'étudiant est créé dans le système

## Notes de Sécurité et Bonnes Pratiques

1. **Validation des données:**
   - Tous les IDs sont validés avant utilisation
   - Les statuts sont limités à un ensemble défini

2. **Contraintes d'unicité:**
   - Un travail ne peut être assigné qu'une fois par étudiant
   - Évite les doublons accidentels

3. **Auditabilité:**
   - `date_assignation` enregistre quand le travail a été assigné
   - `notes` permet aux formateurs de laisser des traces
   - Les changements de statut sont tracés

## Performance et Optimisation

1. **Requêtes Optimisées:**
   - Les sérializers incluent les données en une requête
   - Utilisation de `select_related` et `prefetch_related` dans les views

2. **Pagination:**
   - À implémenter pour les listes volumineuses
   - Ajouter la pagination Django REST Framework si nécessaire

## Futures Améliorations

1. **Groupes de travail:**
   - Créer des groupes d'étudiants pour les travaux collectifs
   - Attribuer un travail collectif à tout un groupe

2. **Rôles d'évaluation:**
   - Notation des travaux
   - Historique des évaluations

3. **Notifications:**
   - Notifier les étudiants de l'assignation
   - Rappels d'échéance

4. **Uploads de fichiers:**
   - Support amélioré des fichiers
   - Stockage cloud optionnel

5. **Commentaires:**
   - Système de commentaires pour le feedback
   - Discussion étudiant-formateur
