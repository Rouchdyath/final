# Système d'Authentification et Gestion des Rôles

## 📋 Vue d'ensemble

Le système d'authentification permet à trois types d'utilisateurs d'accéder à l'application avec des permissions différentes:

1. **👤 Étudiant** - Accès limité aux fonctionnalités d'étudiant
2. **📚 Formateur** - Accès aux fonctionnalités de formateur
3. **👁️ Directeur** - Accès complet à toutes les fonctionnalités

## 🔑 Fichiers Clés

### `auth.js`
Gère l'authentification et les permissions:
- `login(identifier, password, role)` - Connecter un utilisateur
- `logout()` - Déconnecter l'utilisateur
- `isLoggedIn()` - Vérifier si connecté
- `getCurrentUser()` - Obtenir les infos de l'utilisateur
- `getCurrentRole()` - Obtenir le rôle actuel
- `hasAccessToPage(pageName)` - Vérifier l'accès à une page
- `checkAccessAndRedirect()` - Vérifier et rediriger si nécessaire

### `login.html`
Page de connexion avec:
- Sélection du rôle (Étudiant, Formateur, Directeur)
- Champs de login (identifiant + mot de passe)
- Mode démo pour tester facilement

### `sidebar.js`
Affiche le menu de navigation basé sur le rôle de l'utilisateur

## 🔐 Accès par Rôle

### 👤 Étudiant
Pages accessibles:
- `liste-travaux.html` - Voir les travaux assignés
- `soumettre-livraison.html` - Soumettre ses travaux
- `mes-notes.html` - Consulter ses notes et feedback

### 📚 Formateur
Pages accessibles:
- `creer-espace.html` - Créer des espaces
- `liste-espaces.html` - Consulter les espaces
- `ajouter-formateur.html` - Assigner des formateurs
- `creer-formateur.html` - Créer des formateurs
- `creer-travail.html` - Créer des travaux
- `assigner-travail.html` - Assigner des travaux
- `liste-travaux.html` - Consulter les travaux
- `evaluer-livraisons.html` - Évaluer les livraisons
- `consultation-formateur-travaux.html` - Supervision des travaux

### 👁️ Directeur
Pages accessibles:
- **Toutes les pages** (accès complet)

## 🚀 Utilisation

### Première connexion

1. Accédez à `http://localhost:8000/frontend/login.html`
2. Sélectionnez votre rôle
3. Entrez vos identifiants (en mode démo, n'importe quel texte fonctionne)
4. Cliquez sur "Se Connecter"

### Mode Démo

En mode démo, vous pouvez:
- Sélectionner n'importe quel rôle
- Entrer n'importe quel identifiant/mot de passe
- Vous serez immédiatement connecté avec le rôle sélectionné

### Déconnexion

Cliquez sur le bouton "Déconnexion" dans la sidebar pour vous déconnecter. Vous serez redirigé vers la page de login.

## 💾 Stockage des Données

Les informations de l'utilisateur sont stockées dans `localStorage`:

```javascript
{
    id: "unique-id",
    identifier: "nom-utilisateur",
    role: "etudiant|formateur|directeur",
    loginTime: 1234567890
}
```

## 🔒 Sécurité

**Note:** Ce système est une implémentation de démo. En production, vous devez:

1. Implémenter l'authentification côté serveur (Django REST Framework)
2. Utiliser des tokens JWT ou des sessions sécurisées
3. Valider les permissions côté serveur
4. Chiffrer les mots de passe
5. Implémenter une protection CSRF

## 📝 Exemple d'Intégration API

Pour intégrer avec votre backend Django:

```javascript
async function login(identifier, password, role) {
    const response = await fetch('http://localhost:8000/api/auth/login/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: identifier, password, role })
    });
    
    const data = await response.json();
    
    if (data.success) {
        localStorage.setItem('currentUser', JSON.stringify({
            id: data.user.id,
            identifier: data.user.username,
            role: data.user.role,
            token: data.token,
            loginTime: new Date().getTime()
        }));
        return data.user;
    }
    
    throw new Error(data.error);
}
```

## 🎯 Flux d'Authentification

```
login.html (page publique)
    ↓
[Sélectionnez rôle + identifiants]
    ↓
auth.js login()
    ↓
localStorage.setItem('currentUser')
    ↓
index.html (page protégée)
    ↓
checkAccessAndRedirect() valide l'accès
    ↓
sidebar.js affiche le menu du rôle
    ↓
Navigation selon les permissions
```

## ⚠️ Limitations Actuelles

- Pas de backend API (mode démo uniquement)
- Les données de login ne sont pas persistées
- Pas de gestion de session
- Les mots de passe ne sont pas validés

## ✨ Améliorations Futures

1. Intégration avec l'API Django
2. Tokens JWT pour l'authentification
3. Gestion des sessions
4. Récupération de profil utilisateur
5. Modification du profil
6. Gestion des mots de passe oubliés
7. Logs d'audit
8. 2FA (Two-Factor Authentication)
