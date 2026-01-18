# 🗺️ Carte du Système - URLs et Navigation

## 📍 Points d'Entrée Principaux

### Page de Connexion
```
URL: http://localhost:8000/frontend/login.html
Description: Page principale - choisir rôle et se connecter
Accès: Sans authentification
```

### Page d'Inscription
```
URL: http://localhost:8000/frontend/signup.html
Description: Créer un compte avec vérification email
Accès: Sans authentification
Lien depuis: login.html "S'inscrire ici →"
```

### Dashboard / Accueil
```
URL: http://localhost:8000/frontend/index.html
Description: Page d'accueil personnalisée
Accès: Authentifiés uniquement
Redirection: Vers login.html si pas connecté
```

---

## 👤 Pages Étudiant (3 pages)

```
┌─────────────────────────────────────────┐
│  Rôle: Étudiant                         │
│  Menu: 4 liens                          │
└─────────────────────────────────────────┘

1. 📚 Mes Travaux
   URL: liste-travaux.html
   Actions: Voir tous les travaux assignés

2. 📤 Soumettre une Livraison
   URL: soumettre-livraison.html
   Actions: Remettre un travail

3. ⭐ Mes Notes
   URL: mes-notes.html
   Actions: Voir les notes et évaluations

4. 📂 Retour Accueil
   URL: index.html
   Actions: Revenir au dashboard
```

---

## 📚 Pages Formateur (9 pages)

```
┌─────────────────────────────────────────┐
│  Rôle: Formateur                        │
│  Menu: 9 liens                          │
└─────────────────────────────────────────┘

GESTION DES ESPACES:
1. 🏫 Créer un Espace
   URL: creer-espace.html
   Actions: Créer un nouvel espace

2. 📋 Mes Espaces
   URL: liste-espaces.html
   Actions: Voir et gérer ses espaces

GESTION DU PERSONNEL:
3. 👨‍🏫 Gérer Formateurs
   URL: ajouter-formateur.html
   Actions: Ajouter des formateurs

4. 👨‍🎓 Ajouter Étudiants
   URL: ajouter-etudiant-espace.html
   Actions: Ajouter étudiants à un espace

GESTION DES TRAVAUX:
5. 📝 Créer un Travail
   URL: creer-travail.html
   Actions: Créer un nouveau travail

6. 📌 Assigner des Travaux
   URL: assigner-travail.html
   Actions: Assigner travaux aux étudiants

7. ✅ Évaluer Livraisons
   URL: evaluer-livraisons.html
   Actions: Noter et commenter les livraisons

8. 📊 Consulter Travaux
   URL: consultation-formateur-travaux.html
   Actions: Voir l'historique des travaux

NAVIGATION:
9. 📂 Retour Accueil
   URL: index.html
   Actions: Revenir au dashboard
```

---

## 👁️ Pages Directeur (13 pages - TOUTES)

```
┌─────────────────────────────────────────┐
│  Rôle: Directeur                        │
│  Menu: 13 liens (ACCÈS COMPLET)         │
└─────────────────────────────────────────┘

GESTION DES ESPACES:
1. 🏫 Créer un Espace
   URL: creer-espace.html

2. 📋 Tous les Espaces
   URL: liste-espaces.html

3. 🎯 Consulter Espaces
   URL: consultation-directeur-espaces.html

GESTION DU PERSONNEL:
4. 👨‍🏫 Gérer Formateurs
   URL: ajouter-formateur.html

5. 👨‍🎓 Gérer Étudiants
   URL: creer-etudiant.html

6. 📋 Consulter Étudiants
   URL: consultation-directeur-etudiants.html

GESTION DES PROMOTIONS:
7. 📝 Créer Promotion
   URL: creer-promotion.html

8. 📊 Consulter Promotions
   URL: consultation-directeur-promotions.html

GESTION DES TRAVAUX:
9. 📝 Créer un Travail
   URL: creer-travail.html

10. 📌 Assigner des Travaux
    URL: assigner-travail.html

11. ✅ Évaluer Livraisons
    URL: evaluer-livraisons.html

12. 📚 Tous les Travaux
    URL: liste-travaux.html

NAVIGATION:
13. 📂 Retour Accueil
    URL: index.html
```

---

## 🔄 Flux de Navigation Standard

```
┌──────────────────┐
│  login.html      │  Sélectionner rôle
│  signup.html     │  OU S'inscrire
└────────┬─────────┘
         │ Se connecter
         ▼
┌──────────────────┐
│  index.html      │  Dashboard principal
│  (sidebar)       │  Menu selon rôle
└────────┬─────────┘
         │ Cliquer sur menu
         ▼
┌──────────────────┐
│ Page spécifique  │  Formulaire ou liste
│ (selon rôle)     │  Sidebar reste visible
└────────┬─────────┘
         │ Cliquer menu
         ▼
┌──────────────────┐
│ Autre page       │  ...
│ (selon rôle)     │
└──────────────────┘
```

---

## 📱 Structure des Fichiers Frontend

```
frontend/
├─ login.html              ← Point d'entrée principal
├─ signup.html             ← Inscription + vérification
├─ index.html              ← Dashboard (authentifié)
├─ auth.js                 ← Logique d'authentification
├─ sidebar.js              ← Menu dynamique
│
├─ ÉTUDIANT:
│  ├─ liste-travaux.html
│  ├─ soumettre-livraison.html
│  └─ mes-notes.html
│
├─ FORMATEUR:
│  ├─ creer-espace.html
│  ├─ liste-espaces.html
│  ├─ ajouter-formateur.html
│  ├─ ajouter-etudiant-espace.html
│  ├─ creer-travail.html
│  ├─ assigner-travail.html
│  ├─ evaluer-livraisons.html
│  └─ consultation-formateur-travaux.html
│
├─ DIRECTEUR:
│  ├─ creer-etudiant.html
│  ├─ creer-promotion.html
│  ├─ consultation-directeur-etudiants.html
│  ├─ consultation-directeur-promotions.html
│  ├─ consultation-directeur-espaces.html
│  ├─ ajouter-etudiant-promotion.html
│  ├─ liste-etudiants.html
│  ├─ liste-promotions.html
│  └─ ... (tous les autres)
│
└─ styles.css              ← Styles partagés
```

---

## 🔐 Authentification Flow

```
INSCRIPTION:
signup.html
  └─ Formulaire inscription
  └─ Validation email
  └─ Génération code (console)
  └─ Vérification code
  └─ localStorage.app_users.push()
  └─ Redirection login.html

CONNEXION:
login.html
  └─ Sélection rôle
  └─ Identifiant + mot de passe
  └─ auth.js: login()
  └─ localStorage.currentUser = {...}
  └─ Redirection index.html

PROTECTION:
sidebar.js: initSidebar()
  └─ Vérifie localStorage.currentUser
  └─ Si vide → Redirection login.html
  └─ Si présent → Menu selon rôle

DÉCONNEXION:
logout() [auth.js]
  └─ localStorage.removeItem('currentUser')
  └─ Redirection login.html
```

---

## 🚦 Contrôle d'Accès par Rôle

```
Page                                  │ Étudiant │ Formateur │ Directeur
─────────────────────────────────────────────────────────────────────
index.html (Dashboard)                │    ✅    │     ✅    │    ✅
login.html                            │    ✅    │     ✅    │    ✅
signup.html                           │    ✅    │     ✅    │    ✅
─────────────────────────────────────────────────────────────────────
liste-travaux.html                    │    ✅    │     ❌    │    ✅
soumettre-livraison.html              │    ✅    │     ❌    │    ✅
mes-notes.html                        │    ✅    │     ❌    │    ✅
─────────────────────────────────────────────────────────────────────
creer-espace.html                     │    ❌    │     ✅    │    ✅
liste-espaces.html                    │    ❌    │     ✅    │    ✅
ajouter-formateur.html                │    ❌    │     ✅    │    ✅
ajouter-etudiant-espace.html          │    ❌    │     ✅    │    ✅
creer-travail.html                    │    ❌    │     ✅    │    ✅
assigner-travail.html                 │    ❌    │     ✅    │    ✅
evaluer-livraisons.html               │    ❌    │     ✅    │    ✅
consultation-formateur-travaux.html   │    ❌    │     ✅    │    ✅
─────────────────────────────────────────────────────────────────────
creer-etudiant.html                   │    ❌    │     ❌    │    ✅
creer-promotion.html                  │    ❌    │     ❌    │    ✅
consultation-directeur-etudiants.html │    ❌    │     ❌    │    ✅
consultation-directeur-promotions.html│    ❌    │     ❌    │    ✅
consultation-directeur-espaces.html   │    ❌    │     ❌    │    ✅
ajouter-etudiant-promotion.html       │    ❌    │     ❌    │    ✅
liste-etudiants.html                  │    ❌    │     ❌    │    ✅
liste-promotions.html                 │    ❌    │     ❌    │    ✅
```

---

## 🔗 Liens Rapides

### Pages Publiques
- **login.html** - Connexion
- **signup.html** - Inscription

### Pages Protégées
- **Toute autre page** - Redirection auto si pas authentifié

### Redirection
```javascript
// Dans auth.js
function checkAccessAndRedirect() {
    if (!isLoggedIn()) {
        window.location.href = 'login.html';
    }
}

// Dans sidebar.js
if (currentPage !== 'login.html' && currentPage !== 'signup.html') {
    checkAccessAndRedirect();
}
```

---

## 📊 Statistics

```
Total des pages:              20
Pages publiques (non-auth):    2 (login, signup)
Pages protégées:              18
  ├─ Étudiant:                3
  ├─ Formateur:               9
  └─ Directeur:              13 (toutes)

Rôles:                         3
  ├─ Étudiant
  ├─ Formateur
  └─ Directeur

Rotas:
  ├─ login.html → signup.html (lien)
  ├─ signup.html → login.html (redirection)
  ├─ login.html → index.html (après connexion)
  ├─ index.html → pages selon menu (sidebar)
  └─ N'importe quelle page → login.html (si pas connecté)
```

---

## 🎯 Chemins de Cas d'Usage

### Cas 1: Nouvel Utilisateur
```
1. http://localhost:8000/frontend/login.html
2. Cliquer "S'inscrire ici →"
3. signup.html → Remplir formulaire
4. Vérifier email (F12 → Console)
5. Entrer code
6. Redirection login.html
7. Se connecter
8. index.html avec menu personnalisé
```

### Cas 2: Utilisateur Existant
```
1. http://localhost:8000/frontend/login.html
2. Sélectionner rôle
3. Entrer identifiants
4. Se connecter
5. index.html avec menu personnalisé
6. Naviguer via menu sidebar
```

### Cas 3: Session Expirée
```
1. User sur n'importe quelle page
2. Ferme navigateur ou localStorage purgé
3. Accès à une page
4. Redirection auto vers login.html
5. Reconnecter
```

---

**Carte complète du système - Mise à jour: 17 janvier 2026**
