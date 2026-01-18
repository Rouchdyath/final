# 🔐 Architecture d'Authentification - Diagramme Détaillé

## 1. Architecture Globale

```
┌──────────────────────────────────────────────────────────────┐
│                  APPLICATION WEB                             │
├──────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌────────────────┐      ┌─────────────────────────────────┐ │
│  │  login.html    │      │    Autres pages HTML            │ │
│  │ (Publique)     │      │   (Protégées)                   │ │
│  └────────┬───────┘      └─────────────────────────────────┘ │
│           │                           │                       │
│           └───────┬──────────────────┘                       │
│                   │                                           │
│           ┌───────▼────────┐                                 │
│           │   auth.js      │  (Logique d'auth)              │
│           │   sidebar.js   │  (Menu dynamique)              │
│           └────────────────┘                                 │
│                   │                                           │
│           ┌───────▼──────────┐                               │
│           │ localStorage     │  (Session client)             │
│           │  currentUser     │                               │
│           └──────────────────┘                               │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

## 2. Flux de Connexion Détaillé

```
ÉTAPE 1: Visite du site
┌─────────────────────┐
│ Utilisateur visite  │
│ www.app.com/        │
└────────┬────────────┘
         │
         ↓
ÉTAPE 2: Vérification de connexion
┌──────────────────────────────────────┐
│ checkAccessAndRedirect()              │
│ isLoggedIn() ?                        │
└────┬──────────────────────────┬───────┘
     │                          │
    OUI                        NON
     │                          │
     ↓                          ↓
┌──────────────┐         ┌──────────────────┐
│ Afficher     │         │ Rediriger vers   │
│ dashboard    │         │ login.html       │
└──────────────┘         └────────┬─────────┘
     │                            │
     │                 ÉTAPE 3: Connexion
     │                 ┌──────────────────┐
     │                 │ 1. Sélect rôle   │
     │                 │ 2. Identifiant   │
     │                 │ 3. Mot de passe  │
     │                 │ 4. Soumettre     │
     │                 └────────┬─────────┘
     │                          │
     │                ÉTAPE 4: Auth backend
     │                ┌──────────────────────┐
     │                │ login(id, pwd, role) │
     │                └────────┬─────────────┘
     │                         │
     │        ÉTAPE 5: Stockage session
     │        ┌─────────────────────────┐
     │        │localStorage.setItem(     │
     │        │'currentUser',            │
     │        │{id, identifier, role})   │
     │        └────────┬────────────────┘
     │                 │
     └────────┬────────┘
              │
    ÉTAPE 6: Redirection
    ┌────────────────────────┐
    │ window.location.href = │
    │ index.html             │
    └────────┬───────────────┘
             │
    ÉTAPE 7: Chargement dashboard
    ┌────────────────────────┐
    │ initSidebar()           │
    │ - Lit rôle              │
    │ - Affiche menu rôle     │
    │ - Affiche infos user    │
    └────────────────────────┘
```

## 3. Structure de Permissions

```
Rôles disponibles:
│
├─ 👤 ÉTUDIANT
│  └─ Pages (3):
│     ├─ liste-travaux.html
│     ├─ soumettre-livraison.html
│     └─ mes-notes.html
│
├─ 📚 FORMATEUR
│  └─ Pages (9):
│     ├─ creer-espace.html
│     ├─ liste-espaces.html
│     ├─ ajouter-formateur.html
│     ├─ creer-formateur.html
│     ├─ creer-travail.html
│     ├─ assigner-travail.html
│     ├─ liste-travaux.html
│     ├─ evaluer-livraisons.html
│     └─ consultation-formateur-travaux.html
│
└─ 👁️ DIRECTEUR
   └─ Pages (19 - TOUTES):
      ├─ [Toutes les pages du formateur]
      ├─ creer-etudiant.html
      ├─ ajouter-etudiant-espace.html
      ├─ creer-promotion.html
      ├─ ajouter-etudiant-promotion.html
      ├─ liste-etudiants.html
      ├─ liste-promotions.html
      ├─ consultation-directeur-espaces.html
      ├─ consultation-directeur-etudiants.html
      └─ consultation-directeur-promotions.html
```

## 4. Cycle de Vie de la Session

```
LOGIN                           NAVIGATION                      LOGOUT
│                               │                               │
├─ Sélect rôle                  ├─ Vérifier auth               ├─ Click logout
├─ Entrer ID/PWD               ├─ Vérifier accès page         ├─ Appel logout()
├─ Cliquer Se Connecter        ├─ Charger contenu             ├─ Supprimer localStorage
├─ Appel login()               ├─ Afficher menu rôle          ├─ Rediriger login.html
├─ Créer user object           ├─ Permettre navigation         ├─ Session effacée
├─ localStorage.setItem()       │                               │
├─ Rediriger index.html        │ (Boucle continue)             │
└─ Afficher dashboard          │                               └─ Fin session

      30 sec                    ∞ (jusqu'à logout)                  1 sec
```

## 5. Arborescence des Fichiers

```
frontend/
├─ auth.js                      ← Logique d'authentification
├─ sidebar.js                   ← Menu dynamique par rôle
├─ login.html                   ← Page de connexion
├─ index.html                   ← Dashboard (protégé)
├─ test-auth.html               ← Page de test
│
├─ Étudiant:
│  ├─ liste-travaux.html
│  ├─ soumettre-livraison.html
│  └─ mes-notes.html
│
├─ Formateur:
│  ├─ creer-espace.html
│  ├─ liste-espaces.html
│  ├─ ajouter-formateur.html
│  ├─ creer-formateur.html
│  ├─ creer-travail.html
│  ├─ assigner-travail.html
│  └─ evaluer-livraisons.html
│
└─ Directeur:
   ├─ creer-etudiant.html
   ├─ ajouter-etudiant-espace.html
   ├─ creer-promotion.html
   └─ consultation-*.html

Documentation/
├─ AUTHENTICATION_GUIDE.md       ← Guide complet
└─ AUTHENTICATION_IMPLEMENTATION.md ← Implémentation
```

## 6. État de l'Authentification

```
localStorage['currentUser'] = {
  "id": "abc123xyz",                    ← ID aléatoire unique
  "identifier": "jean.dupont",          ← Nom d'utilisateur
  "role": "formateur",                  ← Rôle: etudiant|formateur|directeur
  "loginTime": 1705497600000            ← Timestamp de connexion
}
```

## 7. Flux de Vérification d'Accès

```
L'utilisateur essaie d'accéder à une page
            │
            ↓
    checkAccessAndRedirect()
            │
     ┌──────┴──────┐
     │             │
  connecté?      non
     │             │
    OUI            ↓
     │      Rediriger login.html
     │             
     ↓
  PAGE = fichier actuel
  ROLE = localStorage.role
     │
     ├─ ROLE_PERMISSIONS[ROLE] → Liste pages
     │
     ├─ PAGE dans liste ?
     │ │
     │ OUI         NON
     │  │           │
     │  ↓           ↓
     │ AFFICHER   REDIRIGER
     │  PAGE      INDEX.HTML
     │             + ALERT
     │
     └─ CONTINUER NAVIGATION
```

## 8. Points d'Entrée de Sécurité

```
┌─────────────────────────────────────────────────────────────┐
│ SÉCURITÉ - Points de vérification                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ 1. Page login.html                                          │
│    └─ Pas de vérification (publique)                       │
│                                                              │
│ 2. index.html (dashboard)                                   │
│    ├─ Vérification: isLoggedIn()                           │
│    └─ Redirection: vers login.html si non connecté         │
│                                                              │
│ 3. Autres pages (soumettre-livraison, créer-espace, etc)   │
│    ├─ Script: auth.js chargé                              │
│    ├─ Vérification: checkAccessAndRedirect()              │
│    ├─ Règle: ROLE_PERMISSIONS[role].includes(page)       │
│    └─ Redirection: vers index.html si pas accès           │
│                                                              │
│ 4. Sidebar                                                  │
│    ├─ getUserStoriesByRole(role)                          │
│    └─ Affiche menu filtré par rôle                        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## 9. Exemple de Test

```
TEST: Étudiant essaie d'accéder à creer-espace.html

1. localStorage['currentUser'] = {
     "role": "etudiant"
   }

2. URL: /frontend/creer-espace.html

3. checkAccessAndRedirect() s'exécute
   - Page = "creer-espace.html"
   - Role = "etudiant"
   - Permissions = ["liste-travaux.html", "soumettre-livraison.html", "mes-notes.html"]

4. "creer-espace.html" dans Permissions ?
   → NON

5. Action:
   - alert("Vous n'avez pas accès à cette page.")
   - window.location.href = "index.html"

RÉSULTAT: Utilisateur redirigé ✅
```

## 10. États Possibles

```
┌─────────────────────────────────────────────────────────┐
│ ÉTAT: Utilisateur NON connecté                          │
├─────────────────────────────────────────────────────────┤
│ - localStorage['currentUser'] = null                    │
│ - isLoggedIn() = false                                  │
│ - getCurrentRole() = null                               │
│ - Accès: login.html seulement                           │
│ - Redirection auto: vers login.html                     │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ ÉTAT: Utilisateur connecté (étudiant)                   │
├─────────────────────────────────────────────────────────┤
│ - localStorage['currentUser'] = {id, identifier, role}  │
│ - isLoggedIn() = true                                   │
│ - getCurrentRole() = "etudiant"                         │
│ - Accès: 3 pages seulement                              │
│ - Sidebar: 2 US visibles                                │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ ÉTAT: Utilisateur connecté (formateur)                  │
├─────────────────────────────────────────────────────────┤
│ - localStorage['currentUser'] = {id, identifier, role}  │
│ - isLoggedIn() = true                                   │
│ - getCurrentRole() = "formateur"                        │
│ - Accès: 9 pages                                        │
│ - Sidebar: 4 US visibles                                │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ ÉTAT: Utilisateur connecté (directeur)                  │
├─────────────────────────────────────────────────────────┤
│ - localStorage['currentUser'] = {id, identifier, role}  │
│ - isLoggedIn() = true                                   │
│ - getCurrentRole() = "directeur"                        │
│ - Accès: TOUTES les pages (19)                          │
│ - Sidebar: TOUTES les US (6) visibles                   │
└─────────────────────────────────────────────────────────┘
```

---

**Last Update:** 2026-01-17
**Version:** 1.0 - Mode Démo
**Status:** ✅ Complet et Fonctionnel
