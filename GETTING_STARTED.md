# Guide de démarrage - Après implémentation

## Démarrage du serveur Django

```bash
cd backend
python manage.py runserver
```

Le serveur démarrera sur http://localhost:8000

## Accès aux pages Frontend

- **Créer une promotion**: http://localhost:8000/frontend/creer-promotion.html
- **Liste des promotions**: http://localhost:8000/frontend/liste-promotions.html
- **Créer un étudiant (avec promotion)**: http://localhost:8000/frontend/creer-etudiant.html

## Tester l'API avec curl ou Postman

### 1. Créer une promotion
```bash
curl -X POST http://localhost:8000/api/promotions/creer/ \
  -H "Content-Type: application/json" \
  -d '{
    "nom": "L3 Informatique",
    "annee": 2024,
    "description": "Promotion de troisième année"
  }'
```

### 2. Lister les promotions
```bash
curl http://localhost:8000/api/promotions/
```

### 3. Créer un étudiant avec une promotion
```bash
curl -X POST http://localhost:8000/api/etudiants/creer/ \
  -H "Content-Type: application/json" \
  -d '{
    "nom": "Dupont",
    "prenom": "Alice",
    "email": "alice.dupont@example.com",
    "promotion_id": 1
  }'
```

### 4. Ajouter un espace à une promotion
```bash
curl -X POST http://localhost:8000/api/promotions/1/ajouter-espace/ \
  -H "Content-Type: application/json" \
  -d '{"espace_id": 1}'
```

## Structure des données

### Promotion
```json
{
  "id": 1,
  "nom": "L3 Informatique",
  "annee": 2024,
  "description": "Description de la promotion",
  "date_creation": "2026-01-17T10:30:00Z",
  "nombre_etudiants": 45,
  "nombre_espaces": 3
}
```

### Étudiant (avec promotion)
```json
{
  "id": 1,
  "nom": "Dupont",
  "prenom": "Alice",
  "email": "alice.dupont@example.com",
  "telephone": "+33 6 12 34 56 78",
  "promotion": {
    "id": 1,
    "nom": "L3 Informatique",
    "annee": 2024,
    ...
  },
  "date_creation": "2026-01-17T10:30:00Z",
  "espaces": []
}
```

## Prochaines étapes (suggestions)

1. **Ajouter l'authentification**: Protéger les endpoints API avec token/session
2. **Statistiques**: Créer un dashboard pour voir les statistiques par promotion
3. **Export de données**: Permettre l'export en CSV/Excel
4. **Gestion des absences**: Tracker les absences par étudiant et promotion
5. **Notes et évaluations**: Système de notation intégré

## Architecture

```
projet_SIL3/
├── backend/
│   ├── espaces_pedagogiques/
│   │   ├── models.py (Promotion, Etudiant, ...)
│   │   ├── views.py (API endpoints)
│   │   ├── serializers.py (Data serialization)
│   │   ├── urls.py (Routes)
│   │   └── migrations/ (0004_promotion.py)
│   ├── manage.py
│   └── backend/
│       ├── settings.py
│       └── urls.py
└── frontend/
    ├── creer-promotion.html (NOUVEAU)
    ├── liste-promotions.html (NOUVEAU)
    ├── creer-etudiant.html (MODIFIÉ)
    └── ... autres pages
```

## Notes importantes

- Les promotions sont identifiées de manière unique par la combinaison (nom, annee)
- Les étudiants peuvent être optionnellement liés à une promotion
- Un étudiant peut être inscrit à plusieurs espaces pédagogiques
- Une promotion peut contenir plusieurs espaces pédagogiques
