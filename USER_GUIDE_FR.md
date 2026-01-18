# 🚀 GUIDE UTILISATEUR - Nouveau Système

## 📋 Table des matières
1. [S'inscrire](#sincrire)
2. [Se connecter](#se-connecter)
3. [Naviguer dans le système](#naviguer-dans-le-système)
4. [Assistance](#assistance)

---

## 🔐 S'inscrire

### Étape 1: Accéder à la page d'inscription
```
1. Allez sur: http://localhost:8000/frontend/login.html
2. Cliquez sur: "S'inscrire ici →" (bouton vert)
```

### Étape 2: Remplir le formulaire
```
Email:              ✉️  votre@email.com
Identifiant:        👤  jean.dupont (min 3 caractères)
Mot de passe:       🔒  Abc12345! (8+ chars, majuscule, minuscule, chiffre)
Confirmer MDP:      🔒  Abc12345! (même password)
Rôle:               👥  Étudiant ou Formateur
```

### Étape 3: Vérifier votre email
```
1. Un code 6 chiffres est envoyé
2. En mode DÉMO: Le code s'affiche dans la console (F12)
3. Entrez le code reçu
4. Cliquez "Vérifier →"
```

### Étape 4: Succès! 🎉
```
Vous êtes redirigé vers la page de connexion
Connectez-vous avec vos identifiants
```

---

## 🔑 Se Connecter

### Étape 1: Ouvrir la page de connexion
```
http://localhost:8000/frontend/login.html
```

### Étape 2: Sélectionner votre rôle
```
Cliquez sur:
  👤 Étudiant     - Accès aux travaux et notes
  📚 Formateur    - Gestion des espaces et évaluations
  👁️  Directeur   - Accès complet au système
```

### Étape 3: Entrer vos identifiants
```
Nom d'utilisateur: jean.dupont (ou votre email)
Mot de passe:      Abc12345!
```

### Étape 4: Cliquez "Se Connecter"
```
Vous êtes redirigé vers le dashboard
```

---

## 🗂️ Naviguer dans le Système

### La Sidebar (Menu Gauche)

#### En haut: Votre Profil
```
┌─────────────────────────┐
│   [J]  Jean Dupont      │
│        Étudiant         │
└─────────────────────────┘
```

#### Au milieu: Menu par rôle

**Si Étudiant (3 options):**
```
📚 Mes Travaux
📤 Soumettre une Livraison
⭐ Mes Notes
📂 Retour Accueil
```

**Si Formateur (9 options):**
```
🏫 Créer un Espace
📋 Mes Espaces
👨‍🏫 Gérer Formateurs
👨‍🎓 Ajouter Étudiants
📝 Créer un Travail
📌 Assigner des Travaux
✅ Évaluer Livraisons
📊 Consulter Travaux
📂 Retour Accueil
```

**Si Directeur (13 options - TOUTES):**
```
Accès à tous les menus du système
```

#### En bas: Déconnexion
```
Bouton: 🚪 Déconnexion
Clic pour quitter le système
```

### Utiliser le Menu

```
1. Cliquez sur n'importe quel lien dans le menu
2. Vous êtes redirigé vers la page
3. Le menu suit à gauche
4. Cliquez sur un autre lien pour naviguer
```

---

## 🎯 Cas d'usage Typiques

### Je suis Étudiant
```
1. S'inscrire comme "Étudiant"
2. Se connecter
3. Menu affiche 3 options:
   - Voir mes travaux
   - Soumettre une livraison
   - Voir mes notes
4. Clicquez sur ce que vous voulez faire
```

### Je suis Formateur
```
1. S'inscrire comme "Formateur"
2. Se connecter
3. Menu affiche 9 options:
   - Créer/gérer les espaces
   - Ajouter des étudiants
   - Créer des travaux
   - Assigner/Évaluer les travaux
4. Gérez votre contenu pédagogique
```

### Je suis Directeur
```
1. S'inscrire avec email admin
   (ou contactez admin)
2. Se connecter
3. Menu affiche TOUS les menus:
   - Accès complet à tout
   - Gestion complète du système
4. Supervisez l'ensemble
```

---

## 🆘 Assistance

### Q: Je n'ai pas reçu le code?
**A:** 
- En mode DÉMO: Ouvrez la console (F12)
- Cherchez le message "📧 Code de vérification envoyé"
- Copiez le code 6 chiffres
- Cliquez sur "Renvoyer" pour un nouveau code

### Q: J'ai oublié mon mot de passe?
**A:** 
- Cette fonctionnalité arrive bientôt
- Pour l'instant, créez un nouveau compte

### Q: Puis-je changer mon rôle?
**A:** 
- Créez un nouveau compte avec le rôle souhaité
- À chaque connexion, vous choisissez le rôle

### Q: Je n'ai pas accès à une page?
**A:** 
- Vérifiez que vous avez sélectionné le bon rôle
- À la connexion, les rôles sont lisibles
- Certaines pages ne sont accessibles que pour certains rôles

### Q: Ma session a expiré?
**A:** 
- Vous êtes redirigé vers login.html
- Reconnectez-vous
- Votre session dure jusqu'à fermeture du navigateur

---

## 📱 Mobile

### La Sidebar sur Mobile
```
Sur petit écran (<768px):
- La sidebar se masque
- Menu accessible via hamburger (en développement)
- Cliquez sur le header pour voir le menu
```

### Navigation sur Mobile
```
1. Même processus que sur desktop
2. Tous les liens fonctionnent
3. L'écran s'adapte automatiquement
```

---

## 🔒 Sécurité

### Points Importants
```
✅ Votre email n'est jamais partagé
✅ Votre mot de passe est encodé
✅ Un code unique à chaque inscription
✅ Session valide jusqu'à déconnexion
✅ Redirection auto si non connecté
```

### Ne Partagez PAS
```
❌ Votre mot de passe
❌ Votre code de vérification
❌ Votre email de quelqu'un d'autre
```

---

## 📞 Contact & Support

Pour des problèmes:
1. Vérifiez ce guide
2. Consultez la FAQ ci-dessus
3. Contactez votre administrateur
4. Email: admin@ecole.edu

---

## ✅ Checklist de Première Utilisation

- [ ] Je me suis inscrit avec mon email
- [ ] J'ai reçu et vérifié mon code email
- [ ] Je suis connecté au système
- [ ] Je vois mon profil en haut du menu
- [ ] Le menu affiche mes options possibles
- [ ] Je peux cliquer sur les liens du menu
- [ ] Je peux me déconnecter

**Félicitations! Vous êtes prêt à utiliser le système! 🎉**

---

**Dernière mise à jour:** 17 janvier 2026
**Version:** 2.0 (Avec inscription)
