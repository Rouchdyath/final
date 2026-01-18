# Guide Rapide: Système de Gestion des Travaux

## 🎯 Cas d'Usage

### Pour un Formateur

#### Tâche 1: Créer un Travail
1. Ouvrir: `http://localhost:8000/frontend/creer-travail.html`
2. Remplir:
   - Titre du travail
   - Description
   - Type (Individuel ou Collectif)
   - Consignes détaillées
   - Date d'échéance
   - Sélectionner l'espace pédagogique
3. Cliquer: "Créer le Travail"

#### Tâche 2: Assigner le Travail aux Étudiants
1. Ouvrir: `http://localhost:8000/frontend/assigner-travail.html`
2. Sélectionner le travail créé
3. Chercher et sélectionner les étudiants (clic sur les cartes)
4. Ajouter des notes si nécessaire
5. Cliquer: "Assigner aux Étudiants Sélectionnés"

#### Tâche 3: Consulter et Suivre
1. Ouvrir: `http://localhost:8000/frontend/consultation-formateur-travaux.html`
2. Filtrer par:
   - Espace pédagogique
   - Statut de l'assignation
3. Cliquer sur un travail pour voir les assignations
4. Cliquer "Mettre à jour" pour:
   - Changer le statut
   - Ajouter des commentaires

---

## 📡 Endpoints API (Utilisation Avancée)

### Créer un Travail
```bash
curl -X POST http://localhost:8000/api/travaux/creer/ \
  -H "Content-Type: application/json" \
  -d '{
    "titre": "Projet Django",
    "description": "Créer une API REST",
    "type_travail": "individuel",
    "consignes": "Instructions détaillées...",
    "date_echeance": "2024-12-31T23:59:59",
    "espace_id": 1
  }'
```

### Assigner un Travail
```bash
curl -X POST http://localhost:8000/api/travaux/assigner/ \
  -H "Content-Type: application/json" \
  -d '{
    "travail_id": 5,
    "etudiant_id": 3,
    "notes": "Notes optionnelles"
  }'
```

### Voir les Travaux Assignés à un Étudiant
```bash
curl http://localhost:8000/api/etudiants/3/travaux-assignes/
```

### Voir les Travaux d'un Espace
```bash
curl http://localhost:8000/api/espaces/1/travaux-assignes/
```

### Mettre à Jour une Assignation
```bash
curl -X PATCH http://localhost:8000/api/assignations/12/mettre-a-jour/ \
  -H "Content-Type: application/json" \
  -d '{
    "statut": "complété",
    "notes": "Travail reçu"
  }'
```

---

## 📊 Statuts des Assignations

| Statut | Signification | Quand? |
|--------|---------------|--------|
| **assigné** | Travail vient d'être assigné | Lors de l'assignation |
| **en_cours** | L'étudiant a commencé | Après que l'étudiant démarre |
| **complété** | L'étudiant a remis | Après la soumission |
| **évalué** | Le formateur a évalué | Après correction |

---

## 🔍 Recherche et Filtrage

### Dans creer-travail.html
- ✅ Sélection d'espace automatique
- ✅ Tous les champs sont validés

### Dans assigner-travail.html
- 🔍 Recherche d'étudiants par:
  - Nom
  - Prénom
  - Email
- ✓ Sélection multiple avec affichage des tags

### Dans consultation-formateur-travaux.html
- 🏢 Filtrer par espace pédagogique
- 📊 Filtrer par statut
- 🔄 Actualiser les données
- 📈 Voir les statistiques (totaux)

---

## ⚠️ Validation et Erreurs

### Erreurs Communes

| Erreur | Cause | Solution |
|--------|-------|----------|
| "Ce travail est déjà assigné" | Étudiant a déjà ce travail | Choisir un autre étudiant |
| "Espace n'existe pas" | ID incorrect | Vérifier la liste des espaces |
| "Étudiant n'existe pas" | ID incorrect | Créer l'étudiant d'abord |
| "Statut invalide" | Statut non reconnu | Utiliser: assigné, en_cours, complété, évalué |

---

## 💡 Bonnes Pratiques

### Gestion des Travaux
1. ✅ Toujours créer le travail d'abord
2. ✅ Assigner ensuite aux étudiants
3. ✅ Consulter régulièrement la progression
4. ✅ Mettre à jour les statuts au fur et à mesure

### Organisation
1. 📝 Donner des titres et descriptions clairs
2. 📋 Écrire des consignes détaillées
3. 🎯 Fixer des dates d'échéance réalistes
4. 💬 Ajouter des commentaires utiles aux assignations

### Suivi
1. 🔄 Actualiser régulièrement la consultation
2. 📊 Utiliser les filtres pour voir les retards
3. ✏️ Documenter les problèmes dans les notes

---

## 🚀 Scénarios Complets

### Scénario 1: TP de Fin de Semaine
```
1. Lundi matin:
   - Créer travail "TP JavaScript"
   - Type: Individuel
   - Échéance: Vendredi 18h
   - Assigner à tous les étudiants

2. Vendredi:
   - Vérifier consultation
   - Mettre à jour: quelques "en_cours", autres "complété"

3. Lundi suivant:
   - Tous les statuts → "évalué"
   - Ajouter notes de correction
```

### Scénario 2: Projet Collectif
```
1. Créer travail "Projet Web Final"
   - Type: Collectif
   - Échéance: 1 mois
   - Consignes très détaillées

2. Créer groupes d'étudiants (manuel ou automatique)
3. Assigner un travail par groupe
   - Méthodologie: Assigner à UN représentant du groupe
   - OU: Assigner à chaque membre séparément

4. Suivi:
   - Voir progression des groupes
   - Un seul statut par groupe (tous pareil)
```

### Scénario 3: Travail Supplémentaire
```
1. Créer "Devoir Supplémentaire"
   - Type: Individuel
   - Pour étudiants en rattrapage

2. Assigner uniquement à ceux qui ont besoin

3. Mettre à jour les statuts individuellement
```

---

## 📱 Interface Mobile

### Consultation Mobile
- ✅ Les pages sont responsive
- ✅ Fonctionnent sur tablettes et téléphones
- ✅ Tous les filtres disponibles
- ✅ Tous les boutons tactiles

### Limitations
- ❌ Upload de fichiers difficile (utiliser un ordinateur)
- ⚠️ Écrans petits: peut faut dérouler

---

## 🔗 Lien Rapide

| Page | URL |
|------|-----|
| Créer Travail | `http://localhost:8000/frontend/creer-travail.html` |
| Assigner Travail | `http://localhost:8000/frontend/assigner-travail.html` |
| Consulter Travaux | `http://localhost:8000/frontend/consultation-formateur-travaux.html` |
| API - Espaces | `http://localhost:8000/api/espaces/` |
| API - Travaux | `http://localhost:8000/api/travaux/` |
| Admin Django | `http://localhost:8000/admin/` |

---

## 🆘 Besoin d'Aide?

### Vérifier que le Serveur Tourne
```bash
# Terminal
python manage.py runserver
# Devrait afficher: Starting development server at http://127.0.0.1:8000/
```

### Vérifier les Données
```bash
# Aller à l'admin Django
http://localhost:8000/admin/
# Username: admin
# Password: (celui que vous avez défini)
```

### Voir les Logs d'Erreur
```bash
# Les erreurs API s'affichent:
1. Console du navigateur (F12)
2. Terminal du serveur Django
3. Les alertes rouges sur la page
```

---

## 📚 Documentation Complète

Pour plus de détails techniques, voir:
- `WORK_MANAGEMENT_GUIDE.md` - Guide complet
- `IMPLEMENTATION_WORK_SYSTEM.md` - Détails techniques
