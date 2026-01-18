# 🚀 Guide de Démarrage Rapide - Authentification

## ⚡ En 30 Secondes

### 1. Accédez à la page de connexion
```
http://localhost:8000/frontend/login.html
```

### 2. Sélectionnez votre rôle
- 👤 **Étudiant** - pour les étudiants
- 📚 **Formateur** - pour les formateurs
- 👁️ **Directeur** - pour les directeurs

### 3. Entrez vos identifiants
En mode démo, n'importe quel texte fonctionne:
```
Identifiant: jean
Mot de passe: test123
```

### 4. Cliquez sur "Se Connecter"
Vous serez redirigé vers le dashboard avec accès selon votre rôle.

## 📋 Rôles et Accès

### 👤 Étudiant
```
Pages accessibles:
  ✓ Voir les travaux
  ✓ Soumettre une livraison
  ✓ Consulter ses notes
```

### 📚 Formateur
```
Pages accessibles:
  ✓ Gérer les espaces
  ✓ Gérer les formateurs
  ✓ Créer et assigner des travaux
  ✓ Évaluer les livraisons
```

### 👁️ Directeur
```
Pages accessibles:
  ✓ TOUTES les pages
  ✓ Gestion complète du système
  ✓ Supervision de tout
```

## 🎯 Cas d'Usage

### Je suis étudiant
```
1. Allez à login.html
2. Sélectionnez "Étudiant"
3. Entrez vos identifiants
4. Vous accédez à:
   - Liste des travaux
   - Soumettre une livraison
   - Consulter vos notes
```

### Je suis formateur
```
1. Allez à login.html
2. Sélectionnez "Formateur"
3. Entrez vos identifiants
4. Vous accédez à:
   - Créer des espaces
   - Créer des travaux
   - Évaluer les livraisons
   - (Et plus...)
```

### Je suis directeur
```
1. Allez à login.html
2. Sélectionnez "Directeur"
3. Entrez vos identifiants
4. Vous accédez à:
   - TOUTES les pages de l'application
   - Supervision complète
```

## 🔒 Sécurité

- ✅ Les pages non autorisées sont bloquées automatiquement
- ✅ Les menus s'adaptent à votre rôle
- ✅ La session est sauvegardée (jusqu'à la fermeture du navigateur)
- ✅ Le bouton "Déconnexion" vous ramène à login.html

## 🧪 Mode Test

Pour tester tous les rôles:
```
http://localhost:8000/frontend/test-auth.html
```

Vous pourrez:
- ✓ Tester la connexion avec chaque rôle
- ✓ Vérifier les permissions
- ✓ Voir les user stories par rôle
- ✓ Tester la déconnexion

## 💡 Conseils

1. **Première visite**
   - Vous serez redirigé vers login.html automatiquement

2. **Déconnexion**
   - Cliquez sur "Déconnexion" dans la sidebar
   - Vous revenerez à login.html

3. **Changement de rôle**
   - Déconnectez-vous
   - Connectez-vous avec un autre rôle

4. **Pages non autorisées**
   - Si vous essayez d'accéder directement à une URL non autorisée
   - Vous serez redirigé automatiquement à l'accueil

## ❓ FAQ

**Q: Peut-on avoir plusieurs rôles?**
A: En mode démo, non. En production, il faudrait adapter le système.

**Q: Comment les mots de passe sont vérifiés?**
A: En mode démo, n'importe quel mot de passe fonctionne. En production, ils seront vérifiés par le backend.

**Q: La session persiste après fermeture du navigateur?**
A: Non, les données sont stockées dans localStorage qui se vide à la fermeture du navigateur.

**Q: Je peux accéder à d'autres rôles ?**
A: Oui! Déconnectez-vous et connectez-vous avec un autre rôle pour voir les différences.

## 🔗 Liens Utiles

- [Guide d'Authentification Complet](AUTHENTICATION_GUIDE.md)
- [Architecture Détaillée](AUTHENTICATION_ARCHITECTURE.md)
- [Implémentation](AUTHENTICATION_IMPLEMENTATION.md)
- [Page de Test](test-auth.html)

---

**Dernière mise à jour:** 2026-01-17
**État:** ✅ Opérationnel
