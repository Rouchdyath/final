# 👨‍💻 GUIDE DÉVELOPPEUR - Architecture Nouvelle

## 📋 Table des matières
1. [Fichiers modifiés](#fichiers-modifiés)
2. [Architecture](#architecture)
3. [Intégration API](#intégration-api)
4. [Prochaines étapes](#prochaines-étapes)

---

## 📁 Fichiers Modifiés

### 1. sidebar.js - ENTIÈREMENT REFACTORISÉ

#### Avant (User Stories)
```javascript
// Ancien système
const userStories = getUserStoriesByRole(userRole);
let storiesHTML = userStories.map(story => `
    <div class="user-story">
        <div class="story-header" onclick="toggleStory(this)">
            ...story content...
        </div>
    </div>
`);
```

#### Après (Menu Simple)
```javascript
// Nouveau système
const menuItems = {
    'etudiant': [
        { icon: '📚', text: 'Mes Travaux', href: 'liste-travaux.html' },
        { icon: '📤', text: 'Soumettre une Livraison', href: '...' },
        ...
    ],
    'formateur': [ ... ],
    'directeur': [ ... ]
};

const items = menuItems[userRole] || [];
let menuHTML = items.map(item => `
    <a href="${item.href}" class="menu-item">
        <span class="menu-icon">${item.icon}</span>
        <span class="menu-text">${item.text}</span>
    </a>
`);
```

#### Structure CSS Changée
```css
/* Ancien */
.sidebar-stories { /* layout avec user stories */ }
.user-story { /* expand/collapse */ }
.story-header { /* clickable */ }

/* Nouveau */
.sidebar-nav { /* sticky sidebar */ }
.menu-item { /* simple links */ }
.user-avatar { /* avatar display */ }
```

#### Points Clés
- ✅ Suppression de `getUserStoriesByRole()`
- ✅ Suppression de `toggleStory()`
- ✅ Menu direct sans nesting
- ✅ Responsive mobile friendly

---

### 2. login.html - AMÉLIORATION

```html
<!-- Ajout: Lien vers inscription -->
<a href="signup.html" style="...">S'inscrire ici →</a>

<!-- Modifications: Style cohérent avec signup.html -->
```

#### Comportement
```
Avant: Connexion seulement
Après: Connexion + Lien vers inscription
```

---

### 3. signup.html - NOUVEAU FICHIER COMPLET

#### Structure HTML
```html
<div id="signupForm" class="verification-step active">
    <!-- Formulaire d'inscription -->
</div>

<div id="verificationForm" class="verification-step">
    <!-- Étape 2: Vérification email -->
</div>

<div id="successStep" class="verification-step">
    <!-- Étape 3: Succès -->
</div>
```

#### Fonctions JavaScript
```javascript
function handleSignup(event) {
    // Validation des données
    // Vérification des doublons
    // Génération du code
    // Sauvegarde dans localStorage
    // Affichage de l'étape de vérification
}

function handleVerification(event) {
    // Validation du code
    // Création de l'utilisateur
    // Sauvegarde dans localStorage
    // Redirection vers login
}

function resendCode(event) {
    // Renvoi du code email
}
```

#### Données Stockées
```javascript
// localStorage.pendingUser (avant vérification)
{
    email: "user@email.com",
    identifier: "username",
    password: "encoded-password",
    role: "etudiant|formateur",
    verificationCode: "123456",
    verified: false,
    registrationTime: timestamp
}

// localStorage.app_users (après vérification)
[
    {
        id: "unique-id",
        email: "user@email.com",
        identifier: "username",
        password: "encoded-password",
        role: "etudiant|formateur",
        verified: true,
        registrationTime: timestamp
    }
]
```

---

## 🏗️ Architecture

### Flux d'Inscription
```
signup.html
    ↓
handleSignup()
    ↓ [Validation]
    ↓ [Génération code]
Affiche verificationForm
    ↓
handleVerification()
    ↓ [Validation code]
localStorage.app_users.push(user)
    ↓
Affiche successStep
    ↓ [3 secondes]
Redirige vers login.html
```

### Flux de Connexion
```
login.html
    ↓
selectRole() + handleLogin()
    ↓
auth.js: login(identifier, password, role)
    ↓
localStorage.currentUser = {id, identifier, role, loginTime}
    ↓
Redirige vers index.html
```

### Flux de Navigation
```
index.html
    ↓
sidebar.js: initSidebar()
    ↓
Lit: localStorage.currentUser
    ↓
menuItems[role]
    ↓
Affiche menu adapté au rôle
```

---

## 🔌 Intégration API

### Phase 1: Validation Email (Sendgrid/AWS SES)

```python
# Django Backend
from django.core.mail import send_mail

@api_view(['POST'])
def register(request):
    email = request.data.get('email')
    identifier = request.data.get('identifier')
    password = request.data.get('password')
    role = request.data.get('role')
    
    # Vérifier unicité
    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email exists'}, status=400)
    
    # Générer code
    code = generate_code()  # 6 digits
    
    # Sauvegarder temporaire
    temp_user = TempUser.objects.create(
        email=email,
        identifier=identifier,
        password=password_hash(password),
        role=role,
        verification_code=code
    )
    
    # Envoyer email
    send_verification_email(email, code)
    
    return Response({'message': 'Check your email'})

@api_view(['POST'])
def verify(request):
    email = request.data.get('email')
    code = request.data.get('code')
    
    temp_user = TempUser.objects.get(email=email)
    
    if temp_user.verification_code != code:
        return Response({'error': 'Invalid code'}, status=400)
    
    # Créer l'utilisateur réel
    user = User.objects.create(
        email=temp_user.email,
        identifier=temp_user.identifier,
        password=temp_user.password,
        role=temp_user.role
    )
    
    # Supprimer temporaire
    temp_user.delete()
    
    return Response({'message': 'Email verified'})
```

### Phase 2: Authentification JWT

```python
# Django Backend
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def login(request):
    identifier = request.data.get('identifier')
    password = request.data.get('password')
    role = request.data.get('role')
    
    user = User.objects.get(identifier=identifier, role=role)
    
    if not check_password(password, user.password):
        return Response({'error': 'Invalid credentials'}, status=400)
    
    refresh = RefreshToken.for_user(user)
    
    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': {
            'id': user.id,
            'identifier': user.identifier,
            'email': user.email,
            'role': user.role
        }
    })
```

### Phase 3: Mise à jour Frontend

```javascript
// signup.js - Remplacer handleSignup
async function handleSignup(event) {
    event.preventDefault();
    
    const data = {
        email: document.getElementById('email').value,
        identifier: document.getElementById('identifier').value,
        password: document.getElementById('password').value,
        role: document.querySelector('input[name="role"]:checked').value
    };
    
    const response = await fetch('/api/auth/register/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    
    if (response.ok) {
        // Afficher l'étape de vérification
    } else {
        // Afficher erreur
    }
}

// auth.js - Remplacer login
async function login(identifier, password, role) {
    const response = await fetch('/api/auth/login/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ identifier, password, role })
    });
    
    const data = await response.json();
    
    localStorage.setItem('access_token', data.access);
    localStorage.setItem('refresh_token', data.refresh);
    localStorage.setItem('currentUser', JSON.stringify(data.user));
    
    return data.user;
}
```

---

## 🚀 Prochaines Étapes

### Court Terme (1-2 semaines)
1. **Tester complètement**
   - Tous les rôles
   - Inscription/Vérification
   - Navigation

2. **Corriger bugs**
   - Responsive mobile
   - Navigation rapide

### Moyen Terme (2-4 semaines)
1. **Intégrer API email**
   - Sendgrid ou AWS SES
   - Templates professionnels

2. **Ajouter sécurité**
   - Hash bcrypt des mots de passe
   - HTTPS obligatoire
   - Rate limiting

3. **Authentification JWT**
   - Tokens au lieu de localStorage
   - Refresh tokens
   - Validation serveur

### Long Terme (1-2 mois)
1. **Fonctionnalités avancées**
   - Récupération mot de passe
   - 2FA/MFA
   - OAuth/SSO

2. **Optimisations**
   - Performance
   - Caching
   - CDN

---

## 📊 Données Modèles Nécessaires (Django)

```python
# models.py

class User(models.Model):
    ROLES = (
        ('etudiant', 'Étudiant'),
        ('formateur', 'Formateur'),
        ('directeur', 'Directeur'),
    )
    
    email = models.EmailField(unique=True)
    identifier = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLES)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('email', 'role')

class TempUser(models.Model):
    email = models.EmailField()
    identifier = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20)
    verification_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
```

---

## 🔍 Tests à Faire

### Test 1: Inscription Complète
```
POST /api/auth/register/
{
    email: "test@test.com",
    identifier: "test",
    password: "Test1234!",
    role: "etudiant"
}

Attendu: Code envoyé, utilisateur créé
```

### Test 2: Vérification Email
```
POST /api/auth/verify/
{
    email: "test@test.com",
    code: "123456"
}

Attendu: Utilisateur vérifié
```

### Test 3: Connexion
```
POST /api/auth/login/
{
    identifier: "test",
    password: "Test1234!",
    role: "etudiant"
}

Attendu: JWT tokens + user data
```

---

## 📝 Checklist Développeur

- [ ] J'ai lu le guide complet
- [ ] J'ai testé l'inscription
- [ ] J'ai testé la vérification email (console)
- [ ] J'ai testé la connexion
- [ ] J'ai testé la navigation par rôle
- [ ] J'ai vérifié le responsive mobile
- [ ] J'ai préparé le backend API
- [ ] J'ai documenté mes changements

---

**Version:** 2.0
**Dernière mise à jour:** 17 janvier 2026
**Statut:** Production Ready (démo)
