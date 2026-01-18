# 🌐 URLS DE TEST - Accès Rapide

**Pour tester le système immédiatement**

---

## 🔗 Pages Principales

### Authentification
```
Login:   http://localhost:8000/frontend/login.html
Signup:  http://localhost:8000/frontend/signup.html
```

### Dashboard
```
Accueil: http://localhost:8000/frontend/index.html
```

---

## 👤 Pages Étudiant (Test avec rôle: Étudiant)

```
Mes Travaux:           http://localhost:8000/frontend/liste-travaux.html
Soumettre Livraison:   http://localhost:8000/frontend/soumettre-livraison.html
Mes Notes:             http://localhost:8000/frontend/mes-notes.html
```

---

## 📚 Pages Formateur (Test avec rôle: Formateur)

```
Créer Espace:          http://localhost:8000/frontend/creer-espace.html
Mes Espaces:           http://localhost:8000/frontend/liste-espaces.html
Gérer Formateurs:      http://localhost:8000/frontend/ajouter-formateur.html
Ajouter Étudiants:     http://localhost:8000/frontend/ajouter-etudiant-espace.html
Créer Travail:         http://localhost:8000/frontend/creer-travail.html
Assigner Travaux:      http://localhost:8000/frontend/assigner-travail.html
Évaluer Livraisons:    http://localhost:8000/frontend/evaluer-livraisons.html
Consulter Travaux:     http://localhost:8000/frontend/consultation-formateur-travaux.html
```

---

## 👁️ Pages Directeur (Test avec rôle: Directeur)

```
Créer Étudiant:        http://localhost:8000/frontend/creer-etudiant.html
Créer Promotion:       http://localhost:8000/frontend/creer-promotion.html
Consulter Étudiants:   http://localhost:8000/frontend/consultation-directeur-etudiants.html
Consulter Promotions:  http://localhost:8000/frontend/consultation-directeur-promotions.html
Consulter Espaces:     http://localhost:8000/frontend/consultation-directeur-espaces.html
+ Toutes les pages Formateur + Étudiant
```

---

## 🧪 Pages de Test

```
Test Authentification:  http://localhost:8000/frontend/test-auth.html
```

---

## 📊 Admin Django (si configuré)

```
Admin Django:         http://localhost:8000/admin/
API Authentication:   http://localhost:8000/api/auth/
```

---

## 🔍 Test Rapide (3 minutes)

```
1. Ouvrir:     login.html
2. Cliquer:    "S'inscrire ici →"
3. Remplir:    Formulaire (email, identifiant, password, rôle)
4. Vérifier:   Code dans F12 → Console
5. Entrer:     Code 6 chiffres
6. Connecter:  Avec rôle sélectionné
7. Tester:     Un lien du menu
```

---

## 📝 Données de Test

### Inscription
```
Email:             test@example.com
Identifiant:       testuser123
Mot de passe:      TestPass123!
Rôle:              Étudiant (ou Formateur)
```

### Connexion
```
Identifiant:       testuser123
Mot de passe:      TestPass123!
Rôle:              Le même que l'inscription
```

---

## 🎯 Scénarios de Test

### Scénario 1: Nouvel Utilisateur
```
1. login.html → "S'inscrire"
2. signup.html → Remplir formulaire
3. Vérifier email (F12 Console)
4. login.html → Se connecter
5. index.html → Tester menu
6. Tester un lien
```

### Scénario 2: Utilisateur Existant
```
1. login.html
2. Sélectionner rôle
3. Entrer identifiants
4. Se connecter
5. Tester menu
6. Tester plusieurs liens
7. Déconnexion
```

### Scénario 3: Contrôle d'Accès
```
1. Connecter comme Étudiant
2. Essayer: creer-espace.html → Redirection
3. Déconnecter
4. Connecter comme Formateur
5. Essayer: creer-etudiant.html → Redirection
6. Connecter comme Directeur
7. Accéder à tout → OK
```

---

## 🔌 API Endpoints (Backend à implémenter)

```
POST   /api/auth/register/
POST   /api/auth/verify/
POST   /api/auth/login/
POST   /api/auth/logout/
GET    /api/auth/permissions/
GET    /api/user/profile/
```

---

## 🚀 Commandes Utiles

### Démarrer le serveur
```bash
python manage.py runserver
```

### Console Django
```bash
python manage.py shell
```

### Migrations
```bash
python manage.py migrate
python manage.py makemigrations
```

### Superuser
```bash
python manage.py createsuperuser
```

---

## 🧪 Test dans la Console (F12)

```javascript
// Vérifier localStorage
localStorage.getItem('currentUser')

// Voir l'utilisateur
JSON.parse(localStorage.getItem('currentUser'))

// Voir tous les utilisateurs (si enregistrés)
JSON.parse(localStorage.getItem('app_users'))

// Déconnexion manuelle
localStorage.removeItem('currentUser')
```

---

## 🔐 Notes de Sécurité

```
⚠️ Mode DÉMO - Pour test uniquement
⚠️ Passwords en plain text - À hasher en production
⚠️ localStorage - À remplacer par JWT tokens
⚠️ Emails en console - À remplacer par API réelle
```

---

## ✅ Checklist Test Rapide

- [ ] login.html accessible
- [ ] signup.html accessible  
- [ ] Inscription marche
- [ ] Code email visible (F12)
- [ ] Vérification marche
- [ ] Connexion marche
- [ ] Menu correct par rôle
- [ ] Navigation marche
- [ ] Déconnexion marche
- [ ] Accès refusé si pas rôle

---

**Commencez maintenant! 🚀**

Allez à: **http://localhost:8000/frontend/login.html**
