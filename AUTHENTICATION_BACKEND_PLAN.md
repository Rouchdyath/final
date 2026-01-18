# 🔌 Plan d'Intégration Backend - Authentification Django

## 📊 Vue d'ensemble

Ce document explique comment intégrer le système d'authentification frontend avec l'API Django backend.

## 🎯 Objectifs

- Remplacer le système de démo par une authentification réelle
- Implémenter les endpoints Django REST Framework
- Sécuriser les tokens et les sessions
- Valider les permissions côté serveur

## 📝 Endpoints à Créer

### 1. POST `/api/auth/login/`

**Requête:**
```json
{
  "username": "jean.dupont",
  "password": "securepassword123",
  "role": "etudiant"
}
```

**Réponse (Succès):**
```json
{
  "success": true,
  "user": {
    "id": 42,
    "username": "jean.dupont",
    "email": "jean@example.com",
    "role": "etudiant",
    "first_name": "Jean",
    "last_name": "Dupont"
  },
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Réponse (Erreur):**
```json
{
  "success": false,
  "error": "Identifiants invalides"
}
```

### 2. POST `/api/auth/logout/`

**Requête:**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Réponse:**
```json
{
  "success": true,
  "message": "Déconnexion réussie"
}
```

### 3. POST `/api/auth/verify/`

**Requête:**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Réponse:**
```json
{
  "valid": true,
  "user": {
    "id": 42,
    "username": "jean.dupont",
    "role": "etudiant"
  }
}
```

### 4. GET `/api/auth/permissions/`

**Requête (Header):**
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Réponse:**
```json
{
  "user_id": 42,
  "role": "etudiant",
  "permissions": [
    "liste-travaux.html",
    "soumettre-livraison.html",
    "mes-notes.html"
  ]
}
```

## 🔨 Implémentation Django

### 1. Modèle d'Utilisateur Étendu

```python
# models.py
from django.contrib.auth.models import User
from django.db import models

ROLE_CHOICES = [
    ('etudiant', 'Étudiant'),
    ('formateur', 'Formateur'),
    ('directeur', 'Directeur'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} ({self.role})"
```

### 2. Serializer

```python
# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'role', 'first_name', 'last_name']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    role = serializers.CharField(required=False)
```

### 3. Vue d'Authentification

```python
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import UserProfile
from .serializers import UserProfileSerializer, LoginSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            role = serializer.validated_data.get('role')
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                # Vérifier le rôle si fourni
                profile = UserProfile.objects.get(user=user)
                
                if role and profile.role != role:
                    return Response({
                        'success': False,
                        'error': 'Le rôle ne correspond pas'
                    }, status=status.HTTP_400_BAD_REQUEST)
                
                # Générer le token
                refresh = RefreshToken.for_user(user)
                
                return Response({
                    'success': True,
                    'user': UserProfileSerializer(profile).data,
                    'token': str(refresh.access_token),
                    'refresh_token': str(refresh)
                })
            
            return Response({
                'success': False,
                'error': 'Identifiants invalides'
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()
            
            return Response({'success': True, 'message': 'Déconnexion réussie'})
        except Exception as e:
            return Response({'success': False, 'error': str(e)}, 
                          status=status.HTTP_400_BAD_REQUEST)

class VerifyTokenView(APIView):
    def post(self, request):
        from rest_framework.authtoken.models import Token
        
        token = request.data.get('token')
        
        try:
            # Vérifier le JWT token
            from rest_framework_simplejwt.tokens import AccessToken
            decoded_token = AccessToken(token)
            user_id = decoded_token['user_id']
            user = User.objects.get(id=user_id)
            profile = UserProfile.objects.get(user=user)
            
            return Response({
                'valid': True,
                'user': UserProfileSerializer(profile).data
            })
        except Exception as e:
            return Response({'valid': False}, status=status.HTTP_401_UNAUTHORIZED)
```

### 4. URLs

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('auth/login/', views.LoginView.as_view(), name='login'),
    path('auth/logout/', views.LogoutView.as_view(), name='logout'),
    path('auth/verify/', views.VerifyTokenView.as_view(), name='verify'),
]
```

### 5. Settings Django

```python
# settings.py

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# JWT Configuration
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]
```

## 📱 Modification Frontend

### 1. Mettre à jour `auth.js`

```javascript
// auth.js - Fonction login() modifiée

async function login(identifier, password, role) {
    try {
        const response = await fetch('http://localhost:8000/api/auth/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: identifier,
                password: password,
                role: role
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            const user = {
                id: data.user.id,
                identifier: data.user.username,
                role: data.user.role,
                email: data.user.email,
                token: data.token,
                refreshToken: data.refresh_token,
                loginTime: new Date().getTime()
            };
            
            localStorage.setItem('currentUser', JSON.stringify(user));
            return user;
        }
        
        throw new Error(data.error || 'Erreur de connexion');
    } catch (error) {
        throw new Error('Erreur réseau: ' + error.message);
    }
}

// Logout modifié
async function logout() {
    const user = getCurrentUser();
    
    try {
        if (user && user.refreshToken) {
            await fetch('http://localhost:8000/api/auth/logout/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${user.token}`
                },
                body: JSON.stringify({
                    refresh_token: user.refreshToken
                })
            });
        }
    } catch (error) {
        console.error('Erreur lors de la déconnexion:', error);
    } finally {
        localStorage.removeItem('currentUser');
        window.location.href = 'login.html';
    }
}
```

### 2. Ajouter le Token aux Requêtes API

```javascript
// Fonction helper pour les requêtes authentifiées
async function fetchWithAuth(url, options = {}) {
    const user = getCurrentUser();
    
    const headers = {
        'Content-Type': 'application/json',
        ...options.headers
    };
    
    if (user && user.token) {
        headers['Authorization'] = `Bearer ${user.token}`;
    }
    
    const response = await fetch(url, {
        ...options,
        headers
    });
    
    // Vérifier l'expiration du token
    if (response.status === 401) {
        // Token expiré, rediriger vers login
        logout();
        return;
    }
    
    return response;
}

// Utilisation
const response = await fetchWithAuth('http://localhost:8000/api/livraisons/', {
    method: 'GET'
});
```

## 🔐 Sécurité - Points Importants

### ✅ À Faire

- [ ] Utiliser HTTPS en production
- [ ] Valider les tokens côté serveur
- [ ] Implémenter rate limiting
- [ ] Logger les connexions/déconnexions
- [ ] Gérer l'expiration des tokens
- [ ] Implémenter un refresh token mechanism
- [ ] Chiffrer les mots de passe (Django le fait automatiquement)
- [ ] Implémenter CSRF protection
- [ ] Ajouter des headers de sécurité (CORS, CSP, etc.)

### ❌ À Éviter

- Ne pas stocker les mots de passe en clair
- Ne pas envoyer les tokens en clair par HTTP
- Ne pas fiducia les permissions côté client uniquement
- Ne pas laisser les tokens expirer sans redirection
- Ne pas exposer les tokens dans les logs

## 📊 Migration des Utilisateurs

```sql
-- SQL pour créer les utilisateurs de test
INSERT INTO auth_user (username, password, email) VALUES
('etudiant1', 'pbkdf2_sha256$...', 'etudiant1@example.com'),
('formateur1', 'pbkdf2_sha256$...', 'formateur1@example.com'),
('directeur1', 'pbkdf2_sha256$...', 'directeur1@example.com');

-- Créer les profils
INSERT INTO app_userprofile (user_id, role) VALUES
(1, 'etudiant'),
(2, 'formateur'),
(3, 'directeur');
```

## 🧪 Tests à Effectuer

```python
# tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import UserProfile

class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user('test', 'test@test.com', 'pass')
        self.profile = UserProfile.objects.create(user=self.user, role='etudiant')
    
    def test_login_success(self):
        response = self.client.post('/api/auth/login/', {
            'username': 'test',
            'password': 'pass',
            'role': 'etudiant'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['success'])
        self.assertIn('token', response.data)
    
    def test_login_fail(self):
        response = self.client.post('/api/auth/login/', {
            'username': 'test',
            'password': 'wrong',
            'role': 'etudiant'
        })
        self.assertEqual(response.status_code, 401)
        self.assertFalse(response.data['success'])
```

## 📈 Prochaines Étapes

1. **Phase 1: Implémentation Backend**
   - Créer les modèles UserProfile
   - Implémenter les endpoints d'authentification
   - Configurer JWT
   - Écrire les tests

2. **Phase 2: Intégration Frontend**
   - Modifier auth.js pour utiliser l'API
   - Ajouter la gestion des tokens
   - Implémenter le refresh automatique
   - Tester tous les rôles

3. **Phase 3: Sécurité**
   - Implémenter CORS correctement
   - Ajouter rate limiting
   - Ajouter logging d'audit
   - Tester les scénarios de sécurité

4. **Phase 4: Déploiement**
   - Configurer HTTPS
   - Déployer en production
   - Monitorer les authentifications
   - Maintenir les logs de sécurité

---

**Statut:** 📋 Plan détaillé - Prêt à implémenter
**Durée estimée:** 2-3 jours de développement
